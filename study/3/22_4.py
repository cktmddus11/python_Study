# 리스트 표현식 

# 리스트 안에서 for반복문과 if조건물을 사용할 수 있음 -> 컴프리헨션(list comprehension)
# 식으로 지정해서 생성된 것을 리스트로 잡아두는 것

# 리스트 안에 for문 지정
# [식 for 변수 in 리스트] -> 이게 더 좋음
# list(식 for 변수 in 리스트)

a = [i for i in range(10)] # 0부터 9까지 숫자를 생성하여 리스트를 생성
print(a)
b = list(i for i in range(10)) # 0부터 9까지 숫자를 생성하여 리스트 생성
print(b)

c = [i + 5 for i in range(10)]
print(c)

# 리스트 표현식에서 if조건문 사용하기
# [식 for 변수 in 리스트 if 조건식]
# list(식 for 변수 in 리스트 if 조건식)

d = [i for i in range(10) if i % 2 == 0] # 0 ~ 9까지 숫자 생성후 
# 2의 배수로만 리스트를 생성
print(d)

# for 반복문과 if 조건문을 여러 번 사용
# [식 for 변수1 in 리스트1 if 조건식1 for 변수2 in 리스트2 if 조건식2...]
# list(식 for 변수1 in 리스트1 if 조건식1...)
# for 이 여러개 일 때 처리 순서 뒤에서 앞
e = [i * j for i in range(2,10)
           for j in range(1, 10)]
print(e)

# 리스트에 map사용 -> 원본 리스트를 변경하지 않고 새 리스트를 생성
# list(map(함수, 리스트))
# tuple(map(함수, 튜플))

f = [1.2, 2.5, 3.7, 4.6]
for i in range(len(f)):
    f[i] = int(f[i])

g = [1.2, 2.5, 3.7, 4.6]
g = list(map(int, g))

h = list(map(str, range(10))) # 0~ 9까지 리스트 만들고 그거 문자열로 변환
print(h)

# input().split()과 map

i = input().split()
print(i) # 문자열이 들어있는 리스트가 생성

i = map(int, input().split()) # map로 정수형으로 변환
print(i) # map 객체가 만들어짐 따라서 리스트로 출력하도록 해야함
print(list(i)) # 정수가 들어있는 리스트 생성

j, k = [10, 20]
print(j) # 10
print(k) # 20

# map이 반환하는 맵 객체는 이터레이터라서 변수 여러 개에 저자하는
# 언페킹이 가능함 그래서 a, b = map(int, input().split()) 처럼 list를 생략함
# 다음과 같이 풀어낼 수 있음

x = input().split() # x에 문자열 리스트 생성
m = map(int, x) # 리스트 요소를 int로 변환, m 에 map 객체를 저장함
a, b = m # 맵 객체는 변수 여러 개에 저장할 수 있음

