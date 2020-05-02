# 시퀸스 자료형 : 리스트, 튜플, range, 문자열

# 시퀀스 자료형으로 만든 객체를 시퀀스 객체라고 하며, 시퀸스 객체에 들어있는 
# 각 값을 요소라고 부름 


# 특정 값이 있는지 확인하기
# 리스트 a에서 30, 100 이 있는 지 확인
a = [0, 10, 20, 30, 40, 50, 60, 80, 90]
print(30 in a)
print(100 in a)
print(34 not in a)

print(43 in (38, 76, 43, 62, 19))
print(1 in range(10))
print('p' in 'Hello, Python')

# 시퀀스 객체 연결(range는 +연산자로 객체를 연결할 수 없음-> list나 튜플로 바꿔서 연결하면 됨)
a = [0, 10, 20, 30]
b = [9, 8, 7, 6]
print(a+b)  

print('Hello'+str(10))

# 시퀸스 객체 * 정수 리스트 정수 만큼 반복(range안됨)

# 리스트와 튜플의 요소 개수 구하기
print(len(a))

print(len(range(0, 10, 1)))
print(len('hello')) # c언어처럼 null문자는 없음