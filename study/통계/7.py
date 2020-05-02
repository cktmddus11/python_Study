# 분산(variance) : 데이터들 사이에 얼마나 차이가 큰가

import math

num_friends = [100, 15, 10, 10, 9, 4, 3, 3, 2, 1]

def mean(x):
    return sum(x) / len(x) 

def dot(v, w): # 넘어온 매개변수 값
    # 편차의 제곱의 총 합 계산 
    return sum(v_i * w_i for v_i, w_i in zip (v, w)) 

def sum_of_squares(v): # 편차값 매개변수로 받아서
    return dot(v, v) # dot 함수로 편차값 넘겨주고


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

print(standard_deviation(num_friends))