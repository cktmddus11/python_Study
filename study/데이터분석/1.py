import pandas as pd

df = pd.read_csv('C:\\Users\\Cha\\Downloads\\fifa-2018-match-statistics\\FIFA 2018 Statistics.csv')

#print(df)
print(type(df)) # pandas.core.frame.DataFrame
# DataFrame : columns 측 항목들과 index 즉 색인으로 구성됨

#print(df.columns) # 열이름
print(df.columns[1]) # team

print(df.index) # RangeIndex(start=0, stop=128, step=1)

print(df[:3])
# df.head() 위의 4개 출력
# df.tail() 아래의 4개 출력

# print(df['Team'])
print(df['Goal Scored'].sum()) # 총 몇 골
print(df['Goal Scored'].mean()) # 평균 골 
print(df['Goal Scored'].std()) # 표준편차

#print(df.set_index('Team').loc['Korea Republic'].mean())

# 국가별 스탯 정리
team_list = df.set_index('Team').index
#print(team_list)

team = [] # 팀 저장할 빈 리스트 생성
for i in team_list: # 추출한 팀 리스트 요소들을 i에 대입
    if i not in team:  # 대입한 팀 리스트가 새로 만든 팀리스트에 없으면 
        team.append(i) # 없는 팀만 새로 만든 팀 리스트에 추가

#print(team)

# 나리이름별로 스탯 정리
team_summary = {}  # 딕셔너리 자료형으로 만듦
for i in range(len(team)): # 팀 개수만큼
    # 데이터 접근을 위해 key를 나라이름 
    team_summary[team[i]] = df.set_index('Team').loc[team[i]].mean()

print(team_summary['Korea Republic'][13]) # 14번쨰 항목 파울 많이

# Fouls committed 데이터만 모아서 가장 파울을 많이 한 나라를 찾기
fouls = {}
goals = {}
possession = {}
distance = {}
yellow_and_red = {}
pass_accuracy = {}

for i in range(len(team)):
        fouls[team[i]] = team_summary[team[i]][13]
        goals[team[i]] = team_summary[team[i]][0]
        possession[team[i]] = team_summary[team[i]][1]
        pass_accuracy[team[i]] = team_summary[team[i]][9]    
        distance[team[i]] = team_summary[team[i]][11]
        yellow_and_red[team[i]] = team_summary[team[i]][15]

#print(fouls)
print('파울을 가장 많이 한 나라 : ',max(fouls, key=fouls.get))   # 가증큰값을 찾고 max에 접근하는 key값을 돌려줌?
print('가장 골 많이 넣은 나라 : ', max(goals, key=goals.get))     
print('가장 점유율 높은 나라 : ', max(possession, key=possession.get))
print('가장 패스 정확도 높은 나라 : ', max(pass_accuracy, key=pass_accuracy.get))
print('가장 뛴거리가 많은 나라 : ', max(distance, key=distance.get))
print('가장 경고 & 퇴장 많이 받은 나라 : ', max(yellow_and_red, key=yellow_and_red.get))
# print('내용 : {}'.format())


# 골은 +2, 점유율은 +0.1, 패스정확도는 +0.15, 뛴거리 0.005, 경고 및 퇴장 -1 가중치를 
# 부여해서 가장 높은 나라를 뽑음 

score = {}
for i in range(len(team)):
        score[team[i]] = team_summary[team[i]][0]*2 + team_summary[team[i]][1]*0.1 \
                + team_summary[team[i]][9]*0.15 \
                        + team_summary[team[i]][11] *0.005 - team_summary[team[i]][15]


#print(score)                         
print('가장 아름다운 축구를 한 나라 : {}'.format(max(score, key=score.get)))
print('가장 더러운 축구를 한 나라 : {}'.format(min(score, key=score.get)))