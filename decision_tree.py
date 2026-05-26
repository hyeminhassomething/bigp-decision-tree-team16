FEATURE_NAMES = [
    "cap-shape", "cap-surface", "cap-color", "bruises", "odor",
    "gill-attachment", "gill-spacing", "gill-size", "gill-color",
    "stalk-shape", "stalk-root", "stalk-surface-above-ring",
    "stalk-surface-below-ring", "stalk-color-above-ring",
    "stalk-color-below-ring", "veil-type", "veil-color", "ring-number",
    "ring-type", "spore-print-color", "population", "habitat"
]


def load_data(path):
    data = []
    f = open(path, "r")
    for line in f:
        line = line.strip()
        if line == "":
            continue
        parts = line.split(",")
        label = parts[0]
        features = {}
        i = 0
        while i < len(FEATURE_NAMES):
            features[FEATURE_NAMES[i]] = parts[i + 1]
            i = i + 1
        sample = {"label": label, "features": features}
        data.append(sample)
    f.close()
    return data


def gini(data):
    counts = {}
    for sample in data:
        lab = sample["label"]
        counts[lab] = counts.get(lab, 0) + 1
    total = len(data)
    impurity = 1.0
    for lab in counts:
        p = counts[lab] / total
        impurity = impurity - p * p
    return impurity


def split(data, feature, value):
    left = [s for s in data if s["features"][feature] == value]
    right = [s for s in data if s["features"][feature] != value]
    return left, right


def best_split(data):
    base_gini = gini(data)
    best_gain = 0.0
    best_feature = None
    best_value = None
    total = len(data)
    for feature in FEATURE_NAMES:
        values = set()
        for s in data:
            values.add(s["features"][feature])
        for value in values:
            left, right = split(data, feature, value)
            if len(left) == 0 or len(right) == 0:
                continue
            w_left = len(left) / total
            w_right = len(right) / total
            weighted = w_left * gini(left) + w_right * gini(right)
            gain = base_gini - weighted
            if gain > best_gain:
                best_gain = gain
                best_feature = feature
                best_value = value
    return best_feature, best_value, best_gain


class Node:
    def __init__(self):
        self.feature = None
        self.value = None
        self.left = None
        self.right = None
        self.prediction = None


def majority_label(data):
    counts = {}
    for s in data:
        lab = s["label"]
        counts[lab] = counts.get(lab, 0) + 1
    best_lab = None
    best_count = -1
    for lab in counts:
        if counts[lab] > best_count:
            best_count = counts[lab]
            best_lab = lab
    return best_lab


def build_tree(data, depth, max_depth):
    node = Node()
    if gini(data) == 0.0 or depth >= max_depth:
        node.prediction = majority_label(data)
        return node
    feature, value, gain = best_split(data)
    if feature is None or gain <= 0.0:
        node.prediction = majority_label(data)
        return node
    node.feature = feature
    node.value = value
    left, right = split(data, feature, value)
    node.left = build_tree(left, depth + 1, max_depth)
    node.right = build_tree(right, depth + 1, max_depth)
    return node


def predict(node, sample):
    if node.prediction is not None:
        return node.prediction
    if sample["features"][node.feature] == node.value:
        return predict(node.left, sample)
    else:
        return predict(node.right, sample)


def print_tree(node, indent):
    if node.prediction is not None:
        print(indent + "=> predict: " + node.prediction)
        return
    print(indent + "[" + node.feature + " == " + node.value + "?]")
    print(indent + " YES:")
    print_tree(node.left, indent + "  ")
    print(indent + " NO:")
    print_tree(node.right, indent + "  ")


def accuracy(node, data):
    correct = 0
    for s in data:
        if predict(node, s) == s["label"]:
            correct = correct + 1
    return correct / len(data)


if __name__ == "__main__":
    data = load_data("mushroom.data")
    print("total samples:", len(data))

    n = len(data)
    split_point = int(n * 0.7)
    step = 0
    train = []
    test = []
    i = 0
    while i < n:
        if i % 10 < 7:
            train.append(data[i])
        else:
            test.append(data[i])
        i = i + 1
    print("train:", len(train), "test:", len(test))
    print("base gini (train):", round(gini(train), 4))

    f, v, g = best_split(train)
    print("best first split:", f, "==", v, "gain:", round(g, 4))

    print("\n--- max_depth experiment ---")
    for md in [1, 2, 3, 5]:
        tree = build_tree(train, 0, md)
        tr = accuracy(tree, train)
        te = accuracy(tree, test)
        print("max_depth =", md, "| train acc:", round(tr, 4), "| test acc:", round(te, 4))

    print("\n--- tree at max_depth=2 ---")
    tree2 = build_tree(train, 0, 2)
    print_tree(tree2, "")
