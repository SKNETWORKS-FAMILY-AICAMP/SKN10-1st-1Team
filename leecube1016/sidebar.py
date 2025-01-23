import streamlit as st
from streamlit_option_menu import option_menu
import pymysql



# 사이드바 전체 배경 스타일 변경
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-color: #D9D9D9; /* 사이드바 배경색 */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 메뉴바 생성
with st.sidebar:
    selected = option_menu(
        "Menu",  # 메뉴바 제목
        ["FAQ", "자동차 등록 현황 보고", "지역별 자동차 등록 대수"],  # 메뉴 항목
        icons=["question-circle", "file-earmark-bar-graph", "map"],  # 메뉴 아이콘
        menu_icon="list",  # 메뉴바 아이콘
        default_index=0,  # 기본 선택 항목
        styles={
            "container": {"padding": "0!important", "background-color": "#D9D9D9"},  # 사이드바 배경색
            "icon": {"color": "black", "font-size": "20px"},  # 아이콘 스타일
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "5px",
                "background-color": "#D9D9D9",  # 메뉴 항목 배경색 (사이드바와 동일)
                "--hover-color": "#ADA6A6",  # hover 시 배경색 (진한 회색)
            },
            "nav-link-selected": {
                "background-color": "#ADA6A6",  # 선택된 메뉴 항목 배경색
                "color": "white",  # 선택된 메뉴 항목 텍스트 색상
            },
        },
    )

# 각 메뉴별 페이지 내용
if selected == "FAQ":
    st.header("FAQ 페이지")
    st.write("여기는 FAQ 페이지 내용입니다.")
elif selected == "자동차 등록 현황 보고":
    st.header("자동차 등록 현황 보고 ")
    
elif selected == "지역별 자동차 등록 대수":
    st.header("지역별 자동차 등록 대수 페이지")
    st.write("지역별 자동차 등록 대수를 보여줍니다.")



