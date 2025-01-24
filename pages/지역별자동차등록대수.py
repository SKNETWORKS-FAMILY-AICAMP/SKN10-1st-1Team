import streamlit as st
import folium
import pandas as pd
from folium.plugins import HeatMap
from streamlit_folium import folium_static
import pymysql

# 데이터베이스 연결 설정
db_config = {
    "host": "localhost",
    "user": "dreamteam",
    "password": "1234",
    "database": "자동차현황DB",
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

# Streamlit 앱 제목
st.title('대한민국 지역별 등록대수 히트맵')

# 데이터베이스 연결
conn = get_db_connection()

if conn is not None:
    # 데이터 불러오기
    query = "SELECT * FROM 지역등록현황"
    df = pd.read_sql(query, conn)

    # 선택한 연도에 맞는 데이터 필터링
    selected_year = st.selectbox('연도를 선택하세요', sorted(df['등록연도'].unique()))
    filtered_df = df[df['등록연도'] == selected_year]

    # 등록대수 합계 및 비율 계산
    total_count = filtered_df['등록대수'].sum()
    filtered_df['비율(%)'] = (filtered_df['등록대수'] / total_count * 100).round(2)

    # 인덱스 제거
    filtered_df = filtered_df[['지역명', '등록대수', '비율(%)']].reset_index(drop=True)

    # Folium 지도 설정 (서울을 중심으로 설정)
    m = folium.Map(location=[36.5, 127.5], zoom_start=7)

    # 히트맵 데이터 생성
    heat_data = []
    for _, row in filtered_df.iterrows():
        location = location_coords.get(row['지역명'])
        if location:
            heat_data.append([location[0], location[1], row['등록대수']])
            # 지역에 Marker 추가
            folium.Marker(
                location=location,
                popup=f"{row['지역명']}: {row['등록대수']:,}대",
                icon=folium.DivIcon(html=f"""
                    <div style="font-size: 10pt; font-weight: bold; color: black; text-align: center;">
                        {row['등록대수']:,}
                    </div>
                """)
            ).add_to(m)

    # 히트맵 추가
    HeatMap(heat_data).add_to(m)

    # Folium 지도를 Streamlit에 표시
    folium_static(m)

    # 지역별 등록대수와 비율을 포함하는 표 표시
    st.subheader("📊 지역별 등록대수 및 비율")
    st.table(
        filtered_df.style.format({
            "등록대수": "{:,}",
            "비율(%)": "{:.2f}"
        }).set_properties(**{'text-align': 'center'}).set_table_styles(
            [dict(selector='th', props=[('text-align', 'center')])]
        )
    )

else:
    st.error("데이터베이스에 연결할 수 없습니다.")
