computer = int(input()) # 컴퓨터의 개수
couple = int(input()) # 쌍의 수

graph =[[0]*(computer+1) for _ in range(computer+1)]
for i in range(couple):
  X, Y = map(int, input().split())
  graph[X][Y] = 1
  graph[Y][X] = 1

visited = [False] * (computer+1)
count = 0

def dfs(graph, v, visited):
  visited[v] = True
  for i in range(computer+1):
    if visited[i] == 0 and graph[v][i] == True:
      dfs(graph, i, visited)

dfs(graph, 1, visited)
for i in range(computer+1):
  if(visited[i] == 1):
    count += 1
print(count-1)
