#함수에 넣어주기
#기능 축약
def nowValue():
	data = requests.get('<https://finance.naver.com/item/site.nhn?code-005930>')
	soup = BeautifulSoup(data.content, 'html.parser')
	print(soup.find_all('strong', id="_nowVal")[0].text)
	print(soup.find_all('span', class_="tah")[5].text)

nowValue()

#함수 업그레이드
#함수에 인자요소 넣어주기
def curValue(hole):
	data = requests.get(f'<https://finance.naver.com/item/site.nhn?code={hole}>')
	soup = BeautifulSoup(data.content, 'html.parser')
	print(soup.find_all('strong', id="_nowVal")[0].text)
	print(soup.find_all('span', class_="tah")[5].text)

curValue('066575') -> hole 자리에 번호를 넣을 수 있음.
#함수 하나로 다양한 코드 실행가능
#함수에 파라미터 넣어주기
#글자 중간에 변수 넣기 -> f'글자 {변수} 글자' fommating
f.write(curValue('005930') #삼성전자 가격 넣기
f.close()



#return
def curValue(hole):
	data = requests.get(f'<https://finance.naver.com/item/site.nhn?code={hole}>')
	soup = BeautifulSoup(data.content, 'html.parser')
	print(soup.find_all('strong', id="_nowVal")[0].text)
	print(soup.find_all('span', class_="tah")[5].text)
return soup.find_all('strong', id="nowVal")[0].text #현재가 리턴

#리스트에 저장하기
L = []
def curValue(hole):
	data = requests.get(f'<https://finance.naver.com/item/site.nhn?code={hole}>')
	soup = BeautifulSoup(data.content, 'html.parser')
	print(soup.find_all('strong', id="_nowVal")[0].text)
	print(soup.find_all('span', class_="tah")[5].text)
L.append(soup.find_all('strong', id="_nowVal")[0].text

