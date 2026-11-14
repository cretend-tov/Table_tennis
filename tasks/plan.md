# Implementation Plan: 구간별 메모 목록 + CSV 내보내기

> 샘플 계획서 — `planning-and-task-breakdown` 스킬 절차에 따라 작성

## Overview
현재 분석 메모는 기기당 1개(`localStorage["tt3d-memo"]`)만 저장되고, TXT 내보내기에는 "현재 선택 구간" 하나만 들어간다.
이를 **구간(시작~종료)·속도·메모를 한 건으로 묶어 여러 건 저장**하고, 목록에서 다시 재생하거나 **CSV(엑셀 호환)로 내보내는** 기능으로 확장한다.

## Architecture Decisions
- **저장소는 계속 localStorage 사용**: 서버·DB 없이 브라우저 안에서 처리 → 개인 영상/메모가 외부로 나가지 않음(개인정보 리스크 최소화).
- **키 분리**: 신규 키 `tt3d-memos`(JSON 배열). 기존 `tt3d-memo`는 최초 1회 목록의 첫 항목으로 이관 → 기존 사용자 데이터 보존.
- **CSV는 UTF-8 BOM 포함**: 엑셀에서 한글이 깨지지 않도록 함.
- **수정 범위는 `frontend.html` 한 파일**: `app.py`는 변경 없음.

## Task List

### Phase 1: Foundation
- [ ] Task 1: 메모 데이터 구조 + 저장/불러오기 + 기존 데이터 이관 (S)

### Checkpoint: Foundation
- [ ] 기존 메모가 사라지지 않고 새 구조로 보임

### Phase 2: Core Features
- [ ] Task 2: "구간 메모 추가" 버튼과 메모 목록 표시 (S)
- [ ] Task 3: 목록 항목 클릭 시 해당 구간 재생 + 삭제 (S)

### Checkpoint: Core Features
- [ ] 추가 → 목록 → 재생 → 삭제 흐름이 휴대폰에서 동작

### Phase 3: Polish
- [ ] Task 4: CSV 내보내기 (엑셀 한글 정상) (XS)
- [ ] Task 5: README 기능 목록 갱신 (XS)

### Checkpoint: Complete
- [ ] 모든 수용 기준 충족, 리뷰 준비 완료

## Risks and Mitigations
| Risk | Impact | Mitigation |
|------|--------|------------|
| 기존 사용자 메모 유실 | High | Task 1에서 이관 로직 우선 구현, 이관 후에도 구 키는 삭제하지 않음 |
| 엑셀에서 CSV 한글 깨짐 | Med | UTF-8 BOM(`﻿`) 추가 |
| 메모 내 쉼표·줄바꿈으로 CSV 열 밀림 | Med | 모든 필드를 큰따옴표로 감싸고 `"`는 `""`로 이스케이프 |
| 개인 브라우저/시크릿 모드에서 저장 실패 | Low | localStorage 접근을 try/catch, 실패 시 안내 문구 |

## Open Questions
- 기존 "기기에 저장" 단일 메모 칸은 유지할지, 목록으로 완전히 대체할지?
- CSV에 YouTube 링크(영상 출처)도 열로 넣을지?
