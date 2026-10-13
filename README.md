# 탁구 3D 구간 분석기 — Streamlit Cloud 버전

## 업로드 파일
- app.py
- frontend.html
- requirements.txt
- .streamlit/config.toml

## 배포
1. GitHub 저장소 루트에 위 파일 업로드
2. Streamlit Community Cloud에서 Create app
3. 저장소: cretend-tov/takgu-analysis-web
4. 브랜치: main
5. Main file path: app.py
6. Advanced settings에서 Python 3.12 선택
7. Deploy

기존 앱이 Table ten.py로 연결돼 있으면 app.py로 변경하거나 새 앱으로 배포하세요.

## 기능
- 휴대폰 영상 업로드
- 구간 지정 및 반복 재생
- 0.1~2배속
- 프레임 이동
- 2D 관절 오버레이
- 3D 자세 골격
- YouTube 구간 및 배속 재생
- 메모 저장 및 TXT 내보내기

## 제한
- YouTube 영상은 보안 정책 때문에 3D 추출 불가
- 업로드 영상 분석은 브라우저에서 수행
- 단일 카메라 3D는 추정치

## 개발·테스트 환경
배포에는 `requirements.txt`만 사용합니다. 브라우저 자동화 테스트(Playwright)가 필요하면:
```
pip install -r requirements-dev.txt
playwright install chromium
```
