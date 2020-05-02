import collections
import matplotlib.pyplot as plt

num_friends = [100,40,30,30,30,30,30,30,30,30,54,54,54,54,54,54,54,54,25,3,100,100,100,3,3]

friend_counts = collections.Counter(num_friends)
print('friends:', friend_counts)
 

# 가시화 추가

xs = range(101) # 0 ~ 100 x축 친구수 
ys = [friend_counts[x] for x in xs] # 친구수가 동일한 사람들 수

plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()


  
