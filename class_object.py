# 일반적인 하드코딩 방법
# nunu = { 
# 	'q' : 'eat', 
# 	'w' : 'snowball' 
# }
# garen = { 
# 	'q' : 'strike', 
# 	'w' : 'courage' 
# }

# 이런식으로도 할 수 있지만 딕셔너리 자료형의 경우
# 변경하면 복사한 모든 것들에 영향을 준다
# garen = nunu
# 캐릭터2 = nunu
# 캐릭터3 = nunu
# 캐릭터3['q'] = 'sdfsdf'

# 오브젝트 만드는 문법
# class 문법 : 오브젝트 한줄컷 생산해주는 기계
class Hero:
	# class에서 object 뽑을 때 초기값 부여하는 법
	# object 뽑을 때 def __init__ 실행된다
	# self는 새로 생성될 object를 뜻한다
	def __init__(self, hole):
		self.q = hole
		self.w = 'snowball'

	def hello(self):
		# self는 언제나 class로부터 새로 생성되는 object를 뜻한다 


# object 하나 뽑는데 구멍자리에 'eat'넣어서 뽑아주세요~
nunu = Hero('eat')
# object에 구멍자리에 'strike' 넣어서 만들어주세요
garen = Hero('strike')
# hello 함수를 실행해주세요
nunu.hello()
# 가렌의 q를 실행해주세요
print(garen.q)

