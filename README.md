# ttak-pul

스크롤하며 여러 장으로 나눠 찍은 스크린샷을 겹치는 부분 없이 긴 이미지 한 장으로 이어 붙여 주는 Python 라이브러리입니다. 강의 공지, 웹페이지, 채팅 기록을 캡처해 공유하는 사용자를 위해 만들었습니다.

## 1. What it does

같은 화면을 아래로 스크롤하며 찍은 PNG 스크린샷 여러 장을 받아, 이웃한 이미지 사이에서 겹치는 본문을 찾아 한 번만 남기고 긴 이미지 한 장으로 합칩니다.
(우선 초기 프로젝트 목표를 축소하여 스크린샷으로만 대상을 한정하겠습니다.)

- **입력 검증**: 이미지가 2장 이상인지, 정상적으로 열리는지, 너비가 모두 같은지 확인합니다.
- **고정 영역 정리**: 모든 캡처에 반복되는 상단 메뉴와 하단 버튼을 찾아, 결과에는 한 번씩만 남깁니다.
- **겹침 탐색**: 앞 이미지의 아래쪽과 뒤 이미지의 위쪽을 비교해 겹치는 높이를 찾습니다.
- **애매한 연결 알림**: 연결 위치가 확실하지 않으면 잘못 붙이지 않고, 확인이 필요한 이미지 쌍을 알려 줍니다.
- **합성**: 원본 너비와 색을 그대로 유지한 긴 PNG를 만듭니다.

**지원 범위**: 같은 기기·같은 화면 배율에서 위에서 아래로 순서대로 찍은 세로 스크롤 PNG만 지원합니다. 가로 스크롤, 서로 다른 배율, 촬영 순서 자동 추정은 지원하지 않습니다. 두 캡처 사이에 찍히지 않은 내용은 복원할 수 없습니다.

자세한 기획은 [docs/proposal.md](docs/proposal.md)에 있습니다.

## 2. Installation

(아래는 미리 적은 내용입니다. 아직 구현되어 있지 않습니다.)
Python 3.10 이상이 필요합니다. 현재는 테스트 서버(TestPyPI)에 올라가 있습니다.

```bash
# 1) 가상환경 만들기
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2) TestPyPI에서 설치 (Pillow, NumPy는 PyPI에서 함께 설치됨)
pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ ttak-pul==0.1.0
```

> 설치 이름은 `ttak-pul`(하이픈), 코드에서 import하는 이름은 `ttak_pul`(밑줄)입니다.

정식 PyPI에 배포한 뒤에는 아래 한 줄로 설치할 수 있습니다.

```bash
pip install ttak-pul
```

## 3. Quick start

(아래는 미리 적은 내용입니다. 아직 구현되어 있지 않습니다.)

지금 설치한 버전(0.1.0)에서 바로 실행해 볼 수 있는 예제입니다.

```python
from ttak_pul import grayscale, mean_brightness

grayscale("notice-01.png", "notice-01-gray.png")   # 흑백 사본 저장
print(mean_brightness("notice-01.png"))            # 평균 밝기 (0.0 ~ 255.0)
```

스크린샷 이어 붙이기 기능은 구현 중입니다. 완성되면 아래와 같이 사용할 예정입니다. (함수 이름과 인자는 바뀔 수 있습니다.)

```python
from ttak_pul import stitch_images

files = ["notice-01.png", "notice-02.png", "notice-03.png", "notice-04.png"]
stitch_images(files, "notice-merged.png")          # 긴 이미지 한 장으로 저장
```

## 4. Dependencies

(아래는 미리 적은 내용입니다. 아직 구현되어 있지 않습니다.)

`pyproject.toml`의 `dependencies`와 같은 목록입니다. 설치할 때 자동으로 함께 설치됩니다.

|패키지 (pip 이름)|import 이름|최소 버전|용도|라이선스|
|---|---|---|---|---|
|[Pillow](https://pypi.org/project/pillow/)|`PIL`|10|이미지 열기, 자르기, 저장|MIT-CMU (HPND)|
|[NumPy](https://pypi.org/project/numpy/)|`numpy`|1.26|픽셀 배열 계산, 겹침 유사도 계산|BSD-3-Clause|

두 라이선스 모두 허용형(permissive) 라이선스여서 이 프로젝트의 MIT 라이선스와 함께 쓸 수 있습니다.

## 5. Tests

TODO (이후 수업에서 추가 예정)

## 6. Documentation

- 문서 사이트: [https://umin36.github.io/oss_teamproject/](https://umin36.github.io/oss_teamproject/)
- API 레퍼런스 (docstring에서 자동 생성): [https://umin36.github.io/oss_teamproject/api/](https://umin36.github.io/oss_teamproject/api/)
- 기획서: [docs/proposal.md](docs/proposal.md)

함수별 상세 설명은 README가 아니라 API 페이지에 있습니다. 문서 사이트는 MkDocs로 만들며, `main`에 merge될 때마다 GitHub Actions가 자동으로 갱신합니다.

## 7. Release

TODO (이후 수업에서 추가 예정)

## 8. Team

| 이름      | GitHub                                                                       |
| ------- | ---------------------------------------------------------------------------- |
| 권민우     | [권민우](https://github.com/rnjsalsdn2007)                                      |
| 이상진     | [Sjlee-hash](https://github.com/Sjlee-hash)                                  |
| 조연수     | [joyeonsu-p](https://github.com/joyeonsu-p)                                  |
| 천지명     | [saramimni](https://github.com/saramimni)                                    |
| 최유민(PM) | [umin36](https://github.com/umin36), [UminChoi](https://github.com/UminChoi) |

- **작업 방식**: 브랜치 이름, PR 크기, 리뷰, merge 규칙은 [docs/team-rules.md](docs/team-rules.md)를 따릅니다. 모든 PR은 2명 이상의 리뷰와 승인을 받은 뒤 `--no-ff`로 merge합니다.
- **AI 사용**: AI 도구를 사용한 경우 모든 PR의 `## AI use` 항목에 사용 범위를 기록합니다. 

## 9. License

MIT License. 자세한 내용은 [LICENSE](LICENSE) 파일을 참고하세요.

Copyright (c) 2026 권민우, 이상진, 조연수, 천지명, 최유민