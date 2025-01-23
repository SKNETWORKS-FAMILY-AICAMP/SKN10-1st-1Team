import sys
import os

# 프로젝트의 루트 디렉토리를 sys.path에 추가
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_path)

# faq db에서 데이터 뽑기.
from common.sql_constant import SELECT_SQLs
import streamlit as st
from sqlalchemy import text


@st.cache_resource
def get_connector():
    return st.connection(
        "faq_db",
        type = "sql",
        autocommit=True
    )

class Faq_Query:
    def __init__(self):
        self.connector = get_connector()

    def _execute_query(self,query:str,params:dict=None):
        with self.connector.connect() as conn:
            try:
                result = conn.execute(text(query),params)
                return result.fetchall()
            except Exception as e:
                st.error(f"Error executing query: {e}")
                return None
            
    def select_query_faq(self,sql_constant=SELECT_SQLs.FAQ_DATA):
        # FAQ data는 전체 다 뿌려주기
        return self._execute_query(sql_constant.value[1])

    def select_query_faq_search(self,search_word:str, sql_constant=SELECT_SQLs.SIMILAR_DATA):
        params = {
            'question':f"%{search_word}%",
            'answer':f"%{search_word}%"
        }
        return self._execute_query(sql_constant.value[1], params)
>>>>>>> origin/feature-jennyjo
