# 문자열 응용 
# 1. 문자열 조작 
# 메서드를 이용해서 함 나중에 기기

# 2. 문자열 바꾸기
# replace('바꿀문자열', '새문자열')
print('Hello, world'.replace('world', 'Pyhton'))

s = 'hello world'
c = s.replace('hello', 'new word')
print(c)

# 2_2. 문자 바꾸기
# table = str.maketrans('바꿀문자열', '새문자') -> 변환 테이블 만들고
# '문자열'.translate(테이블)

table = str.maketrans('banana', '123456')
print('banana'.translate(table))


# 3. 문자열 분리하기
# split ()안에 쓴것을 기준으로 문자열 분리하여 리스트로 만듦 
a = 'apple pear grape pineapple orange'.split()
print(a)
b = 'apple, pear, grape, pineapple, orange'.split(',')
print(b)

# 4. 구분자 문자열과 문자열 리스트 연결
# join(리스트) : 구분자 문자열과 문자열과 문자열 리스트의 요소를 연결
# 하여 문자열로 만듦. 공백에 ' ' 에 join을 사용하여 각 문자열 사이에 공백이
# 들어가도록 만듦
c = ' '.join(b)
print(c)
d= '-'.join(b)
print(d)

# 5. 소문자를 대문자로 바꾸기
f = 'python'.upper()
print(f)
# 6. 대문자를 소문자로 바꾸기
g = f.lower()
print(g)

# 7. 왼쪽 공백 삭제하기
# lstrip, rstrip, strip 메서드 사용
i = '     공백삭제하기    '
print(i)
print(i.strip())

# 7_2 특정 문자 삭제하기
# 됐다 안됐다 그러는데 먼지 몰겟담
h = ',  python.'
print(h.strip('.,'))

# 문자열 정렬
n = 'python'.rjust(10)
print(n)
# 가운데 정렬
j = 'python'.center(10)
print(j)


# 8. 메서드 체이닝
# 메서드를 계속 연결해서 메서드 체이닝 가능

# ex) 문자열을 오른쪽 정렬한뒤 대문자로 바꿈
print('python'.rjust(10).upper())
# input().split() 이거도 메서드 체이닝

# 9. 문자열 왼쪽에 0채우기
print('35'.zfill(4))

# 10. 문자열 위치 찾기
# find('찾을 문자열') 없으면 -1 반환, 있으면 위치 반환
print('apple을 찾아보아랑 '.find('apple'))
# rfind 오른쪽부터 ㅊ찾

#11. 문자열 위치 찾기 index, rindex
print('apple pineapple'.index('pl'))

# 12. 문자열 개수 세기
print('apple pineapple'.count('pl'))