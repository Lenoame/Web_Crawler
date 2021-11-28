import requests
import json
import time

requests.get('https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h')


dictionary = json.loads(data.content)
# JSON -> 딕셔너리 해주는 함수

# [key][뽑을 데이터 순서][뽑을 값 key]
for i in range(200):
    times = dictionary['data'][i]['DT']
    strtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(times/1000))
    print(strtime)
    print(dictionary['data'][i]['Close'])
# 반복문으로 만들기
# 코인의 시간별 가격 200개 뽑기 완료

# formatting 문법 년-월-일 시:분:초로 변환해준다
# localtime(epoch시간)
# a = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1637308800000/1000))
# print(a)

