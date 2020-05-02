import copy
x = {'python': {'version': '2.7'}, 'script': {'name': 'hello.py'}}
a = x 
b = x.copy() # 얕은 복사 -> 내부 리스트는 복사 안됨 할당과 동일 따라서
# b['python']['version'] 는 x의 부분과 동일한 객체이므로 동일한 주소를 가리킴
c = copy.deepcopy(x)
x['python']['version'] = '3.6'
print(a['python']['version'], b['python']['version'], c['python']['version'])
 #     3.6                          3.6                2.6


maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}

average = sum(maria.values())/len(maria)

print(average)

keys = input().split() # 리스트로 문자열 입력
values = map(int, input().split()) # 리스트 정수 형태의 숫자 입력
 
x = dict(zip(keys, values)) 

#x = {key : values for key, values in x.items() if x.keys()!='delta' and x.values()!=30}
x = {key : values for key, values in x.items() if key !='delta' and values !=30}
#                                                   x.keys 이거 아님 주의
# x['delta'] 이거 먼저 해도 된다
print(x)