import streamlit as st

# 가상의 데이터베이스 (실제 사용 시 이 부분을 데이터베이스 연결로 대체)
database = [
    "사과는 빨간색 과일입니다.",
    "바나나는 노란색 과일입니다.",
    "오렌지는 주황색 과일입니다.",
    "포도는 보라색 또는 녹색 과일입니다.",
    "키위는 갈색 껍질에 녹색 속을 가진 과일입니다."
]

# 검색 함수
def search(query):
    return [item for item in database if query.lower() in item.lower()]

# 제목
st.title("과일 검색 앱")

# 검색어 입력창
query = st.text_input("검색어를 입력하세요:")

# 검색 버튼
if st.button("검색"):
    if query:
        results = search(query)
        if results:
            st.subheader("검색 결과:")
            for result in results:
                st.write(result)
        else:
            st.write("검색 결과가 없습니다.")
    else:
        st.write("검색어를 입력해주세요.")