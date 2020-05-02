import turtle as t

t.shape()

#t.circle(120) # 반지름 값 120


n = 60
a = 120
t.speed('fastest') # 거북이 속도 가장 빠르게 설정
for i in range(n):
    t.circle(a)
    t.right(360 / n) # 계산결과 6이니까 6도씩 회전하면서
    # 원을 그림

# 'fastest': 0
# 'fast': 10
# 'normal': 6
# 'slow': 3
# 'slowest': 1

t.mainloop()