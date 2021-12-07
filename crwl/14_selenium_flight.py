from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com"
browser.get(url) # url 로 이동

# 가는 날 선택 클릭
browser.find_elements(By.CLASS_NAME,'tabContent_option__2y4c6')[0].click()
elem = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'modal_modal__1rTeN'))
                                        )

# 이번달 27일, 다음달 28일 선택
#browser.find_elements(By.CLASS_NAME, 'calendar_tab__1ZlvZ')[1].click()
browser.find_elements(By.CLASS_NAME, 'month')[0].find_elements(By.CLASS_NAME, 'sc-crzoAE')[10].click() # [0] -> 이번달
browser.find_elements(By.CLASS_NAME, 'month')[1].find_elements(By.CLASS_NAME, 'sc-crzoAE')[10].click() # [0] -> 다음달

browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]').click()
browser.find_elements(By.CLASS_NAME, 'autocomplete_Collapse__tP3pM')[1].click()
browser.find_elements(By.CLASS_NAME, 'autocomplete_Airport__3_dRP')[0].click()

# 항공권 검색 클릭
browser.find_element(By.CLASS_NAME, 'searchBox_search__2KFn3').click()

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
    # 성공했을 때 동작 수행
    print(elem.text) # 첫번째 결과 출력
finally:
    browser.quit()

# 첫번째 결과 출력
# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
# print(elem.text)
