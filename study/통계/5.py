# 친구 수의 중앙값(median)
# 평균은 누구 한명의 값이 너무 높으면 달라져 버리니까
# 중간값이용하는듯 


num_friends = [1200,15,10,10,9,4,3,3,2,1]

def mean(x):
    return sum(x) / len(x)

avgOfFriends = mean(num_friends)
print(avgOfFriends)

def median(v):
    n = len(v)
    sorted_v = sorted(v)
    print(sorted_v)
    midpoint = n // 2 # //로 나누면 몫, / 로 나누면 float로 나옴

    if n % 2 == 1: # 리스트 요소가 홀수개이면 가운데값
        return sorted_v(midpoint)
    else: # 리스트요소가 짝수개이면 
        lo = midpoint - 1 
        hi = midpoint
        return (sorted_v[lo]+sorted_v[hi])/2 # 가운데 2개의 값 평균     
        
medianOfFriends = median(num_friends)
print(medianOfFriends)

