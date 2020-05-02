# for i in range(횟수): -> 바깥쪽 루프/ 세로 처리(행) 
#   for j in range(횟수): -> 안쪽 루프
#           가로 처리 코드(열)
#   코드


for i in range(5): # 0 ~ 4 5번 반복 -> 행
    for j in range(5): # 5번 반복 -> 열 
        print('j:', j, sep='', end=' ')
    print('i:', i, '\\n', sep='')    

print()

for i in range(5):
    for j in range(5):
        print('*', end='') # 줄바꿈 없앰
    print() # print 기본 줄바꿈 지정되있음 

print()
for i in range(3):
    for j in range(6):
        print('*',end='')
    print()
    
print()
for i in range(5):
    for j in range(5):
        if j<=i:
            print('*', end='')

    print()   


print()
for i in range(5): # 0 ~ 5
    for j in range(i+1): 
        print('*', end='')

    print()           


print()    


for i in range(5): # 행
    for j in range(5): # 열 
        if j == i:
            print('*', end='')
        else: print(' ', end='')
    print()


print()


for i in range(5):
    for j in range(5):
        if j<i:
            print(' ', end='')
        else: print('*', end='')    
    print()


print()

a = int(input())

for i in range(a):
    for j in reversed(range(a)):
        if j>i:
            print(' ', end='')
        else: 
            print('*', end='')        
    for j in range(a):
        if j<i:
            print('*', end='')            
    print()                


