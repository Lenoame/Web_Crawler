from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://instagram.com')

# 인스타그램 자동 로그인
e = driver.find_element_by_css_selector('input[name="username"]')
e.send_keys('내아이디')
e.send_keys(Keys.ENTER)



# 2초간 코드 실행을 멈춰주세요
# time.sleep(2)
# # 여기 마침표는 클래스라는 뜻
# e = driver.find_element_by_css_selector('.b_nGN').text
# print(e)

