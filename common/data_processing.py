## python ./data/data_processing.py
import pandas as pd

def data_process():
    차종등록현황_df = pd.read_csv("./data/data_before_processing/자동차등록대수현황_연도별_20250123043649.csv")
    차종등록현황_df = 차종등록현황_df.rename(columns={"시점": "등록연도", "레벨01(1)": "차종명", "데이터": "등록대수"})
    차종등록현황_df = 차종등록현황_df.groupby(["등록연도", "차종명"])["등록대수"].sum().reset_index()
    차종등록현황_df.to_csv("./data/csv_files/차종등록현황.csv",index=False)


    지역등록현황_df = pd.read_csv("./data/data_before_processing/전국 자동차 등록대수.csv")
    지역등록현황_df = 지역등록현황_df.dropna() # null 제거 

    지역등록현황_df['년도'] = [str(year).split(".")[0] for year in 지역등록현황_df['년도']] # 2013.0-> "2013" 문자열로 변환 
    지역등록현황_df = 지역등록현황_df[지역등록현황_df['지역명']!="합계"] # 합계 행 제거 
    지역등록현황_df = 지역등록현황_df.rename(columns={"년도": "등록연도"}).reset_index(drop=True)
    지역등록현황_df.to_csv("./data/csv_files/지역등록현황.csv",index=False)
    return

if __name__ == "__main__":
    data_process()