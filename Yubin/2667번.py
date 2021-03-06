from collections import deque

N = int(input())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

result = [] # 결과

def bfs(graph,x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    count = 1 # 0으로 바꿔주니깐 count 1부터 시작
    while queue:
        x, y = queue.popleft()
        graph[x][y] = 0 # 0으로 바꿔주기
        for i in range(4):
            Nx = x + dx[i]
            Ny = y + dy[i]

            if Nx < 0 or Ny < 0 or Nx >= N or Ny >= N: # 벗어나면 다음
                continue
            if graph[Nx][Ny] == 1: 
                graph[Nx][Ny] = 0
                queue.append((Nx, Ny))
                count += 1
    return count # count를 리턴함

for i in range(N):
    for j in range(N): # NxN이니깐 
        if graph[i][j] == 1: # 1이면 
            count = bfs(graph, i, j) 
            result.append(count) # result에 차례대로 

result.sort() # 정렬해서 보여주기 오름차순으로

print(len(result)) 
for k in result:
    print(k)
