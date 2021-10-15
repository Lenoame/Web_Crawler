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