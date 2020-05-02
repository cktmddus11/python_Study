print(1==1.0) # true
# is, is not 은 객체를 비교하기 때문에  1과 1.0 을 다르다고 판별함
print(1 is 1.0) # false
# 정수 객체와 실수 객체이기 때문에 false

print(id(1)) # 객체의 고유한 값(메모리 주소)을 구함
print(id(1.0))

a = 15
print(not a == 15)
print(not a)

b = 20
print(not b != 20)



korea, english, mathematics, science = 92, 47, 86, 81

print(korea >= 50 and english >= 50 and mathematics >= 50 and science >= 50)


