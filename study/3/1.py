# 코드 입력 후 엔터 키를 누르면 바로 결과 나오는 
# 방식 인터프리터방식 이라고 부름

# 대화형 셸 
# interactive shell 대화형 셸, interactive mode 인터렉티브 모드
# 코드 읽고 평가(계산, 실행)하고, 출력 REPL(Read-Eval-Print Loop)

#.py 파일 저장한 코드 -> 파이썬 스크립트


# print함수 안에 출력할 내용 -> 함수 실행(함수 호출)
print('Hello world');print('hello world2')
a = 10
if a == 10:
    print('10입니다')


# 파이썬은 나누기를 했을 때 실수로 나옴
# 정수로 나오게 하려면 5 // 2 이렇게 해야함
print(4 / 2)
print(5//2) # 버림 나눗셈으로 소수점 이하는 버림 

# 거듭제곱 2 ** 10
print(2**10)

# 형변환 
print(int(3.3))
print(int(5/2))
print(int('10'))

# type(값) -> 자료형 알아내는 함수 

# 몫과 나머지를 함께 구하기 
print(divmod(5, 2)) # 몫 과 나머지 괄호로 출력됨
# 괄호로 출력묶은 형태를 튜플이라고 함 
quotient, remainder = divmod(5, 2)
print(quotient, remainder)

# 2 진수 : 0b
# 8 진수 : 0o
# 16 진수 : 0xF

# 실수 범위 안에 정수 -> 4.2 + 5 = 9.2 실수가 정수보다
# 표현 범위가 넓음 

# float(숫자)

print(int(0.2467 * 12 + 4.159),'층')

print(102 * 0.6 + 225)

#a, b = map(input('문자열 두개를 입력하세요 : ').split())
# split() : 공백을 기준으로 문자열 분리해서 변수에 저장
# split(',') : 콤마를 기준으로 문자열 분리해서 변수에 저장
# input, split 함수 결과값이 모두 문자열이기 때문에 
# int, float로 변환할 때 int() 를 쓰거나 map(자료형, 변환할 값)을 사용

a = 50
b = 100
c = None

print(a)
print(b)
print(c)

a, b, c, d = map(float, input().split())
print(int((a+b+c+d)/4))

print('python', 'hello world') # 그냥 공백으로 띄어서 출력됨

print(1, 2, 3, sep=', ') # sep에 콤마와 공백을 지정

print(1, 2, 3, sep='\n')
print('1\n2\n3\n')

print(1, 2, 3, end='')  # 각각 끝에 출력되는거 지정