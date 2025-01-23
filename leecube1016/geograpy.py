import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd

# Streamlit 앱 제목
st.title("📍 지역별 자동차 누적 등록 대수")

# CSV 데이터 로드
df = pd.read_csv("지역등록현황.csv", encoding='utf-8')

# 지역별 누적 등록 대수 계산
grouped_df = df.groupby("지역명")["등록대수"].sum().reset_index()

# 비율 계산 (총합 대비 비율)
total_count = grouped_df["등록대수"].sum()
grouped_df["비율(%)"] = (grouped_df["등록대수"] / total_count * 100).round(2)

# 지도 데이터 설정 (좌표는 대략적인 지역 중심점)
geo_data = {
    '서울': [37.5665, 126.9780],
    '부산': [35.1796, 129.0756],
    '대구': [35.8722, 128.6018],
    '인천': [37.4563, 126.7052],
    '광주': [35.1595, 126.8526],
    '대전': [36.3504, 127.3845],
    '울산': [35.5384, 129.3114],
    '세종': [36.4801, 127.2891],
    '경기': [37.4138, 127.5183],
    '강원': [37.8228, 128.1555],
    '충북': [36.6357, 127.4913],
    '충남': [36.6583, 126.6721],
    '전북': [35.7175, 127.1530],
    '전남': [34.8679, 126.9910],
    '경북': [36.5756, 128.5056],
    '경남': [35.4606, 128.2132],
    '제주': [33.4996, 126.5312],
}

# 지도 생성
m = folium.Map(location=[36.5, 127.5], zoom_start=7)

# 지도에 지역별 데이터 추가
for _, row in grouped_df.iterrows():
    region = row['지역명']
    cumulative_count = row['등록대수']
    if region in geo_data:
        folium.CircleMarker(
            location=geo_data[region],
            radius=cumulative_count / 100,  # 원 크기를 키우려면 분모 값을 줄임
            color="blue",
            fill=True,
            fill_color="blue",
            fill_opacity=0.6,
            popup=f"{region}: {cumulative_count:,}대"
        ).add_to(m)

# Folium 지도 표시
st.subheader("📍 자동차 등록 현황 지도")
folium_static(m)

# HTML 기반 테이블 생성
st.subheader("📊 지역별 누적 등록 대수 및 비율")
html_table = grouped_df.to_html(
    index=False,
    justify="center",
    classes=["table", "table-striped", "table-hover"],
    border=0
)

# CSS 스타일로 가운데 정렬 적용
table_styles = """
<style>
    table {
        width: 100%;
        border-collapse: collapse;
        text-align: center; /* 모든 셀의 텍스트 가운데 정렬 */
    }
    th, td {
        padding: 8px;
        border: 1px solid #ddd;
    }
    th {
        background-color: #f4f4f4;
    }
</style>
"""

# Streamlit에서 HTML로 테이블 렌더링
st.markdown(table_styles + html_table, unsafe_allow_html=True)
