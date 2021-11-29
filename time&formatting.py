import time

# 1. 현재 Epoch 시간 출력하는 법 (이걸로 뭐할 수 있나?)
a = time.time()
print(a)

# 2. 현재 ctime 출력하는 법
b = time.ctime(a)
print(b)

# 3. localtime() 으로 세부 항목만 출력하기
c = time.localtime()
print('현재시간' + str(c.tm_hour))
print(c.tm_year)

# 4. strftime()으로 시간표시형식 맘대로 바꾸기 string format time
d = time.strftime('%Y year %m month', time.localtime())
print(d)

# 5. 문자 formatting (문자중간에 변수/문자넣기)
name = 'Kim'
print('안녕하세요 %s' %name)
# '문자' + '문자' = '문자문자'
# '문자 %s문자' %변수명

# 신문법
print(f'안녕하세요 {name}')
# f'문자{변수명}'

# 시간 출력하고 싶은데 복잡한 생각 싫으면
import datetime
# 년 월 일 시 분 초
e = datetime.datetime(2022, 10, 1, 12, 12, 30)
print(e)