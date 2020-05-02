# 리스트 
# 리스트 = [값, 값, 값] 리스트에 저장된 각 값 요소라고 부름
# 리스트 여러 자료형을 모두 저장할 수 있음

# 빈 리스트
# 리스트 = []
# 리스트 = list()
a = list()
print(a)


# range 를 사용하여 리스트 만들기
# range(횟수) 0 ~ 9까지 숫자 생성
# 리스트 = list(range(횟수))
print(range(10))
a = list(range(10))
print(a)

# 리스트 = list(range(시작, 끝, 증가폭))
b = list(range(-4, 10, 2))
print(b)

# 튜플은 저장된 요소를 추가, 변경, 삭제 할 수 없음
# 요소가 변경되면 안될 떄 사용 
# 튜플 = (값, 값, 값)
# 튜플 = 값, 값, 값 

person = ('james', 17, 175.3, True)
print(person)

# (값) -> 얘는 튜플이 아니라 그냥 값 
# 요소가 한개인 튜플을 만들 때에는
# 튜플 = (값, )

# range 를 사용하여 튜플 만들기
# 튜플 = tuple(range(횟수))
# 튜플 = tuple(range(시작, 끝, 증가폭))
a = tuple(range(10))
print(a)

# 리스트와 튜플로 변수 만들기
a, b, c = [1, 2, 3]
print(a)


x = [1, 2, 3] # 리스트 변수에 저장
a, b, c = x # 리스트 저장된 변수 리스트 값 각 변수에 저장
print(2)  # 리스트와 튜플의 요소를 변수 여러 개에 할당하는
# 것을 리스트 언패킹, 튜플 언패킹이라고 함

x = input().split() # 리스트를 반환함 
print(x)
a, b  = x
print(a, b)

# 튜플 괄호 생략 가능
a = 10, 20, 30, False, 'Hello'
print(a)

a = list(range(5, -10, -2))
print(a)