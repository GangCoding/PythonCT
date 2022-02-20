from turtle import distance
from itertools import combinations

n, m = map(int, input().split())
graph = []

for i in range(n) :
    graph.append(list(map(int, input().split())))

house = []
chicken = []
result = 9999

for i in range(n) :
    for j in range(n) :
        if graph[i][j] == 1 :
            house.append((i,j))
        elif graph[i][j] == 2 :
            chicken.append((i,j))
            
        
for candidates in combinations(chicken, m) :   ## 치킨집 m개 선택(조합)
    temp = 0     ## 전체 도시의 치킨 거리
    for h in house :    ## 집을 하나씩 접근할 수 있다!
        candidates_len = 9999  
        for k in range(m) :
            candidates_len = min(candidates_len, abs(h[0] - candidates[k][0])+abs(h[1] - candidates[k][1]))
        temp += candidates_len
    result = min(result, temp)
    
print(result)