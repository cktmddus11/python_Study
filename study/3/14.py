
jumsu = list(input().split())

if 0<=int(jumsu[0])<=100 and  0<=int(jumsu[1])<=100 and 0<=int(jumsu[2])<=100 and 0<=int(jumsu[3])<=100:      
    result = (int(jumsu[0])+int(jumsu[1])+int(jumsu[2])+int(jumsu[3])) // 4
    print(result)
    if result >= 80:
        print('합격')s
    else: 
        print('불합격')
else:
      print('잘못된 숫자')
 