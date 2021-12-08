# 일반적인 하드코딩 방법
# nunu = { 
# 	'q' : 'eat', 
# 	'w' : 'snowball' 
# }
# garen = { 
# 	'q' : 'strike', 
# 	'w' : 'courage' 
# }

# 오브젝트 만드는 문법
# class 문법 : 오브젝트 한줄컷 생산해주는 기계
class Hero:
	# class에서 object 뽑을 때 초기값 부여하는 법
	# object 뽑을 때 def __init__ 실행된다
	# self는 새로 생성될 object를 뜻한다
	def __init__()
		self.q = 'eat'
		self.w = 'snowball'

nunu = Hero()
garen = Hero()
print(nunu.q)
print(nunu.w)
