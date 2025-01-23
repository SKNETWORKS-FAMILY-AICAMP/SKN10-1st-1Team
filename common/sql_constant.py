import enum
class SELECT_SQLs(enum.Enum):
    # 1.FAQ 만 뽑아내기
    FAQ_DATA = (enum.auto(),
                """select * from faq_category""",
                "FAQ 뽑아내기")  

    # 2.검색 단어와 유사한 질의응답 뽑아내기
    SIMILAR_DATA = (enum.auto(),
                    """select * from faq_category 
                    where question like :question
                    and answer like :answer""",
                    "검색단어와 유사한 질의응답 뽑아내기")