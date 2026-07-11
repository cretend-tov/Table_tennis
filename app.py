from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="탁구 3D 구간 분석기", page_icon="🏓", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""<style>.block-container{max-width:1180px;padding:.4rem .5rem 1rem}header[data-testid="stHeader"]{background:transparent}iframe{border-radius:16px}</style>""", unsafe_allow_html=True)
frontend_path=Path(__file__).with_name("frontend.html")
if not frontend_path.exists():
    st.error("frontend.html 파일을 찾을 수 없습니다.")
    st.stop()
components.html(frontend_path.read_text(encoding="utf-8"), height=2450, scrolling=True)
