# while 문

# i = 0
# while i < 100:
#   print('hello world!')
#   i += 1


# random 모듈 난수 발생
import random

a = random.randint(1, 6) # 정수 난수 범위 지정 함수
print(a)


i = 0
cnt = 0
while i != 3: # 3이 나오면 반복 멈춤
    i = random.randint(1, 6) 
    print(i)
    cnt = cnt + 1

print('끝, cnt : ', cnt)


# 시퀀스 객체에서 무작위로 요소 선택
dice = range(1, 7)
print(random.choice(dice))



# while 무한 루프

# while 1:
# while True:

i = 2
j = 5

while i<=32 or j>=1:
    print(i, j)
    i = i * 2
    j = j -1

money = int(input())    

while money >= 1350:
    money = money - 1350
    print(money)
    