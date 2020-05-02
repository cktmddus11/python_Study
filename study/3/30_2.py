korean, english, mathematics, science = map(int, input().split())

def get_min_max_score(*arg):
    return min(arg), max(arg)
def get_average(**kwargs):
    sum_s = 0
    for arg in kwargs.values():
        sum_s = sum_s + arg
    # for문 보다 sum(kwargs.values()) 가 더 간단
    return sum_s/len(kwargs)


min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english,
                            mathematics=mathematics, science=science)

print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))



min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))      