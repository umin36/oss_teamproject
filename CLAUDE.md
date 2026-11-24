# CLAUDE.md

공통 규칙은 AGENTS.md에 있습니다. 규칙을 고칠 때는 AGENTS.md만 수정합니다.

@AGENTS.md

## Claude Code 전용
- GitHub 작업은 `gh` CLI로 합니다. 먼저 `gh auth status`로 로그인 상태를 확인합니다.
- `main`의 보호 규칙은 classic branch protection이 아니라 ruleset입니다. `gh api repos/umin36/oss_teamproject/rules/branches/main`으로 확인합니다.
- 이슈 연결은 `closingIssuesReferences`만으로 판단하지 말고 PR 본문의 `Issue #N`도 확인합니다.
- 팀원 PR 리뷰는 `/code-review <PR번호>`로 검토한 뒤, 사람이 확인하면 `--comment`로 게시합니다.
