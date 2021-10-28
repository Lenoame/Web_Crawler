import requests
from bs4 import BeautifulSoup

requests.get('수집할 페이지URL') #의 경우 맨 처음 몇 개 밖에 처리를 못함
# 해결책 : 이 추가 데이터들을 달라고 네이버 서버에 요청하기

requests.get('URL2')

soup = BeautifulSoup(data.text.replace('\\', ''), 'html.parser')
print(soup.select('a.api_txt_lines'))
list = soup.select('a.api_txt_lines')

print(list[0].text) #그 안에 있는 텍스트를 출력하고 싶을 때는 .text 사용
print(list[1].text)
print(list[2].text)


print(list[1].['href']) # 블로그 URL 알고 싶을 때
print(list[2].['href'])

def blogRanking():

blogRanking('apple')
#query는 대부분 검색어 정보 어떤걸 검색했는지 알려줌
#query=귤 URL을 바꾸면 검색이 된다