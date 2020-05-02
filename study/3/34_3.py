# 비공개 속성 사용하기
class Person:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address

# 위 클래스 속성들은 클래스 안에서도 접근가능하고
# 외부에서도 접근 가능하다

# 클래스 바깥에서 접근 불가능하고
# 클래스 안에서만 사용할 수 있는
# 비공개 속성(Private attribute)을 만들 수 있다

class 클래스이름:
    def __init__(self, 매개변수)
        self.__속성 = 값 # __속성 -> 비공개 속성
