# 국어 90점 이상, 영어 80점 초과, 수학 85점 초과, 과학 80점
# 이상일 때 합격 (한 과목이라도 조건에 만족하지 않으면 불합격)

korea, english, math, science = map(int, input().split())
print(korea >= 90 and english > 80 and math > 85 and science >= 80) 
