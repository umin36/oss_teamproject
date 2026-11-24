# AGENTS.md

코딩 에이전트(Claude Code, Codex, Copilot, Cursor 등)가 이 저장소에서 지킬 규칙입니다.
팀 규칙의 원본은 [docs/team-rules.md](docs/team-rules.md)이며, 둘이 다르면 원본을 따릅니다.

## 프로젝트
- `ttak-pul`: 세로로 스크롤하며 찍은 PNG 스크린샷 여러 장을 긴 이미지 한 장으로 이어 붙이는 Python 라이브러리
- 기획: [docs/proposal.md](docs/proposal.md). 기능 범위는 기획서를 벗어나지 않습니다.
- 코드: `src/ttak_pul/` (설치 이름 `ttak-pul`, import 이름 `ttak_pul`)
- 의존성: Python 3.10+, Pillow, NumPy. 새 의존성은 팀 합의 없이 추가하지 않습니다.

## 개발 환경
```bash
python -m venv .venv
.venv\Scripts\activate            # macOS/Linux: source .venv/bin/activate
pip install -e . mkdocs-material "mkdocstrings[python]"
mkdocs serve                      # 문서 미리보기
```
- 테스트는 아직 없습니다. 추가되면 이 문서에 실행 명령을 적습니다.

## 코드 작성
- docstring은 Google 스타일로 씁니다. API 문서(`docs/api.md`)가 docstring에서 자동 생성됩니다.
- 공개 함수를 추가하면 `src/ttak_pul/__init__.py`의 import와 `__all__`도 함께 고칩니다.

## 브랜치와 커밋
- 브랜치 이름: `<user_name>/{feat,fix,docs,chore}/<name>` (예: `umin36/docs/agent_guide`)
- `main`에 직접 push하지 않습니다. `main`은 ruleset으로 보호됩니다.
- 커밋 메시지: `<type>: <변경 내용>` 형식으로 간단히 씁니다 (`feat`, `fix`, `docs`, `test`, `chore`).

## Pull request
- `.github/PULL_REQUEST_TEMPLATE.md`의 모든 항목(What, Why, How I tested, AI use, Checklist)을 채웁니다.
- 관련 이슈를 반드시 `Issue #N`으로 표기합니다. 이슈를 닫는 PR이면 `Closes #N`을 쓰고 README와 docstring을 업데이트합니다.
- 크기: diff 100줄 이하, 함수나 클래스는 최대 1개만 추가합니다. 초기 설정처럼 팀이 합의한 경우만 예외입니다.
- `## AI use`에는 사용한 도구, 대상 파일과 함수, 사용 방식(generated / completed / refactored / explained / reviewed)을 적습니다.
- PR을 올린 뒤 단톡방에 알리는 것은 사람이 합니다. 에이전트는 작성자에게 알림을 잊지 않도록 안내합니다.

## 리뷰
- 모든 PR은 72시간 안에 2명 이상이 리뷰하고 승인해야 머지할 수 있습니다.
- 리뷰 체크리스트
  - 모든 요구 사항을 충족했는가?
  - 생각하지 못한 부분이 있는가?
  - 테스트가 정확한가?
- 에이전트가 작성한 리뷰 코멘트에는 AI 보조로 작성했다는 사실을 밝힙니다.

## Merge
- 마지막(두 번째) 리뷰어가 merge commit 방식(`--no-ff`)으로 머지하고, 머지 후 브랜치를 삭제합니다.

## 에이전트가 사람의 확인 없이 하지 않는 일
- PR 생성, 리뷰나 코멘트 게시, 이슈 생성처럼 GitHub에 글을 남기는 일
- PR 승인(Approve), 변경 요청(Request changes), 머지
- force push, 원격 브랜치 삭제, 저장소 설정과 ruleset 변경
- 위 작업은 올릴 내용을 먼저 보여 주고, 사람이 승인한 뒤에만 실행합니다.
