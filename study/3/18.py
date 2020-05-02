# while 에서 break로 반복문 끝내기

i = 0
while True:
    print(i)
    i += 1
    if i==100:
        break # 반복문 끝냄, while의 제어흐름을 벗어남

for i in range(10000):
    print(i)
    if i == 100:
        break # for의 제어흐름을 벗어남


# for에서 continue로 코드 실행 건너뛰기

for i in range(100):
    if i % 2 == 0:
        continue # 아래 코드를 실행하지 않고 건너뜀 
    print(i)            

# 반목문 안에 pass 입력시 반복문 형태를 유지하지만
# 아무일도 하지 않음   


i = 0
while True:       
    if i % 10 != 3:
        i += 1
        continue
    if i > 73:
        break     
    print(i, end=' ')
    i += 1


start, stop = map(int, input().split())

i = start 
while True:
    if i % 10 == 3: # 끝나는 수가3 이 아닌 숫자들 
        i += 1
        continue
    if i > stop: 
        break
    print(i, end = ' ')
    i += 1