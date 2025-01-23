import streamlit as st
import folium
import pandas as pd
from folium.plugins import HeatMap
from streamlit_folium import folium_static

# 지역별 위도, 경도 데이터
location_coords = {
    '서울': [37.5665, 126.9780],
    '부산': [35.1796, 129.0756],
    '대구': [35.8682, 128.5916],
    '인천': [37.4563, 126.7052],
    '광주': [35.1604, 126.8514],
    '대전': [36.3504, 127.3845],
    '울산': [35.5395, 129.3114],
    '세종': [36.4801, 127.2896],
    '경기': [37.4138, 127.5183],
    '강원': [37.8228, 128.1555],
    '충북': [36.6359, 127.4916],
    '충남': [36.5182, 126.8000],
    '전북': [35.7195, 127.1397],
    '전남': [34.8167, 126.4636],
    '경북': [36.5761, 128.7325],
    '경남': [35.4606, 128.2132],
    '제주': [33.4996, 126.5312]
}

# CSV 파일 읽기 (파일 경로 수정 필요)
df = pd.read_csv('narani20\data\csv_files\지역등록현황.csv')

# Streamlit 앱 제목
st.title('2022년 대한민국 지역별 등록대수 히트맵')

# 선택한 연도에 맞는 데이터 필터링
selected_year = st.selectbox('연도를 선택하세요', df['등록연도'].unique())
filtered_df = df[df['등록연도'] == selected_year]

# Folium 지도 설정 (서울을 중심으로 설정)
m = folium.Map(location=[36.5, 127.5], zoom_start=7)

# 히트맵 데이터 생성
heat_data = []
for _, row in filtered_df.iterrows():
    location = location_coords.get(row['지역명'])
    if location:
        heat_data.append([location[0], location[1], row['등록대수']])

# 히트맵 추가
HeatMap(heat_data).add_to(m)

# Folium 지도를 Streamlit에 표시
folium_static(m)
