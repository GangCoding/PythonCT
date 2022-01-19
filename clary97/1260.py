from collections import deque
import sys
sys.setrecursionlimit(10**9)

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
# 정렬을 단순하게 정렬만 하면 안되고, 차례대로 모두 정렬될 수 있도록!
for i in range(1, n+1) :
    graph[i].sort()

def dfs(graph, v, visited) :
    visited[v] = True
    print(v, end=' ')
    
    for i in graph[v] :
        if not visited[i] :
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
        
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True
                
visited = [False] * (n+1)

bfs(graph, v, visited)