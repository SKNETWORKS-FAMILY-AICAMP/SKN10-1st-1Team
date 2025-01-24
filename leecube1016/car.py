import streamlit as st
import pymysql
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows의 경우 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False     # 한글 폰트 사용 시 마이너스 기호 깨짐 방지

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
    return pymysql.connect(**db_config)

# Streamlit 앱 시작
st.title("📊 자동차 등록현황 보고")

# 데이터베이스 연결 및 데이터 로드
conn = get_db_connection()
sql = "SELECT 등록연도, 등록대수 FROM 차종등록현황"
df = pd.read_sql(sql, conn)
conn.close()

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
fig.suptitle(f"연도별 자동차 등록현황 및 증감률", fontsize=16)
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))

# Streamlit을 통해 그래프 표시
st.pyplot(fig)



st.markdown(
    """
    <style>
    .main-title {
        font-size: 20px; /* 지표 설명의 크기 */
        font-weight: bold; /* 굵게 표시 */
        color: black; /* 글자 색상 */
        margin-bottom: 10px; /* 아래 여백 */
    }
    .icon {
        color: #8B00FF; /* 보라색 아이콘 색상 */
        font-size: 14px; /* 아이콘 크기 */
        margin-right: 5px; /* 아이콘과 글자 사이 간격 */
    }
    .section-title {
        font-weight: bold;
        font-size: 12px; /* 제목 글씨 크기 줄임 */
        color: black;
    }
    .description {
        margin-left: 20px;
        font-size: 10px; /* 설명 글씨 크기 더 줄임 */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 지표 설명 문장 추가
st.markdown('<div class="main-title">지표 설명</div>', unsafe_allow_html=True)

# 지표 설명 작성
st.markdown(
    """
    <p><span class="icon">○</span><span class="section-title">자동차등록대수 개념</span></p>
    <p class="description">
        ○ 자동차등록대수: 통계시점에 자동차등록원부에 등록하고 운행 중인 자동차의 등록대수
        (이륜자동차 사용신고대수는 제외된 대수)
    </p>

    <p><span class="icon">■</span><span class="section-title">지표의 의의 및 활용도</span></p>
    <p class="description">
        ○ 자동차는 비교적 고가품으로 대표적인 내구재이기 때문에 경기상황에 민감, 따라서 자동차 등록대수의 추이는
        경기상황을 판단하는 지표가 될 수 있음
    </p>
    """,
    unsafe_allow_html=True,
)
