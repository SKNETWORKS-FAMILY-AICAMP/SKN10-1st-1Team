import streamlit as st
import pymysql
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False    

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

# Streamlit 앱 시작
st.title("📊 자동차 등록현황 보고")

# 사용자로부터 기간 선택 입력받기
start_year, end_year = st.select_slider(
    "📅 기간 선택",
    options=list(range(2014, 2025)),
    value=(2014, 2023)
)

# 데이터베이스 연결
conn = get_db_connection()

if conn is not None:
    try:
        # 디버깅용: 테이블 데이터 미리 확인
        # st.subheader("🔍 데이터 확인")
        # query_check = "SELECT * FROM 차종등록현황2 LIMIT 10"
        # df_check = pd.read_sql(query_check, conn)
        # st.write(df_check)

        # SQL 쿼리 실행
        sql = f"""
            SELECT 등록연도, SUM(등록대수) AS 등록대수
            FROM 차종등록현황
            WHERE 등록연도 BETWEEN {start_year} AND {end_year}
            GROUP BY 등록연도
            ORDER BY 등록연도
        """
        # st.write(f"디버깅용 SQL 쿼리: {sql}")  # SQL 쿼리 출력
        df = pd.read_sql(sql, conn)
        # conn.close()

        # 데이터가 없는 경우 처리
        if df.empty:
            st.warning("선택한 기간에 해당하는 데이터가 없습니다.")
        else:
            # 증감률 계산
            df['증감률(%)'] = df['등록대수'].pct_change() * 100

            # 그래프 그리기
            fig, ax1 = plt.subplots(figsize=(12, 6))

            # 첫 번째 y축 (등록대수)
            bars = ax1.bar(df['등록연도'], df['등록대수'], color='skyblue', label='등록대수')
            ax1.set_xlabel('연도', fontsize=12)
            ax1.set_ylabel('등록대수', fontsize=12)
            ax1.tick_params(axis='y')
            ax1.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))

            # 모든 연도 라벨 표시
            ax1.set_xticks(df['등록연도'])
            ax1.set_xticklabels(df['등록연도'], rotation=45)

            # 데이터 레이블 추가
            for bar in bars:
                yval = bar.get_height()
                ax1.text(bar.get_x() + bar.get_width() / 2, yval + 0.05 * yval, f'{int(yval):,}', ha='center', va='bottom')

            # 두 번째 y축 (증감률)
            ax2 = ax1.twinx()
            ax2.plot(df['등록연도'], df['증감률(%)'], color='orange', marker='o', label='증감률(%)')
            ax2.set_ylabel('증감률(%)', fontsize=12)
            ax2.tick_params(axis='y')

            # 그래프 제목 및 범례
            fig.suptitle(f"{start_year}년부터 {end_year}년까지 자동차 등록현황 및 증감률", fontsize=16)
            fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))

            # Streamlit을 통해 그래프 표시
            st.pyplot(fig)

    except Exception as e:
        st.error(f"SQL 실행 오류: {e}")
else:
    st.error("데이터베이스에 연결할 수 없습니다. 설정을 확인하세요.") 