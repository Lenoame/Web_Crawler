from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://instagram.com')

# 인스타그램 자동 로그인
time.sleep(3)
e = driver.find_element_by_css_selector('input[name="username"]')
e.send_keys('leno1010')
e = driver.find_element_by_css_selector('input[name="password"]')
e.send_keys('asdf1234*')
e.send_keys(Keys_ENTER)

# 페이지 이동
time.sleep(2)
driver.get('https://instagram.com/explore/tags/%EC%%82%AC%EA%B3%BC/')

# 첫째사진누름
# 이 요소가 없으면 최대 10초간 기다려줘
driver.implicitly_wait(10)
e = driver.find_element_by_css_selector('._9AhH0').click()
# 클래스 명이 여러 개 있으면 멘 위에 하나만 찾아줌
# 다른 것 찾고 싶으면 element -> elements로 바꿔주기 -> 찾아서 리스트에 담아준다

# 사진 저장
img = driver.find_element_by_css_selector('.FFVAD').get_attribute('src')
urllib.request.urlretrieve(img, '1.jpg')
