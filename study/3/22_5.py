# 튜플 표현식 사용
# tuple(식 for 변수 in 리스트 if 조건식)
# (i for i in range(10) if % 2 == 0) 이거처럼 리스트에서 한것처럼 쓰면 안됨
# 튜플이아니라 제너레이터 표현식이됨

a = tuple(i for i in range(10) if i % 2 == 0)
print(a)


n = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
l = [n[i] for i in range(len(n)) if len(n[i])==5]
# [i for i in a if len(i) == 5]
print(list(l))

a, b = map(int,(input().split()))
res = [2**i for i in range(a,b+1)]
res.pop(1)
res.pop(-2)
print(res)