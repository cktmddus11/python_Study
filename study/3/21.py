import turtle as t

t.shape('turtle')

t.forward(100) # 앞으로
t.right(90) # 거북이 방향 오른쪽으로 틀기(각도)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(300)
t.right(90)

for i in range(3): # 0 ~ 3 
    t.forward(100)
    t.right(90)

t.left(90)
t.forward(300)

t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)


t.mainloop()

# 앞으로 이동: forward, fd
# 뒤로 이동: backward, bk, back
# 왼쪽으로 회전: left, lt
# 오른쪽으로 회전: right, rt