import requests

requests.get('https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h')
print(data.content)

dictionary = json.loads(data.content)
# JSON -> 딕셔너리 해주는 함수

# [key][뽑을 데이터 순서][뽑을 값 key]
print(dictionary['data'][0]['Close'])
