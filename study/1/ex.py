# 입력한 숫자의 약수 리스트 출력
a = int(input())
b = []
for i in range(1,a+1):
    if a % i == 0:
        b.append(i)


print(b)
