# 클래스 사용하기

# 특정한 개념이나 모양으로 존재하는 것을 객체라 함
# 객체를 만들기 위해 클래스를 사용

# 클래스는 속성(attribute)와 메서드(method)로 구성되어있음
#         속성은 구성되어있는것?   메서드는 기능이라 할 수 있음
# -> 객체 지향 프로그래밍(object oriented)
# 복잡한 문제를 잘게 나누어 객체로 마들고 
# 객체를 조합하여 문제를 해결함
# 해당 클래스만 수정되면 되기 때문에 유지보수에도 효율적

'''
class 클래스 이름:
    def 메서드(self): # 메서드의 첫번째 매개변수는 
        # 반드시 self로 지정해야함
        코드
''' 
class Person:
    def greeting(self):
        print('hello')

# 클래스 사용 : 클래스에 괄호 후 변수에 할당 
# 인스턴스 = 클래스()
james = Person()
# 인스턴스를 생성해야지 클래스를 사용할 수있음

# 메서드 호출 
james.greeting() # 인스턴스를 통해 메서드 호출
# '인스턴스 메서드'라고 부름



# 파이썬 기본 클래스
# 다 인스턴스를 생성해서 인스턴스를 출력함
a = int(10)
print(a)
b = list(range(10))
print(b)
c = dict(x=10, y=20)
print(c)

b.append(20) # 인스턴스 b에서 메서드 append 를 호출해서 
# 리스트에 값을 추가

# type 를 이용하면 객체가(인스턴스) 어디 클래스인지 알수 있음
print(type(b)) # <class 'list'>
print(type(james))

'''
객체와 인스턴스 차이점
인스턴스는 클래스와 연관지어서 말할 때 쓰고
객체는 리스트 변수 a, b가 있다? 
그리고 a와 b는 list클래스의 인스턴스이다
?? 그냥 대충 비슷 
'''

# 빈클래스 
class Person_2:
    pass # 빈 클래스 생성시 pass


# 메서드 안에서 메서드 호출
class Person_3:
    def greeting(self):
        print('hello')
    def hello(self): # 메서드 안에서 
        # 메서드 호출시 
        self.greeting() #self.greeting()
        # self 없이 호출하면 클래스 바깥쪽에
        # 있는 함수를 호출한다는 뜻

twit = Person_3()
twit.hello()    # hello 메서드에서 greeting 메서드를 
            # 호출하기 때문에 greeting 메서드 실행    


# 특정 클래스의 인스턴스인지 확인
# isinstance(인스턴스, 클래스)
print(isinstance(james, Person)) # True

def factorial(n):
    if not isinstance(n, int) or n < 0: # n이 정수가 아니거나 음수이면 함수를 끝냄
        return None
    if n == 1: # n 이 1 이면 
        return 1 # 1을 리턴하고 함수를 종료
    return n * factorial(n-1)
    
a=factorial(5) 
print(a)   