# 상관관계 : 두 특성사이의 연관관계를 말해줌
# 사이트 접속시간, 경력기간 경력이 길수록 사이트 접속시간이 긴가?
def mean(x):
    return sum(x) / len(x) 

def dot(v, w): # 넘어온 매개변수 값
    # 편차의 제곱의 총 합 계산 
    return sum(v_i * w_i for v_i, w_i in zip (v, w)) 

def de_mean(x): # 요소(변량)들과 평균의 차이 = 편차 
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]


def variance(x):
    n = len(x)
    deviations = de_mean(x) # 편차값 deviations 에 저장 
    return sum_of_squares(deviations) / (n-1) # n보다 n-1로 나누어야 더 잘 보정됨
    # 편차의 제곱 총합 / 변량의 개수 -1 
print(variance(num_friends)) # 분산출력


def standard_deviation(x): # 표준편차 : 분산의 루트값
    return math.sqrt(variance(x)) 


# 공분산
def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n-1)

print(covariance(connection_time, working_time))    

# 상관관계 -1 ~ 1
def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)

    if stdev_x >0 and stdev_y >0:
        return convariance(x, y) / stdev_x / stdev_y
    else:
        return 0: