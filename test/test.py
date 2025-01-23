import streamlit as st
import geopandas as gpd
import folium
from folium import plugins
from folium import LinearColormap
from streamlit_folium import st_folium
import pymysql
import pandas as pd
import json
#with open('korea.json') as f:
#    data= json.load(f)


#gdf = gpd.read_file(data)

region_colors = {
    '서울특별시': 'blue',
    '광주광역시': 'yellow',
    '울산광역시': 'pink',
    '경기도도': 'brown',
    # 필요한 만큼 추가...
}

# 각 지역별로 색상 설정
def get_region_color(region_name):
    return region_colors.get(region_name, 'gray')  # 기본값은 'gray'로 설정

# Folium 지도 객체 생성
m = folium.Map(location=[36.5, 127.5], zoom_start=7)

# Streamlit에 Folium 지도 표
db_config = {
    "host": "localhost",
    "user": "team",
    "password": "1234",
    "database": "자동차현황",
    "port": 3306,
}
@st.cache_resource
def get_db_connection():
    """데이터베이스 연결 함수"""
    try:
        conn = pymysql.connect(**db_config)
        return conn
    except Exception as e:
        st.error(f"데이터베이스 연결 오류: {e}")
        return None


sql = f"""
            SELECT 등록연도, SUM(등록대수) AS 등록대수
            FROM 차종등록현황2
            WHERE 등록연도 BETWEEN {start_year} AND {end_year}
            GROUP BY 등록연도
            ORDER BY 등록연도
        """
        # st.write(f"디버깅용 SQL 쿼리: {sql}")  # SQL 쿼리 출력
        df = pd.read_sql(sql, conn)

















st.title("한반도 지역별 색깔 구분 지도")
st_folium(m, width=700, height=500)