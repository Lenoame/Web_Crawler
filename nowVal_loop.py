import requests
from bs4 import BeautifulSoup

def nowVal(hole):
	data = requests.get(f'<https://finance.naver.com/item/site.nhn?code={hole}>')
	soup = BeautifulSoup(data.content, 'html.parser')
	print(soup.find_all('strong', id="_nowVal")[0].text)
	print(soup.find_all('span', class_="tah")[5].text)
L.append(soup.find_all('strong', id="_nowVal")[0].text
#하드 코딩
List = ['005930', '006575', '005380', '035720', '034220', '003490']

f = opne('a.txt', 'w')

f.write(nowVal(List[0])
f.write(nowVal(List[1])
.
.
.

f.close()

#반복문으로 코드를 줄이기
for i in range(6):
	f.write('\n' + nowVal(List[i]))

f.close()


#리스트 순회
#반복문 언제 쓰냐면
#1. 코드 복붙
#2. 리스트, 딕셔너리 자료 꺼낼 때
#리스트, 딕셔너리를 반복문 돌리면
#리스트 자료갯수만큼 반복됨
#i라는 변수는 리스트안에 있던 하나하나의 데이터들
for i in List:
	f.write('\n' + nowVal(i))

f.close()

