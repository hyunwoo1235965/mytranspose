#  창의적연구 및 논문 Assignment 1 & 2 제출 요약

---

## Assignment 1 - `mytranspose` 함수 구현 및 테스트

### 구현 파일
- [`main/mytranspose.py`](https://github.com/hyunwoo1235965/mytranspose/blob/main/mytranspose.py)

### 주요 기능
- 다양한 입력 타입의 전치(transpose) 수행:
  - NumPy ndarray (1D, 2D, NaN 포함)
  - pandas DataFrame
  - torch Tensor
  - 일반 Python 리스트 (v2에서 테스트)

### 테스트 파일
- [`main/testmytranspose.py`](https://github.com/hyunwoo1235965/mytranspose/blob/main/testmytranspose.py)

### 테스트 대상
- 2차원 배열, 빈 배열, 벡터, NaN 포함 벡터
- DataFrame과 Tensor
- 모든 테스트는 `unittest` 기반 자동 검증으로 구성

---

## Assignment 2 - 브랜치 분기 및 통합 시나리오

### 브랜치 구성
| 브랜치 | 설명 |
|--------|------|
| `v1` | NumPy 관련 테스트만 포함된 버전 |
| `v2` | list, torch.Tensor, pandas.DataFrame만 포함된 테스트 버전 |
| `main` | 모든 테스트를 통합한 최종 완성본 |

### PR 생성 설명
- `v1 → main` 및 `v2 → main` PR을 시도하였으나,
  현재 `main` 브랜치가 `v1` 및 `v2`와 동일한 상태로 판단되어,
  GitHub에서 “There isn’t anything to compare.” 메시지와 함께 PR 생성을 막음.
- 따라서 변경사항이 `main`에 이미 반영된 것으로 보고 영상에서 이를 설명함.

---

## 영상 구성 안내 (음성 없음)

- GitHub 페이지에서 각각의 브랜치(`main`, `v1`, `v2`) 확인
- 각 브랜치의 `mytranspose.py` 및 `testmytranspose.py` 열람
- 브랜치 간 PR 비교 화면 확인 (PR이 생성되지 않는 이유 시각적으로 확인됨)
- 코드와 테스트 항목들을 화면 중심으로 보여줌
- 전체 흐름은 README 내용 기준으로 구성

---

## 제출 링크

- 📁 GitHub Repository:  
  https://github.com/hyunwoo1235965/mytranspose

- 🎥 클라우드 녹화 영상 링크:  
  (예: https://drive.google.com/file/d/xxxxxxxxxxxxxxxx/view?usp=sharing)

---

## 부연설명 (필요 시 영상 부재 대비)

- 교수님, 본 과제 영상은 음성 없이 화면 녹화만 제공됩니다.
- 설명은 본 파일에 충분히 서술되어 있으며, 브랜치 구조와 코드 구조는 명확하게 시각적으로 제시됩니다.
- 모든 테스트는 unittest를 기반으로 자동 검증되며, 영상 내에서 코드 실행 화면도 확인 가능합니다.

감사합니다.
