# 의사결정트리 (Decision Tree) — 16조 발표 패키지

> 빅데이터프로그래밍1 팀 프로젝트 · **외부 라이브러리 0개** 순수 파이썬 구현

수업에서 배운 파이썬 문법(`list`, `dict`, `class`, 반복문, 조건문, 함수)만으로 의사결정트리 알고리즘을 처음부터 구현했습니다. numpy, pandas, sklearn 같은 머신러닝 라이브러리는 **하나도 쓰지 않았습니다**.

---

## 📁 파일 구성

| 파일 | 설명 |
|---|---|
| `decision_tree.py` | 알고리즘 본체 (6단계 함수 구조) |
| `decision_tree_presentation.ipynb` | **발표 시연용 Colab 노트북** (셀별 설명 + 실행 결과 포함) |
| `mushroom.data` | UCI Mushroom 데이터셋 (8124 샘플) — 인터넷 없이도 바로 실행 가능 |
| `DecisionTree_발표패키지.docx` | 발표/보고서 패키지 |

---

## 🚀 로컬에서 바로 돌리기 (팀원용)

### 1) 레포 클론
```bash
git clone https://github.com/<OWNER>/bigp-decision-tree-team16.git
cd bigp-decision-tree-team16
```

### 2) 알고리즘만 실행 (가장 빠름)
```bash
python3 decision_tree.py
```
출력: 첫 분기, max_depth 1/2/3/5 정확도, 깊이 2 트리 구조

### 3) 노트북 실행 (Jupyter 설치되어 있다면)
```bash
jupyter notebook decision_tree_presentation.ipynb
# 또는 VSCode에서 .ipynb 파일을 바로 열어도 됩니다
```

> 💡 **`mushroom.data`가 레포에 포함되어 있어서 인터넷 없이도 즉시 실행됩니다.**
> 노트북 첫 셀은 파일이 없을 때만 UCI에서 자동 다운로드합니다.

---

## ☁️ Colab에서 열기

**방법 1 — GitHub 경유 (가장 편함)**
1. https://colab.research.google.com 접속
2. `파일 > 노트북 열기 > GitHub` 탭
3. 검색창에 레포 URL 붙여넣기 → 노트북 선택
4. `런타임 > 모두 실행`

**방법 2 — 파일 직접 업로드**
1. `decision_tree_presentation.ipynb` 다운로드
2. Colab에서 `파일 > 노트북 업로드`로 업로드
3. `런타임 > 모두 실행`

Colab에서는 첫 셀이 자동으로 데이터를 다운로드하므로 별도 작업 불필요.

---

## 🤝 팀원 공동 작업 가이드

### 처음 한 번만
```bash
git clone https://github.com/<OWNER>/bigp-decision-tree-team16.git
cd bigp-decision-tree-team16
```

### 작업할 때마다 (브랜치 방식 권장)
```bash
git pull origin main                # 최신 상태로 맞추기
git checkout -b feat/my-change      # 내 브랜치 만들기
# ... 작업 ...
git add .
git commit -m "무엇을 바꿨는지 한 줄 요약"
git push origin feat/my-change
# GitHub 웹에서 Pull Request 만들기
```

### 빠르게 (브랜치 없이 main에 바로)
```bash
git pull origin main
# ... 작업 ...
git add .
git commit -m "수정 내용"
git push origin main
```

> ⚠️ 둘 이상이 같은 셀을 동시에 수정하면 충돌 가능성 ↑. 노트북(.ipynb)은
> JSON이라 충돌이 까다로우니 가급적 **분담해서 다른 셀/파일을 건드리기**.

---

## ✅ 검증된 출력값

노트북을 끝까지 실행하면 다음과 같이 나옵니다:

| 항목 | 값 |
|---|---|
| 전체 샘플 | 8124 (식용 51.8% / 독성 48.2%) |
| train / test 분할 | 5688 / 2436 (i % 10 < 7) |
| 첫 분기 | `odor == n` (gain ≈ 0.31) |
| max_depth=1 | train 0.888 / test 0.885 |
| max_depth=2 | train 0.952 / test 0.959 |
| max_depth=3 | train 0.985 / test 0.985 |
| max_depth=5 | train 1.000 / test 0.998 |

---

## 📚 데이터셋 출처

UCI Machine Learning Repository — Mushroom Data Set
https://archive.ics.uci.edu/ml/datasets/mushroom

특징 22개(모두 범주형), 결측치 없음, 식용(e)/독성(p) 이진 분류.
