# FizzBuzz

# 1에서 100 까지 출력
# 3의 배수는 Fizz 출력
# 5의 배수는 Buzz 출력
# 3과 5의 공배수 FizzBuzz

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0: # 얘 먼저 해야되는거 주의 
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else: 
        print(i)

# 코드 단축

# 'Fizz' + 'Buzz' -> FizzBuzz
# 'Fizz' * True -> 'Fizz'
# 'Fizz' * False -> ''

# Fizz * Fizz 이건 안되네

for i in range(1, 101):
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)

# 2와 11의 배수, 공배수 처리
for i in range(1, 101):
    if i % 2 == 0 and i % 11 == 0:
        print('FizzBuzz')
    elif i % 2 == 0:
        print('Fizz')
    elif i % 11 == 0:
        print('Buzz')
    else: print(i)
print('=====')
a, b = map(int, input().split())

for i in range(a, b+1):
    if i % 5 == 0 and i % 7 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Fizz')
    elif i % 7 == 0:
        print('Buzz')
    else: print(i)
    
