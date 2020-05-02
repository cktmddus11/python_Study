
# 스택 LIFO
# append() -> 끝에다 추가 
# pop() -> 끝에꺼 삭제

# 큐 FIFO
# append() -> 끝에 추가  또는 insert(0, 요소) -> 처음에 추가
# pop(0) -> 처음꺼 삭제    또는 pop() -> 끝에꺼 삭제

# 덱(deque, double ended queue)
from collections import deque # collections 모듈에서 deque를 가져옴

a = deque([10, 20, 30])

print(a)
a.append(500) # 덱의 오른쪽 500 추가
print(a)
a.popleft() # 덱의 왼쪽 요소 하나 삭제
print(a)
a.appendleft(100) # 덱의 왼쪽에 요소 추가
print(a)
a.pop() # 덱의 오른쪽 요소 삭제
print(a)

# 리스트에서 특정 값 인덱스 구하기
# index(값)

b = [10, 20, 30, 40, 50]
print(b.index(20)) # 1
print(b[1]) # 20


# 특정 값의 개수 구하기
c = [10, 20, 30, 15, 20, 40]
print(a.count(20))

# 리스트의 순서 뒤집기
c.reverse()
print(c)

# 리스트 요소 정렬
# sort() 또는 sort(reverse=False) : 리스트의 값을 작은 순서대로 정렬(오름차순)
# sort(reverse=True) : 리스트의 값을 큰 순서대로 정렬(내림차순)
c.sort()
print('정렬 리스트 ', c)


# sort메서드, sorted 함수 
# sort메서드느 리스트를 변경하지만 
# sorted 함수는 정렬된 새 리스트를 생성함
print('새리스트',sorted(c))

# 리스트 모든 요소 삭제
c.clear()
# del c[:]
print(c)


# 리스트를 슬라이스로 조작하기
d = [10, 20, 30]
d[len(d):] = [500] # 슬라이스로 리스트 끝에 값 한개 들어잇는 리스트 추가
print(d) # d.append(500) 과 동일 
# d.extend([500]) 과 동일

# 리스트 비어있는지 확인
if not len(d): # 리스트가 비어 있으면 True
    print('리스트 d 비어있음 ')
else: print('리스트 요소 있음')

# if len(d): 리스트에 요소있으면 True
# 위에 방법보다 바로 리스트를 if문 조건으로 판단
# if not d:    if d:

# 리스트가 비어있는지 확인할 때 리스트 마지막 요소 접근할 때 d[-1] 로 하는걸 이용해서
# seq = []
# if seq: -> 리스트에 요소 있으면
#   print(seq[-1]) # 요소가 있을 때만 마지막 요소를 가져옴 

