# 백준 15686번
import sys
from itertools import combinations # 조합

input = sys.stdin.readline # 오류 나서 바꿈

N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

city = []
chicken = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            city.append((i,j))
        if graph[i][j] == 2:
            chicken.append((i,j))

# 조합 사용? 왠지는 모르겠음...
pick_chicken = list(combinations(chicken, M))

answer = []

for i in pick_chicken: # for문 치킨 좌표
    total = 0
    for j in city: # for문 city 좌표
        Min = 10000
        for k in i: # 최소값 찾기
            dist = abs(k[0]-j[0])+abs(k[1]-j[1])
            Min = min(Min,dist)
        
        total += Min

    answer.append(total)

print(min(answer))