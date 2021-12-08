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

## 무한 스크롤 데이터 수집

무한 스크롤이 되는 페이지 데이터 수집

보통 웹사이트들은 간편하게 페이지가 나뉘어져있음

- 페이지 1 수집
- 페이지 2 수집
- 페이지 3 수집 ...
- URL로 코드를 짜면 됨
- URL 중간에 page '숫자'를 잘 보면됨

크롤러 만드는 법

1. 페이지가 나뉜 사이트면 위 설명대로 함
2. 그게 아니라 무한스크롤이나 그럴 경우... 스크롤바를 내릴 때마다 내용이 추가가 되는 경우

```python
import requests
from bs4 import BeautifulSoup

requests.get('수집할 페이지URL') #의 경우 맨 처음 몇 개 밖에 처리를 못함
# 해결책 : 이 추가 데이터들을 달라고 네이버 서버에 요청하기

requests.get('URL2')

```

개발자도구의 Network탭 들어가기

- 현재 페이지를 보여주기 위해 서버에서 받아온 모든 파일들이 있음
- 여기서 더보기 데이터 찾아보기
- 더보기 데이터가 담긴 파일을 찾은 후 그걸 서버에 따로 요청하면 크롤링 가능
- Search에 검색하기
- 검색한 데이터를 가로채기
- Headers 탭이 가장 중요함
- Request URL로 GET요청하면 더보기 데이터가 온다. 이제 스크롤 내릴 필요가 없어보임
- requests.get = GET 요청할 수 있음
- URL 적고 변수에 저장하기
- 스크롤바 내렸을 때 두번째 데이터를 얻고 싶은 경우

네이버의 경우 start=31 → start=61 보통 30개의 포스트를 보여준다

URL에서 규칙을 찾아내면 숫자만 바꿔주면 자동으로 데이터 수집 가능

가끔가다 HTML 데이터를 가져왔을 때 클래스명에 백슬래시가 들어가있는 경우가 있음

데이터에 백슬래시가 들어가 있는 경우 제거

글자에서 원하는 문자 제거해주는 함수 replace()

백슬래시를 그대로 적고 싶으면 '\\' 두 개 적어주ㅜ기

GET요청한 데이터에 .text 하면 문자로 가져옴

브라우저 주소창은 실은 GET요청을 할 수 있는 공간이다

브라우저에 잘 뜨면 여기서 검사해보기

HTML 에서 원하는 정보 뽑으려면 select사용

리스트 자료형에 잘 담아줌

블로그의 주소를 알고싶을 경우 href 붙이기

다음에 할 데이터 수집도 URL만 바꿔주기

## JSON 데이터 다루기 1 : 암호화폐 가격
암호화계 거래소 아무데나 들어가보셈

- 거기서 원하는 코인 차트 찾아보기

차트에 등장하는 가격을 수집할 순 없을까?

(가격정보가 HTML안에 없다)

Network탭에 들어가기

현재 페이지에 필요한 모든 데이터파일을 보여준다

여기서 코인가격 데이터파일을 찾아내는 식으로 크롤링 가능하다

Headers 탭을 살펴보면 이 파일 받아오려면 이런 URL로 GET요청하라고 함

굳이 HTML 분석 안해도 Network 탭에서 데이터파일을 가로채서 데이터 수집가능(운이 좋으면)

딕셔너리 자료형 { '자료이름' : '값' }

JSON 자료형 { "자료이름" : " 값" } 얘도 글자취급 받는다

큰따옴표가 있으면 의심해봐야 한다

보통 서버랑 글자데이터를 주고받을 수 있다

딕셔너리로 바꿔야 파이썬으로 편하게 조작가능

긴 딕셔너리는 어떻게 다룰까

브라우저 주소창에 URL 입력해도 GET 요청하는거랑 똑같음

어쩌구.json 파일 하나 생성하기

거기에 JSON 데이터 복붙하면 그나마 보기가 쉽다

Format Document눌러서 데이터 정렬

코드짜서 종가 출력해보기

{[{뽑을데이터}]}

자료형 데이터를 뽑을 때 괄호를 제거하는 식으로 접근해보기

## JSON 데이터 다루기 2 : 데이터 출력과 시간
일명 epoch / UNIX 시간

1970년 1월 1일부터 초단위로 나타내는 시간

- 10자리는 시간이고 뒤에 세자리는 밀리세컨드 단위로 표현하는 것이다

epoch 시간을 년월일시분초로 변환해보기

```python
import time
```

과거 가격 수백만개 수집하려면?

- 역시 URL에서 규칙파악하기

차트 뒤로 갈수록 URL 안의 time 숫자도 적어진다

- 숫자 규칙 찾아서 여러번 get 요청하면 다 수집 가능할듯

