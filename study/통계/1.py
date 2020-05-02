# 동일한 친구수를 가진 사람들을 모아서 보여줌
# 100명의 친구 4명, 3명의 친구 3명 100:4, 3:3

import collections

num_friend = [100, 40, 30, 54, 25, 3, 100, 100, 100, 3, 3]
friend_counts = collections.Counter(num_friend)
print('friend:', friend_counts)