# 위치 인수를 사용하는 함수를 만들고 호출하기
def print_numbers(a, b, c):
    print(a)
    print(b)
    print(c)
print_numbers(10, 20, 30)

# 언패킹 이용하기
# 함수(*리스트)
# 함수(*튜플)
x = [10,20, 30]
print_numbers(*x) # *x 리스트의 포장을 품

# 가변 인수 만들기
print('========')
def print_numbers2(*args):
    for arg in args:
        print(arg)

print_numbers2(10, 20, 30)        


# 인수 순서 정해져 인수 기억해야 해야하는  함수
def personal_info(name, age, address):
        print('이름 : ', name)
        print('나이 : ', age)
        print('주소 : ', address)

personal_info('차승연', '22', '서울특별시 은평구 역촌동')

# 정해져 있으면 불편하니까 외워야 하니까
# 키워드 인수(Keyword argument)
# 라는 기능을 제공
# 함수(키워드 = 값)

personal_info(name = '차승연2', age='22_1', address='서울')
# 키워드 함수는 인수를 순서에 상관없이 넣어도 됨

print('-------')

# 딕셔너리를 사용해 키워드 인수로 값을 넣는
# 딕셔너리 언 패킹 
# 함수(**딕셔너리)

x = {'name': '차승연', 'age':'22', 'address':'서울시'}
personal_info(**x) # 언패킹 시 아래와 동일
# personal_info(name = '차승연2', age='22_1', address='서울')


# ** 두번 사용 이유가 딕셔너리 사용해서 그럼
# * 한번하면 키값 나옴 
# 그냥 리스트값 출력일때 그래서 한번한거

# 키워드 인수를 사용하는 가변 인수 함수 만들기
# def 함수이름(**매개변수)

def personal_info2(**kwargs):
        for kw, arg in kwargs.items():
                print(kw, ':', arg, sep='')

#personal_info2(**x)
personal_info2(**{'name':'차승연'})


print('-----------')

# 함수를 호출할때 항상 인수를 넣어서 값을 전달하는데
# 이를 생략하려면 
# 매개변수에 초기값을 지정하면 됨

def personal_info3(name, age, address='비공개'):
        print('이름 ', name)
        print('나이', age)
        print('주소 : ', address)

personal_info3('차승연', '')

# 초기값을 지정하고 호출할떄 인수를 넣으면 
# 인수로 값이 전달됨

# 초기값이 지정된 매개변수의 위치
#def personal_info4(name, address='비공개', age):
 #       print('이름 ', name)
  #      print('나이', age)
   #     print('주소 : ', address)
# 위처럼 하면 문법 오류 이므로 초기값 지정된거 매개변수 
# 뒤쪽으로 써야됨


print('====')
# 연습문제
# 가장 높은 점수를 구하는 함수 만들기
korea, english, mathematics, science = 100, 86, 81, 91

def get_max_score(*arg):
        return max(arg)

max_score = get_max_score(korea, english, mathematics, science)
print('높은 점수 : ', max_score)

max_score = get_max_score(english, science)
print('높은 점수 : ', max_score)
