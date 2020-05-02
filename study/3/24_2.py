# 문자열 서식 지정자와 포매팅 사용

# 서식 지정자로 문자열 넣기
a = 'I am %s.' % 'james'
print(a)

# 서식 지정자로 숫자 넣기
b = 'I am %d years old' % 22
print(b)

# 서식 지정자로 소수점 표현
c = '%.2f' % 2.3 # 2 소수점 이하 자릿수 지정
print(c)

# 서식 지정자로 문자열 정렬
d = '%10s' % 'python' # 문자열 길이를 10으로 만들고 오른쪽 정렬
# 왼쪽에는 공백 생김 
print(d)


# 서식 지정자로 문자열 안에 값 여러개 넣기
e = 'my name is %s I am %d years old' % ('seung yeon', 22)
print(e)

# format 메서드 사용
# 문자열안에 {}넣고 인덱스를 지정함 
# format에는 {} 부분에 넣을 값을 지정함
f = 'hello {0}'.format('world')
print(f)

# format 메서드로 값을 여러개 넣기
g = 'hello {0} {2} {1}'.format('python', 'Script', 3.2)
print(g)

# format 메서드에서 인덱스 대신 이름 지정하기
h = 'hello {language} {version} '.format(language='Python', version=3.6)
print(h)


# 문자열 포매팅 변수를 그대로 사용하기
language = 'C language'
version = 'none'
print(f'hello {language} {version}') # 포맷팅 뜻의 f붙이기

# format 메서드로 문자열 정렬하기
# '{인덱스:<길이}'.format(값)
i = '{0:<10}'.format('python') # 왼쪽(부등하고 가리키는 방향)
# 으로 정렬하고 남은 공간 공백으로 채움
print(i)

# 숫자 개수 맞추기
j = '%03d' % 1 # 0개수 3개
print(j)

l = '{0:03d}'.format(35)
print(l)

m = '%08.2f' % 3.6 # 전체 길이 개수 8, 소수점 이하 개수 2
print(m)

# 채우기와 정렬을 조합해서 사용
# '{인덱스:[[채우기]정렬][길이][, 자릿수][자료형]}'

# 길이를 10으로 만든 뒤, 오른쪽으로 정렬하고 남은 공간은 0으로 채움
o = '{0:x>10}'.format(15)
    #   채우기 x, 정렬 오른쪽 , 길이 10
print(o)

u = '%20s' % format(1493500, ',')
print(u)

n = '{0:>9,}'.format(1493500)
print(n)