## 파이썬 멀티쓰레딩
for 돌리거나 해도 순차적으로 한줄한줄 실행된다

실전에서는 천개 만개씩 크롤링 해야되는 경우가 많다

multi-processing/multi-threading

병렬 작업 시키려면 이거 쓰면 된다

multi-processing

여러개의 파이썬 실행창 띄우기

multi-threading

CPU 병렬처리

대부분 문법이 어려움

내가 이 문법에 맞게 짰다고 해도 내가 원하는대로 동작하지 않을 수 있음

변경하고 싶은 변수에 락이 걸릴 수도 있다 → 병목현상이 일어날 수도 있음

그래서 코드 잘 자고 테스트도 잘해봐야한다

map 함수 = 동시처리 가능

multiprocessing = 멀티프로세싱 라이브러리

multiprocessing.dummy = 멀티쓰레딩 라이브러리

ide에서 색이 바뀌면 내장함수이다

map(아무 함수, 리스트)

Q. 이 리스트의 원소들을 하나씩 더해주고 싶으면 map을 이용한다

map에 들어가있는 함수에 담궜다 빼면 각각 결과를 리턴해준다

리스트 내의 모든 자료에 똑같은 작업을 시켜주고 싶을 때 map() 쓰면 편함

map(리스트에 적용할 함수, 리스트)

pool.map()

여기 넣으면 map 해주는데 알아서 멀티쓰레딩 해준다

멀티 프로세싱, 멀티쓰레딩을 하면 작업의 시간이 단축된다

일반적으로 반복문이나 코드를 나열해서 했을 경우 시간이 오래걸림

실전에선 수집필요한 모든 URL을 리스트에 담아둔 후 크롤러 함수랑 함께 map에 집어넣으면 된다

## 인스타그램 봇 만들기
단순반복 웹업무 자동화하고 싶으면 구조가 어려운 사이트 크롤링 하고 싶으면

Python + Selenium 사용하기

첫 프로젝트는 인스타그램 자동 로그인 / 데이터 수집

세팅

Selenium

Chromedriver

1. 구글에 Chromedriver 검색 후 다운 (내 크롬버전과 동일한 버전 추천)
2. selenium 라이브러리 설치

사람이 하던 다양한 웹작업 시키기 가능 클릭, 타이핑 등

물론 웹페이지에 보이는 데이터 수집도 된다

웹페이지에 보이는 글자 수집법

1. 원하는 글자 분석
2. 찾아오라고 시킴

컴퓨터야... 이 글자 좀 찾아서 가져와줘(x)

컴퓨터야... class="b_nGN"인 글자좀 찾아서 가져와줘(O)

셀레니움을 이용하면 requests보다 다이나믹하고 어려운 사이트도 쉽게 수집을 할 수 있다

case study 다른 것도 찾아보자

클래스 명이 띄어쓰기가 되있으면 여러개 부착된 것이다

id를 찾을 때

id는 페이지 내에서 하나밖에 존재할 수 없다

id는 #~~~로 넣어주기 class는 .~~~

input에 name을 찾을 때는 input[]를 이용해서 찾아주기. 기타 형식도 마찬가지

1. 수집원하는 요소를 분석한 뒤에
2. id, class, name 등으로 찾음

컨트롤 + 스페이스 같이 누르면 자동완성을 보여줄 수 있다

로그인 후 데이터수집

#사과 검색페이지의 이미지 수집

(python) 10개 수집하고 스크롤바를 내려주세요

어떻게?

1. 로그인 후
2. #사과 검색페이지 이동
3. 첫사진 클릭
4. 이미지 저장
5. 다음 누르고 이미지 저장
6. 다음 누르고 이미지 저장
7. 다음 누르고 이미지 저장...

Class로 찾을 때 주의할 점

클래스 명이 여러개일 때 사용하면 클래스 중에서 제일 위에 위치한 것만 찾아줌

그럴 때는 element를 elements로 바꾸기

그리고 클래스 명 뒤에 인덱싱 한다 ('._9AhH0')[2]

항상 코드를 짜고서 테스트를 해보기

팁 : 코드를 어떻게 짜야할지 모르겠으면 한글로 먼저 써보기

그리고 파이썬으로 번역해보기

이미지 파일로 저장하는 법

네모 박스는 전부 <div>이다

이미지는 <img>에 있음. 이미지 수집할 땐 img 태그 찾기

<img src="~~~"> 찾기 링크를 가져오면 된다

ctrl + f

다음 사진 버튼 누르기

가끔 .click()이 안된다면?

class 중복 문제를 해결해보자

어떤 사진만 정확히 찾으려면 어디에 속한 class="FFVAD"인지 알려주기

