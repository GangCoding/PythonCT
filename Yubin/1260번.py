from collections import deque
import sys
sys.setrecursionlimit(10000)

N, M, V = map(int, input().split())

graph =[[0]*(N+1) for _ in range(N+1)]
for i in range(M):
  X, Y = map(int, input().split())
  graph[X][Y] = 1
  graph[Y][X] = 1

visited = [False] * (N+1)

def dfs(graph, v, visited):
  visited[v] = True
  print(v, end=' ')
  for i in range(N+1):
    if visited[i] == 0 and graph[v][i] == True:
      dfs(graph, i, visited)
dfs(graph, V, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in range(N+1):
            if visited[i] == 0 and graph[v][i] == True:
                queue.append(i)
                visited[i] = True

print('')
visited = [False] * (N+1)
bfs(graph, V, visited)
