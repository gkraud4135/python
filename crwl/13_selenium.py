from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

browser = webdriver.Chrome() # "./chromedriver.exe"

# 1. 네이버 이동
browser.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")
uid = 'gkraud4135'
upw = 'pwpw'

time.sleep(2) #로딩 대기

tag_id = browser.find_element_by_id('id')
tag_pw = browser.find_element_by_id('pw')

# id 입력
tag_id.click()
pyperclip.copy(uid)
tag_id.send_keys(Keys.CONTROL, 'v')
time.sleep(1)
# pw 입력
tag_pw.click()
pyperclip.copy(upw)
tag_pw.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

#로그인 버튼 클릭
login_btn = browser.find_element_by_id('log.login')
login_btn.click()
time.sleep(2)

# 5. id 를 새로 입력
#browser.find_element_by_id("id").send_keys("my_id")
#browser.find_element_by_id("id").clear()
#browser.find_element_by_id("id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
#browser.close() # 현재 탭만 종료
browser.quit() # 전체 브라우저 종료
