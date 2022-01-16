from collections import deque
import sys
sys.setrecursionlimit(10**9)

n, m, v = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m) :
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
def dfs(graph, v, visited) :
    visited[v] = True
    print(v, end=' ')
    
    for i in range(n+1) :
        if visited[i] == 0 and graph[v][i] == True:
            dfs(graph, i, visited)
            
visited = [False] * (n+1)

dfs(graph, v, visited)

print('')

def bfs(graph, start, visited) :
    queue = deque([start])
    
    visited[start] = True
    while queue :
        v = queue.popleft()
        print(v, end=' ')
        
        for i in range(n+1) :
            if visited[i] == 0 and graph[v][i] == True:
                queue.append(i)
                visited[i] = True
                
visited = [False] * (n+1)

bfs(graph, v, visited)