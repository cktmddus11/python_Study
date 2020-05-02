# 2차원 리스트
# 가로 - 행 ->
# 세로 - 열 ↓
# 인덱스 0부터 시작 


# 리스트 = [[값, 값, 값], [값, 값, 값]]
a = [[10, 20], 
    [30, 40], 
    [50, 60]]
print(a)
# 리스트[세로인덱스(행)][가로인덱스(열)] = 값 
print(a[2][0])
a[2][1] = 1000
print(a)

# 톱니형 리스트
c = [[10, 20],
     [500, 600, 700],
     [9],
     [30, 40],
     [8],
     [800, 900, 1000]]

c.append([5000])
c[1].append(20) 
print(c) 

from pprint import pprint # 2차원 리스트 사각형 구조 유지 출력
pprint(c, indent=3, width=20) # indent 들여쓰기 칸수
# width 가로폭

# for 반복문 한번만 사용
for x, y in a: # a 안쪽 리스트에서 요소 두 개 꺼냄 
    print(x, y)

# for 반복문 두번만 사용
for i in a: # 안쪽 리스트 꺼냄
    for j in i:  # 안쪽 리스트에서 요소 하나씩 꺼냄
        print(j)


# for 와 range 사용
d = [[10, 20], [30, 40], [50, 60]]

for i in range(len(d)): # d리스트 안쪽 리스트 갯수 3
    for j in range(len(d[i])):  # 안쪽 리스트 요소 갯수 2
        print(d[i][j], end=' ') 
    print()

# while 반복문 한번 사용
e = [[10, 20], [30, 40], [50, 60]]

i = 0
while i < len(e): # 0 ~ 2 3번 반복 
        x, y = e[i] # 안쪽 리스트 한개 가져옴
        print(x, y)
        i+=1

# while 반복문 두번 사용
i = 0
while i < len(e): # 안쪽 리스트 개수 3 
        j = 0
        while j < len(e[i]): # 안쪽 리스트 요소 개수 2
                print(e[i][j], end=' ')
                j += 1
        print()
        i += 1


print('============')
# for문과 append를 활용하여 리스트 만드는 방법
f = [] # 빈 리스트 생성
for i in range(10):
        f.append(0) # append 로 요소 추가

print(f)

# for 반복문으로 2차원 리스트 
g = []
for i in range(3): # 안쪽 리스트 3개 만들거
        line = [] 
        for j in range(2): # 안쪽 요소 2개
                line.append(0) # 안쪽 리스트에 요소 추가
        g.append(line) # 겉 리스트에 안쪽 리스트 추가

print(g)        


# 리스트 표현식으로 2차원 리스트 만들기
h = [[0 for j in range(2)] for i in range(3)]
#         0 ~ 1 2개 안쪽 리스트 요소 생성 후 0으로 채움
#                         그 후 두번째 for문으로 0~2 3개 안쪽 리스트 만듦  

# h = [[0] * 2 for i in range(3)] 위와 동일


# 톱니형 리스트 만들기
a = [3, 1, 3, 2, 5] # 가로 크기를 저장한 리스트
b = [] # 빈 리스트 생성

for i in a: # 가로 크기를 저장한 리스트로 반복
    line = [] # 안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(i): # 리스트 a 에 저장된 가로 크기만큼 반복 
        line.append(0)
    b.append(line) # 리스트 b에 안쪽 리스트 추가

print(b)    

# sorted 로 2차원 리스트 정렬하기
# sorted(반복 가능 객체, key = 정렬함수, reverse = True 또는 False)
students = [
    ['john', 'C', 19],
    ['maria', 'A', 25],
    ['andrew', 'B', 7]
]                         # 정렬 함수로 람다 사용
print(sorted(students, key=lambda student: student[1])) # 안쪽 리스트의 인덱스 1을 기준으로 정렬
# 인덱스 1 -> ABC 이거 순으로 정렬
print(sorted(students, key=lambda student: student[2]))

 
# 2차원 리스트의 할당과 복사
# 할당은 같은 객체이지만 복사는 다른 객체이므로 다름
a = [[10, 20], [30, 40]]
b = a.copy()
b[0][0] = 500
print(a)
print(b)
# 하자만 실행해보면 a, b 둘다 바껴있음
# -> 2차원 함수는 리스트를 완전히 복사하려면 
# copy 모듈의 deepcopy함수를 사용해야함

a = [[10, 20], [30, 40]]
import copy # copy 모듈을 가져옴 
b = copy.deepcopy(a) # copy.deepcopy 함수를 사용하여 깊은 복사
b[0][0] = 500
print(a)
print(b)


a = [[[0 for col in range(3)]for row in range(4)]for depth in range(2)]
print(a)