from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
from selenium.webdriver.chrome.options import Options

Options = webdriver.ChromeOptions()
Options.add_argument(r'user-data-dir=경로')
# 어떤 옵션을 추가할것인가 -> 계정정보
# 평소에 크롬브라우저로 쓰던 계정정보로 여기에 복붙하자


driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
# 로그인 페이지 주소
driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')

time.sleep(2)

pyperclip.copy('네이버아이디')

e = driver.find_element_by_css_selector('#id')
# 복붙으로 아이디/비번 입력하기
e.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

pyperclip.copy('비번')
e = driver.find_element_by_css_selector('#pw')
e.send_keys(Keys.CONTROL, 'v')

time.sleep(1)
e.send_keys(Keys.ENTER)