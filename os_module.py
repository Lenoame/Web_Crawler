import os

# 거기 있는 파일명들 다 알려주세요

files = os.listdir(r'test')
print(files)

# 리스트 형태로 파일명 출력해줌(os에서 가장 많이 쓰는 함수)
# print(files)

# 리스트 디렉토리를 넣어서 리스트를 순회하도록 하기
# for i in os.listdir('test'):
	# formatting 문법으로 해야지 파일명이 변경된다
	# os.rename(f'test/{i}', f'text/a{i}')

# 파이썬을 이용한 파일 복사
# import shutil
# 반복문을 사용해서 파일 복사하기
# for i in os.listdir('test'):
	# 만약에 i 이름에 jpg가 들어 있으면 그 파일을 복사해주세요
	# if 'jpg' in i:
		# shutil.copy(f'test/{i}', f'test2/{i}')

# 경로 합치는 함수
os.path.join('경로', '경로2')
# 현재 파이썬 파일의 절대경로를 알려주는 함수
os.getcwd()