n, m = map(int, input().split())


graph = [[] for i in range(n)]

for i in range(n):
    l = list(map(int, input().split()))
    graph[i] = l

# 집의 좌표와 치킨 집의 좌표 리스트 생성

house = []
chicken = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i, j))
        if graph[i][j] == 2:
            chicken.append((i, j))

# C(# of chicken, M) 의 경우의 수를 list로 출력하는 함수
from itertools import combinations

combination_result = list(combinations(chicken, m))

distance_result = []

if m == 1:
    temp_sum = []
    combination_result = chicken
    for i in range(len(combination_result)):
        temp = []
        for j in house:
            temp.append(
                abs(combination_result[i][0] - j[0]) + abs(combination_result[i][1] - j[1])
            )
        temp_sum.append(sum(temp))
    print(min(temp_sum))
    
else:
    temp_sum = []
    combination_result = list(combinations(chicken, m))
    for i in range(len(combination_result)):
        distance_one = []
        for j in house:
            temp = []
            for k in range(len(combination_result[i])):
                temp.append(
                    abs(combination_result[i][k][0] - j[0]) + abs(combination_result[i][k][1] - j[1])
                )
            distance_one.append(min(temp))
        temp_sum.append(sum(distance_one))
    print(min(temp_sum))


# 치킨거리를 계산하는 함수
# 치킨거리(h1) : min{(|h1-c1|,|h1'-c1'|), ... ,(|h1-cn|,|h1'-cn'|)}
# 치킨거리(hn) : min{(|hn-c1|,|hn'-c1'|), ... ,(|hn-cn|,|hn'-cn'|)}


    

