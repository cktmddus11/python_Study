# 클래스에서 속성을 만들고 사용
# __init__ 메서드 안에서 self.속성 에 값을 할당
'''
class 클래스 이름:
    def __init__(self):
        self.속성 = 값 
        
'''

class Person:
    def __init__(self): # __init__ : 새로운 인스턴스를 만들때 호출되는 메서드
        # 초기화 메서드 또는 생성자 
        self.hello = '안녕하세요'
    def greeting(self):
        print(self.hello)

james = Person() # james 새로운 인스턴스 생성시 __init__메서드 호출로
# 생성 초기에 변수를 지정해줌
james.greeting()        

# self란 인스턴스 자기 자신을 의미함
'''
__init__ 의 매개변수 self에 Person() 이 들어가고 
self 가 생성된뒤 james 에 할당됨
그 후 메서드를 호출하면 james.greeting() 
def greeting(self) self에 james 가 들어감

???...
'''

# 인스턴스 만들때 값 받기
'''
class 클래스이름:
    def __init__(self, 매개변수1, 매개변수2):
        self.속성1 = 매개변수1
        self.속성2 = 매개변수2
'''
class Person2:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요'
        self.name = name 
        self.age = age
        self.address = address
    def greeting(self):
        print('{0} 저는 {1} 입니다.'.format(self.hello, self.name))

maria = Person2('마리아', 22, '서울')
maria.greeting()

# 인스턴스 속성 출력
print('이름 : ', maria.name) # 클래스 밖에서 속성 접근할때 '인스턴스.속성'
print('나이 : ', maria.age)
print('주소 : ', maria.address)

# 클래스 위치 인수, 키워드 인수
class Person3:        # 가변인수, 언패킹
    def __init__(self, *args):
        #print(type(args)) 튜플 
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]

maria = Person3(*['마리아', 20, '서울시 서초구 반포동']) # 리스트언패킹


class Person4:
    def __init__(self, **kwargs):    # 키워드 인수
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.address = kwargs['address']
 
maria1 = Person4(name='마리아', age=20, address='서울시 서초구 반포동') # 키워드 인수
maria2 = Person4(**{'name': '마리아', 'age': 20, 'address': '서울시 서초구 반포동'})
 # 딕셔너리 언패킹 
print('이름 : ', maria1.name)


# 인스턴스를 생성한 뒤에 속성 추가하기, 특정 속성만 허용하기

class Person5:
    pass

maria3 = Person5() # 인스턴스 생성
maria3.name = '마리아' # 인스턴스를 만든 뒤 속성 추가
print(maria3.name)

# 새로 인스턴스 만들었을 때는 추가한 속성이 생기지 않음
james2 = Person5()
# print(james.name) # AttributeError: 'Person' object has no attribute 'name'


# 특정 속성만 허용하고 다른 속성 제한
class Person6:
    __slots__ = ['name', 'age'] # 얘네 둘만 허용 

maria4 = Person6()
maria4.name = '마리아'
maria4.age = 20
# maria4.address = '서울' # Assigning to attribute 'address' 
# not defined in class slotspylint(assigning-non-slot)

