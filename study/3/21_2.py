import turtle as t

t.shape()
t.color('#ccccff') # 펜의 색깔 선택
t.begin_fill() # 색칠할 영역 시작

n = int(input())
for i in range(n):
    t.forward(100)
    t.right(360 / n)

t.end_fill() # 색칠할 영역 끝

t.mainloop()