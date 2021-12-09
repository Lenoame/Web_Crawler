import requests
from bs4 import BeautifulSoup

header = {
	'User-agent' : 'Nozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
}

# 브라우저에 저장된 쿠키정보
cookie = {'session-id' : '130-0285385-8214515',
'session-id-time' : '2082787201l',
'i18n-prefs' : 'USD',
'sp-cdn' : 'L5Z9:KR',
'skin' : 'noskin',
'ubid-main' : '135-0221855-4090766'
'session-token' : '1RmwblOX82NGGHzUmgiRHhWLdQL/KFsLPnraJQiPxPL6G4yLyPXpe/nxbvoy+geHaqUgxXRNzPJPSPlVbs/y9l3LM4MC0T5b2qnQ28/fl8oV1rD98KqG29I1GAnLbjL3NK5ncl3/LtBVMG/6lQppHDZZDK51GA+JLVBbJFX+iO0gQeYtmwK676YfNnGoiCI+',
'csm-hit' : 'tv:X84QY8NGKEE16FD2262Y+b-5CEXZF00TPHZZ0Q9PSPK|1639058848542&t:1639058848542&adb:adblk_no'
}


# amazon에서 키보드 검색한 페이지를 들어가주는 코드
r = requests.get('https://www.amazon.com/s?k=keyboard&ref=nb_sb_noss_2', headers=header, cookies = cookie)
soup = BeautifulSoup(r.content, 'lxml')
print(soup.select('.a-size-medium a-color-base a-text-normal')[0])
print(r.content)
print(r.status_code)

# 크롤링 가능한 범위를 넘겼을 때는 예외처리하기
try:
	print(soup.select('.a-size-medium a-color-base a-text-normal')
except:
	print('안되네요')

# 에러나서 코드가 멈추는 것을 예방하려면
# if r.status_code == 200:
# 	print(soup.select('.a-size-medium a-color-base a-text-normal')
# else:
# 	print('에러났어요')