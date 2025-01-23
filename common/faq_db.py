import pymysql
import streamlit as st
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
from sqlalchemy import create_engine

# Selenium WebDriver 설정 
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # 브라우저 창을 띄우지 않음
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 기아 FAQ 페이지 접속
url = "https://www.kia.com/kr/customer-service/center/faq"
driver.get(url)
time.sleep(5) 

# 카테고리 이름 리스트
categories = ["TOP 10", "전체", "차량 구매", "차량 정비", "기아멤버스", "홈페이지", "PBV", "기타"]
faq_data = []

for category in categories:
    try:
        # 카테고리 버튼 선택 및 클래스 상태 변경
        category_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//button[span[contains(text(), '{category}')]]"))
        )
        # `is-active` 클래스 추가!!category 바꾸려면 꼭 필요 
        driver.execute_script("arguments[0].classList.add('is-active');", category_button) # 카테고리 버튼 활성화 
        time.sleep(1) 
        driver.execute_script("arguments[0].click();", category_button) #버튼 클릭 
        time.sleep(2) 

        # 페이지 다음으로 넘기기 
        while True:
            # 페이지 소스 가져오기
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")

            # FAQ 데이터 추출
            faq_items = soup.find_all("div", class_="cmp-accordion__item")
            for item in faq_items:
                title_tag = item.find("span", class_="cmp-accordion__title")
                title = title_tag.get_text(strip=True) if title_tag else "제목 없음"
                content_tag = item.find("div", class_="cmp-accordion__panel")
                content = content_tag.get_text(strip=True) if content_tag else "내용 없음"

                faq_data.append({
                    "category": category,
                    "question": title,
                    "answer": content
                })

            # 다음 페이지 버튼 확인
            try:
                next_button = driver.find_element(By.XPATH, "//ul[@class='paging-list']/li[@class='is-active']/following-sibling::li[1]/a")
                
                # `is-active` 클래스 추가 (강제 활성화)
                driver.execute_script("arguments[0].classList.add('is-active');", next_button)
                time.sleep(1)

                # 다음 페이지 클릭
                driver.execute_script("arguments[0].click();", next_button)
                time.sleep(3)  # 다음 페이지 로드 대기
            except Exception as e: # 다음 페이지 없으면 완료라고 생각함
                print(f"'{category}' 완료.")
                break

    except Exception as e:
        print(f"Error with category '{category}': {e}")

faq_df = pd.DataFrame(faq_data)
faq_df.to_csv("kia_faq_data.csv", index=False, encoding="utf-8-sig")

# 드라이버 종료
driver.quit()
faq_df.head()