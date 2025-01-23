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
        results = Faq_Query().select_query_faq_search(search_word=query)
        if results:
            for result in results:
                # 카테고리,질문과 답변을 각각 보여주는 위젯
                question = result[2]
                answer = result[3]
                with st.expander(question):
                    st.write(answer)
        else:
            st.write('검색결과가 없습니다.')
    else:
        st.write('검색어를 입력해주세요.')


# 3.카테고리 탭 조회
# 4.카테고리별 질의응답
## 4-1.카테고리별로 탭 나열 (카테고리: )
category_faq_list = Faq_Query().select_query_faq()


# 카테고리별로 질문과 답변 구성
faq_dict = {}
if category_faq_list:
    for row in category_faq_list:
        category = row[1]
        question = row[2]
        answer = row[3]
        if category not in faq_dict:
            faq_dict[category]=[]
        faq_dict[category].append((question,answer))
# 카테고리 탭 생성
categories = list(faq_dict.keys())
tabs = st.tabs(list(categories))
# 각 탭에 카테고리별 질문 및 답변 노출
for i,tab in enumerate(tabs):
    with tab:
        category = categories[i]  # 현재 탭의 카테고리 이름
        if category in faq_dict:
            for question, answer in faq_dict[category]:
                with st.expander(question):
                    st.write(answer)  # 질문을 클릭하면 답변이 표시됨
        else:
            st.error(f'{category} 카테고리에 대한 데이터가 없습니다.')