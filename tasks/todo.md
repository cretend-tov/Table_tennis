# TODO: 구간별 메모 목록 + CSV 내보내기

## Task 1: 메모 데이터 구조 + 저장/불러오기 + 기존 데이터 이관
**Description:** `{id, start, end, speed, text, createdAt}` 배열을 `tt3d-memos`에 저장·로드하는 함수를 만들고, 기존 `tt3d-memo` 값이 있으면 첫 항목으로 1회 이관한다.

**Acceptance criteria:**
- [ ] 새로고침 후에도 메모 목록이 유지된다
- [ ] 기존 단일 메모가 있던 브라우저에서 해당 내용이 목록에 나타난다
- [ ] localStorage 접근 실패 시 앱이 멈추지 않는다

**Verification:**
- [ ] Manual check: 개발자도구에서 `tt3d-memo`를 넣고 새로고침 → 목록 1건 확인

**Dependencies:** None
**Files likely touched:** `frontend.html`
**Estimated scope:** Small

## Task 2: "구간 메모 추가" 버튼과 메모 목록 표시
**Description:** 현재 시작/종료/속도 + 입력 메모를 한 건으로 추가하고, 카드 아래에 시간순 목록으로 보여준다.

**Acceptance criteria:**
- [ ] 버튼 1번에 1건 추가, 목록에 `00:03.2 ~ 00:05.0 · 0.5x · 메모` 형식 표시
- [ ] 빈 메모는 추가되지 않고 안내가 뜬다

**Verification:**
- [ ] Manual check: 3건 추가 후 새로고침해도 3건 유지

**Dependencies:** Task 1
**Files likely touched:** `frontend.html`
**Estimated scope:** Small

## Task 3: 목록 항목 클릭 시 해당 구간 재생 + 삭제
**Description:** 항목의 "재생"을 누르면 start/end·속도를 복원해 구간 반복 재생, "삭제"는 확인 후 제거.

**Acceptance criteria:**
- [ ] 재생 시 해당 구간 시작점부터 지정 속도로 재생
- [ ] 삭제 시 확인창 → 확인 시에만 제거

**Verification:**
- [ ] Manual check: 휴대폰 크기(390px)에서 버튼 터치 가능

**Dependencies:** Task 2
**Files likely touched:** `frontend.html`
**Estimated scope:** Small

## Checkpoint: After Tasks 1-3
- [ ] 추가 → 목록 → 재생 → 삭제 전체 흐름 동작
- [ ] 기존 기능(영상 업로드, 3D 골격, TXT 내보내기) 회귀 없음
- [ ] 사용자 검토 후 진행

## Task 4: CSV 내보내기
**Description:** 목록 전체를 `번호,시작,종료,속도,메모,작성일시` CSV로 내려받는다.

**Acceptance criteria:**
- [ ] 엑셀로 열었을 때 한글 정상, 열 밀림 없음(쉼표·줄바꿈 포함 메모도)
- [ ] 파일명 `탁구_분석_메모_YYYYMMDD.csv`

**Verification:**
- [ ] Manual check: 쉼표와 줄바꿈이 들어간 메모로 내보내 엑셀에서 확인

**Dependencies:** Task 1
**Files likely touched:** `frontend.html`
**Estimated scope:** XS

## Task 5: README 기능 목록 갱신
**Description:** README "기능" 항목에 구간 메모 목록·CSV 내보내기 추가.

**Acceptance criteria:**
- [ ] README에 신규 기능 2줄 반영

**Dependencies:** Task 4
**Files likely touched:** `README.md`
**Estimated scope:** XS

## Checkpoint: Complete
- [ ] 모든 수용 기준 충족
- [ ] Definition of Done(`.claude/references/definition-of-done.md`) 확인
