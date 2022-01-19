from collections import deque

M, N = map(int, input().split())

graph = []
for i in range(N):
  graph.append(list(map(int,input().split())))

queue = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#토마토 위치 저장
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append([i,j])

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            Nx = x + dx[i]
            Ny = y + dy[i]
            if 0 <= Nx < N and 0 <= Ny < M and graph[Nx][Ny] == 0:
                graph[Nx][Ny] = graph[x][y] + 1
                queue.append([Nx, Ny])

bfs()
check = False
result = -2
for i in graph:
    for j in i:
      # 다 찾아봤는데 토마토를 익히지 못했다면
        if j == 0:
            check = True # check = True
        # 다 익힌 거면 최댓값이 정답이도록
        result = max(result, j)

if check == True: # 못 익을 때
    print(-1)
elif result == -1: # 모두 익을 때
    print(0)
else: # 며칠 걸리는지
    print(result -1)

