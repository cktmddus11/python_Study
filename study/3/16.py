# for 와 range 사용
# for 변수 in range(횟수):
    # 반복할 코드

for i in range(10): # range 10 -> 0부터 9까지 생성 
    print(i,"안녕")  # i에 하나씩 꺼내서 대입  

# range(10) -> range(0, 10)객체 생성     

for i in range(5, 12): # 5 ~ 11
    print('hello world', i)

# 감소
for i in range(10, 0, -1): # 10 ~ 1
    print(i)    

# for 변수 in reversed(range(횟수))  숫자의 숫서를 반대로 뒤집음

# 입력한 횟수대로 반복
count = int(input('반복할 횟수를 입력하세요 : '))

for i in range(count):
    print(i)

# 시퀸스 객체로 반복
# 리스트
a = [10, 20, 30, 40, 50]

for i in a:
    print(i)

# 튜플 
fruits = ('apple', 'orange', 'grape')
for fruit in fruits:
    print(fruit)

# 문자열
for letter in 'Python':
    print(letter, end=' ')


x = [49, -17, 25, 102, 8, 62, 21]
for i in x:
    print(i * 10, end =' ')


x = int(input())

for i in range(1, 10, 1):
    print(x, '*', i, '=',x*i)
