# Web_Crawler
파이썬 웹 크롤러 만들기

## 웹크롤러 1 : 파이썬으로 웹페이지 접속과 원하는 글자 찾기

### Web Crawler

웹 크롤러 : 웹에 있는 데이터를 알아서 수집해서 저장해주는 프로그램

- 평소에 웹에서 데이터 수집 많이하면 좋음
- 데이터 기반 서비스 창업에도 쓰임
- 데이터 어디서 구할거임 ? 크롤러로 수집해야함

```basic
pip install requests
pip install bs4
pip - 라이브러리 설치할 때 쓰는 도구
```

```python
#크롤러의 기본
#파이썬으로 웹사이트 접속 도와주는 라이브러리
import requests
#파이썬으로 HTML 웹문서 분석을 도와주는 라이브러리
from bs4 import BeautifulSoup
```

크롤러의 기본

1. 파이썬(크롬이 아니라)으로 데이터 들어있는 웹사이트 접속 (그럼 HTML 도착)
2. HTML 속에서 필요한 정보만 싹 뽑기

크롬 개발자 도구 마법봉(?)을 누르고 원하는 요소 찾기

```python
data = requests.get('URL')

print(data)

<Response [200]>

#그 웹페이지에 들어있던 모든 HTML 데이터를 보여주는 코드
print(data.content) 
#그 웹페이지 접속 제대로 되고 있나 확인 가능
#성공시 200 / 실패시 400 or 500
print(data.status_code) 

#터미널에 html을 보여줌
soup = BeautifulSoup(data.content, 'html.parser')
print(soup)

#HTML에서 원하는 데이터 값(id의 데이터)뽑기
print(soup.find_all('태그명''strong', id='_nowVal'속성명[class, id 등])[0].text)
-> 어디다가 저장하기

 요소를 찾은 결과는 [리스트] 로 보여줌
```

```python
print(soup.find_all('span', class_="tah p11")[0].text)
1. class 로 찾고싶으면 class_ 언더바를 붙여줘야함
2. 띄어쓰기로 여러개 있으면 하나만 쓰기

```

<태그>에 부여된 id는 유니크함

<태그>에 부여된 class는 중복등장 가능

결론 : class로 찾으면 다 찾아주기 때문에 리스트 indexing 잘해야함


## 웹크롤러 2 : 혼자 코드짤 때 도움되는 case study

```python
import requests
from bs4 import BeautifulSoup

data = requests.get('https://finance.naver.com/item/sise.nhn?code=005930')

soup = BeautifulSoup(data.content, 'html.parser')
print(soup.find_all('strong', id="_nowVal")[0].text)
print(soup.find_all('span', class_="tah")[5].text)

#em 태그 찾아주세요
print(soup.find_all('em')

#css 셀렉터를 이용해서 찾기 가능
#내부 요소를 찾으려면 띄어쓰기
#gray 클래스에 f_down 클래스에 em 태그 찾아주세요
#html 코드를 우클릭해서 카피하면 그대로 나옴
soup.select(('.gray .f_down em')[0].text)

image = soup.select('#img_chart_area')
#image의 src를 출력해주세요
print(image['src'])

soup = BeautifulSoup(data.content, 'html.parser')
print(soup.find_all('strong', id="_nowVal")[0].text)
print(soup.find_all('span', class_="tah")[5].text)

#코드가 위에 코드하고 똑같음
#복붙하면 모든 종목 시세 수집 가능함
#반복문 사용하면 원하는 모든 종목 시세 수집 가능 (반복문 돌릴 때마다 URL만 바뀌도록)
#크롤링 잘 하려면 URL과 친해야함 
```

주식시장이 장운영시장이면 가격이 계속 새로고침되서 찾기 어려울 수 있음(주의)

1. 글자가 해체되어있는 경우 → 글자를 전부 담고 있는 클래스를 찾으면 됨.
2. class, id 하나도 없는 요소 → soup.select(' ')
3. 이미지 수집 하는법 → 이미지는 <img> → src를 보면 url이 있음. url을 타고 가면 이미지가 보인다.

<CSS selector>

- class는 .
- id 는 #
- 둘다 만족하려면 붙여쓰기 ex. 'strong#_nowVal'
- 내부 요소를 찾으려면 띄어쓰기

다른 종목 가격들 수집도 동시에하려면?

크롤러 만드는 법

1. 파이썬으로 원하는 페이지 접속해서 HTML 가져오기
2. 원하는 글자만 추리기

수집 원하는 글자는 똑같은 위치에 있음. url만 다름