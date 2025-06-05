# 📂 MyTranspose

과제의 제출용 GitHub 저장소입니다.  
`mytranspose` 함수를 직접 구현하고, 다양한 입력에 대해 테스트하며, Git 브랜치를 이용한 버전 관리 및 PR(Pull Request)까지 수행하였습니다.

---

## 🧩 과제 개요

### ✅ Assignment 1: 구현 및 테스트
- `mytranspose.py` 파일에 transpose 함수 구현
- `testmytranspose.py` 파일에 테스트 케이스 작성 (unittest 모듈 활용)
- 테스트 대상:
  - NumPy 행렬
  - 빈 행렬 (empty matrix)
  - 벡터 (1차원 배열)
  - NaN을 포함한 벡터

### ✅ Assignment 2: 브랜치 생성 및 PR
- `main` 브랜치: 최신 버전 포함 (모든 테스트 포함)
- `v1` 브랜치: **NumPy 행렬 테스트만 포함**
- `v2` 브랜치: **빈 행렬, 벡터, NaN 포함 테스트**
- PR(Pull Request) 생성 및 병합:
  - `main ← v1`
  - `main ← v2`
- 모든 PR은 충돌 없이 성공적으로 병합 완료

---

## 🧪 테스트 실행 방법

```bash
python testmytranspose.py
