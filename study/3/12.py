# 딕셔너리
#lux = [490, 334, 550, 18.72]
# 연관된 값을 묶어서 저장하는 용도로 딕셔너리라는 자료형 이용
lux = {'health':490, 'mana':334, 'melee':550, 'armor':18.72}
# 딕셔너리 = {키1 : 값1, 키2 : 값2}
print(lux)
# 값에 문자열, 정수, 실수, 불, 리스트, 딕셔너리 등 포함하여 사용가능
# 키에는 리스트, 딕셔너리 x


# 딕셔너리 = dict(키1 = 값1) 키와 값 연결 딕셔너리 만듦 
lux1 = dict(health=490, mana = 334, melee=550, armor = 18.72)
# 딕셔너리 = dict(zip([키1, 키2],[값1, 값2])) 키 리스트와 값 리스트 묶음
lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 33, 550, 18.72]))
# 딕셔너리 = dict([(키1, 값1), (키2, 값2)]) 키, 값 튜플을 나열
lux3 = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])
# 딕셔너리 = dict({키1 : 값1, 키2 : 값2}) 중괄호 딕셔너리
lux4 = dict({'health':490, 'mana':334, 'melee':550, 'armor':18.72})


# 딕셔너리 키에 접근
# 딕셔너리[키]
print(lux['health'])

# 딕셔너리의 키에 값 할당
# 딕셔너리[키] = 값
lux['health'] = 2028 # 기존 있는거에 값 변경
print(lux)

lux['mana_regen'] = 3.89 # 새로운거 추가
print(lux)

# 딕셔너리에 키가 있는지 확인
print('health' in lux)
print('healt' not in lux)

# 딕셔너리 키 개수 
print(len(lux))

camille = {
    'health': 575.6,
    'health_regen': 1.7,
    'mana': 338.8,
    'mana_regen': 1.63,
    'melee': 125,
    'attack_damage': 60,
    'attack_speed': 0.625,
    'armor': 26,
    'magic_resistance': 32.1,
    'movement_speed': 340
}
print(camille['health'])
print(camille['movement_speed']) 


a = list(input().split())
b = map(float,list(input().split()))
c = dict(zip(a, b))
print(c)