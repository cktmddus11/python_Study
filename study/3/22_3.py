# 리스트 할당과 복사
a = [0, 0, 0, 0, 0]

b = a # 리스트를 다른 변수에 할당
# a와 b가 동일한 리스트를 가리킴 -> 리스트는 한개 있는거

print(a is b) # True

# b[2] = 99 로 리스트 b 요소를 변경하면 a 리스트 요소도 변경됨 동일한거니까

b[2] = 99
print('a리스트 : ', a)
print('b리스트 : ', b)

c = a.copy() # a리스트를 c 변수에 복사 -> 서로 다른 리스트
print(a is c) # False 서로 다른 객체니까
# a == c는 True라고 나옴 값은 동일하니까

# for 반복문으로 요소 출력하기
d = [38, 21, 53, 62, 19]

for i in d:
    print(i)

# 인덱스와 요소를 함께 출력
for index, value in enumerate(d):
    print(index+1, value) # index 0부터 시작하니까 +1해준거


# for 인덱스, 요소 in enumrate(리스트, start = 숫자):
# start로 시작 인덱스를 지정해줌
for index, value in enumerate(d, start = 1):
    print(index, value)

# for 반복문에서 인덱스로 요소를 출력하기
for i in range(len(d)):
    print(d[i])    


# while 반복문으로 요소 출력
i = 0
while i < len(a):
    print(d[i])
    i += 1

# 리스트(튜플) 에 저장된 값 중에서 가장 작은 수, 가장 큰 수,
#  요소의 합계 구하기
e = [38, 21, 53, 62, 19]
smallest = e[0]
for i in e:
    if i < smallest:
        smallest = i

print('가장 작은 값 : ', smallest)        

# sort 메서드를 이용해서
e.sort() # reverse=True 쓰면 내림차순으로 정렬
print('가장 작은 값 : ', e[0])

# 파이썬 제공 함수 min, max 함수 사용 
f =  [38, 21, 53, 62, 19]
print(min(f))
print(max(f))

# 요소의 합계 구하기
num = 0
for i in f:
    num = num + i

print(num)

# sum 함수 이용
print(sum(f))