유니크한 <div> 안에 클래스 명을 적고 공백을 주고 중복되는 클래스 이름을 적는다

f'글자{변수}글자' → formatting 문법

Q. 사진 말고 동영상이면 에러가 난다

try / except 문법 사용

Q. 단시간에 너무 많이 수집하면 차단하는 사이트도 있다

time.sleep 사용

## 네이버 블로그 자동 글발행
내가 다른 블로그나 다른 카페글을 그대로 네이버 블로그로 옮겨서 하고싶을 때 사용

자동으로 네이버 블로그 글을 발행할 수 있도록 할 때

네이버 알고리즘은 양보다는 질을 중시해서 어떤 글을 쓰는지 더 봄

그냥 하던대로 send_keys 하면 사람인지 확인하는 것들(영수증에 뭐 써져있는지 확인) 하는 것이 뜬다

네이버 로그인 뚫기

1. 복사 붙여넣기 이용
    
    그냥 아이디 입력이 아니라 ctrl+v로 아이디 입력
    
    e.send_keys('dfsfaga')
    
2. 실제 브라우저처럼 꾸미기
- 이사람의 OS
- 무슨 브라우저
- 언제 어디서
- 프로필
- 

크롬브라우저 열고 chrome://version 입력

거기 뜨는 프로필경로 복붙하기

```
pip install pyperclip 설치
복사 도와주는 툴
```

네이버 AI는 우리가 어떤 페이지를 거쳐왔는지 추적이 가능하다

그래서 인간처럼 페이지 이동하는 것처럼 코드를 만들기

그리고 셀레니움으로 내용 입력하고

클릭하고 싶은거 클릭하고 발행하고

<textarea>도 글 입력할 수 있다

<div>도 글입력 가능하다

글 제목요소 찾아서 작성하기 

안에 id나 class를 상세하게 찾으면 좋다

<input> 에다가 send_keㄴys(파일경로) 이러면 파일업로드 됩니다(검색과 연구)

## os module 사용법
이런 것들은 os module로 사용하는 것이 좋다

    파일 백만개 rename하기

    파일 백만개 분류

    - 딥러닝 머신러닝
    - 데이터 분석
    - 웹서버

os module의 사용법

파이썬으로 PC 파일 조작

준비

- test 폴더 하나 만들고
- .txt 파일 아무렇게나 3개 만들기

os모듈은 PC / PC 파일 조작에 쓴다

기본으로 설치되어있음

os.listdir('test') → test 폴더에 있는 파일명들 다 알려주세요

os.rename('1파일명', '2파일명') → 1 파일명을 2 파일명으로 바꿔줌

경로를 함께 적어준다 → ex. test/4.txt 

여러 개의 파일명을 한 번에 바꿀 때는 반복문을 사용한다

Q. 변경할 파일명이 여러 개일 경우?

반복문을 사용해서 리네임 하기

Q. 조건에 맞는 것만 복사?

if in 문법 사용

파일의 경로문제

폴더나 파일의 속성에 들어가서 본 경로를 절대경로라고 한다

파일의 절대경로 입력해도 잘됩니다

다만 앞에 r을 붙여주기 (raw text) → \n 등 파이썬에서 다른 의미를 가진 내용이 있으면 코드가 제대로 동작하지 않음

os.listdir('test') → 이런 경로를 상대경로라 한다 → 이 파이썬 파일과 나란히 있는 test 폴더의 파일들을 리스트로 변환해주세요

os.listdir('C:\Users\~~~\Documents\Web_Crawler\test' ) → 이런 경로를 절대경로라 한다 → 위와 동일한 결과를 주지만 같은 프로젝트 파일에 없어도 사용이 가능함

절대경로를 사용할 때는 앞에 r을 붙여주기

os.rename( r'C:\Users\KDH\Documents\Web_Crawler\test' + f'test/{i}') 

플러스 기호를 넣어주면 경로를 합칠 수 있다

os.path.join('경로', '경로2') → 경로/경로2로 합쳐짐 → 경로 합치기 함수임(안정적인 방식)

os.getcwd() → get currect working directory

현재 파이썬 파일의 절대경로를 알려주는 함수

## 파이썬 class/object 문법
게임 정보제공 사이트를 만들고 싶다

- 그럼 캐릭터마다 정보를 자료형으로 정리하는게 우선

class 문법 : 오브젝트 한줄컷 생산해주는 기계

object 뽑을 때 def __init__ 가 실행된다

self는 새로 생성될 object를 뜻함

object 생성기계 만드시면 비슷하게 생긴 object 자료들 쉽게 생성가능

init 어쩌구 self 어쩌구 잘 쓰면 object 자료에 뭐 집어넣을지 초기값도 설정 가능하다
