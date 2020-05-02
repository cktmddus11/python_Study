# 친구수 데이터 분포(산포도) 분산, 표준편차

# 최대, 최소 사이의 범위
num_friends = [100, 15, 10, 10, 9, 4, 3, 3, 2, 1]

def data_range(x):
    return max(x) - min(x)

print(data_range(num_friends))

# 이상 치를 제외하고 평범한 데이터 사이의 범위 
# 상, 하위 25% 사이의 차이 
def quantile(x, p):
    p_index = int(p * len(x))
    print(sorted(x) [p_index])
    return sorted(x) [p_index]

def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)

print(interquartile_range(num_friends))

#1 2 3 3 4 9 10 10 15 100 
#0 1 2 3 4 5 6   7  8   9
#10 * 0.75 = 7.5 = 7
#10 * 0.25 = 2.5 = 2 