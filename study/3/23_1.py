col, row = map(int, input().split())

matrix = []
for i in range(row): # 줄 수 만큼 반복
    matrix.append(list(input())) # 입력한 값 리스트 생성
    # 생성한 리스트 matrix 리스트 요소로 추가 
                          
for i in range(len(matrix)):            
    for j in range(len(matrix[i])):
        
        print(matrix[i][j])
    print()