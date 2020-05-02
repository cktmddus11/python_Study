import math
x = [0, 1, 3, 6, 12, 13, 10, 7, 5, 1]

def mean(x): # 평균
    return sum(x) / len(x)

a = mean(x)
print(mean(x))   # 5.8

variance = 0 # 편차 = 변량 - 평균
for i in range(len(x)): # 0 ~ 9
    variance += (x[i]-a)**2  # 변량 x[i] - 평균 a = 편차의 제곱의 총합 variance
variance = variance / len(x) # 분산 = 편차 제곱이 총합 / 변량의 개수
std = math.sqrt(variance) # 분산의 

print('분산 : {}'.format(variance))
print('표준 편차 : {}'.format(std))