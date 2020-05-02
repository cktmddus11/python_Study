import turtle as t
 
t.shape('turtle')
t.speed('normal')      # 거북이 속도를 가장 빠르게 설정
for i in range(300):    # 300번 반복
    t.forward(i)        # i만큼 앞으로 이동. 반복할 때마다 선이 길어짐
    t.right(91)  

# print(t.shape()) 터틀모양 확인 변경가능      


t.mainloop()    