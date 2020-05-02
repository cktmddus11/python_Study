# 가장 많은 친구수, 가장 적은 친구 수 
# (len, max, min)
num_friends = [100,40,30,30,30,30,30,30,30,30,54,54,54,54,54,54,54,54,25,3,100,100,100,3,3]
num_points = len(num_friends)
print(num_points) # 25

max_value = max(num_friends) # 가장 많은 친구 수
print(max_value) # 100
min_value = min(num_friends)
print(min_value) # 3

# 두번째 혹은 세번째 친구수
sorted_value = sorted(num_friends) # 리스트 오름차순으로 정렬
print(sorted_value)

second_smallest_value = sorted_value[1]
second_largest_value = sorted_value[-2]

print(second_largest_value)
print(second_smallest_value)