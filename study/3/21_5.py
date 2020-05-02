import turtle as t

# 별출력 
t.shape('turtle')
t.speed('fastest')

#for i in range(5):
 #   t.forward(100)
  #  t.right(72)
   # t.right(72)
   # t.forward(100)
   # t.left(72)
   
n, line = map(int, input().split())

for i in range(n):
    t.forward(line)
    t.right((360/n)*2)
    t.forward(line)
    t.left(360/n)

t.mainloop()