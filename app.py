import requests
import json
import time

# requests.get('https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h')


# dictionary = json.loads(data.content)
# JSON -> 딕셔너리 해주는 함수

# [key][뽑을 데이터 순서][뽑을 값 key]
# for i in range(200):
#     times = dictionary['data'][i]['DT']
#     strtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(times/1000))
#     print(strtime)
#     print(dictionary['data'][i]['Close'])
# 반복문으로 만들기
# 코인의 시간별 가격 200개 뽑기 완료

# formatting 문법 년-월-일 시:분:초로 변환해준다
# localtime(epoch시간)
# a = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1637308800000/1000))
# print(a)

url = [
  https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1609524000000,
  https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608811200000,
  https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608098400000,
  https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1606672800000,
  https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605960000000,
  https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605242700000,
  https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1604534400000,
  https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603821600000,
  https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603108800000,
  https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1602396000000,
]

def jsonCrawler(link):
	data = requests.get('~~~')
	dictionary = json.loads(data.content)
	print(dictionary['data'][0]['Close'])

# 여기 있던 첫번째 URL을 크롤링하려면?
jsonCralwer(url[0])

# for i in range(len(url)):
#	 jsonCralwer(url[i])

# lists = [2, 3, 4, 5, 6]
# def add(x):
# 	return x + 1

# result = map(add, lists)
# print(result)


# 멅티쓰레딩으로 코드 실행시키는 법
from multiprocessing.dummy import Pool as ThreadPool

pool = ThreadPool(4)
# map함수 = 동시처리 가능
# 이 리스트에 있던 하나하나의 자료가 jsonCralwer에 들어갔다 나온다
result = pool.map(jsonCrawler, url)
pool.close()
pool.join()