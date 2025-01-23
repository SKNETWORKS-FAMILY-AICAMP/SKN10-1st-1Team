"""
1.넘어온 ERD 및 DB를 SQL로 만들기
2.DB를 파이썬과 연결하여 스트림릿에 뿌릴 데이터를 뽑는 SQL문 작성하기
3.스트림릿 구현 (데이터 삽입 위치도 고려)
4.뽑아낸 데이터를 스트림릿에 뿌리기
"""
import sys
import os

# 프로젝트의 루트 디렉토리를 sys.path에 추가
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_path)


import streamlit as st
from common.faq_db import Faq_Query

st.title('FAQ 페이지')
# 1.검색어 입력창
# 2.검색시 관련 질문이 질문 입력란 밑에 뜸.

query = st.text_input('검색어를 입력하세요:')

if st.button('검색'):
    if query:
        results = Faq_Query(search_word=query).select_query_faq_search()
        if results:
            st.subheader('검색결과: ')
            for result in results:
                st.write(result)
        else:
            st.write('검색결과가 없습니다.')
    else:
        st.write('검색어를 입력해주세요.')

# 3.카테고리 탭 조회
# 4.카테고리별 질의응답
## 4-1.카테고리별로 탭 나열 (카테고리: )
## 4-2.질문 ( > 화살표 누르면 화살표가 밑으로 내려가면서 답변 보임 )
## 4-3.질문별로 답변 보임

tabs = st.tabs(['cat1','cat2','cat3']) # result에서 tab부분만 뽑기
faqs = {
    "카테고리1": [
        {"질문": "질문 1-1", "답변": "답변 1-1입니다."},
        {"질문": "질문 1-2", "답변": "답변 1-2입니다."},
    ],
    "카테고리2": [
        {"질문": "질문 2-1", "답변": "답변 2-1입니다."},
        {"질문": "질문 2-2", "답변": "답변 2-2입니다."},
    ],
    "카테고리3": [
        {"질문": "질문 3-1", "답변": "답변 3-1입니다."},
        {"질문": "질문 3-2", "답변": "답변 3-2입니다."},
    ],
}

for i, (tab,faq_list) in enumerate(zip(tabs,faqs.values())):
    with tab:
        for faq in faq_list:
            with st.expander(faq['질문']):
                st.write(faq['답변'])