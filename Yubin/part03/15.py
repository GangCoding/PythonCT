from collections import deque

N, M, K, X = list(map(int, input().split()))

visited = [False] * (N+1)

graph =[[] for _ in range(N+1)]

answer = []

for i in range(M):
    X, Y = map(int, input().split())
    graph[X].append(Y)

print(graph)

def bfs(graph, start, visited):
    queue=deque([start])

    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if answer[i] == -1: # 방문하지 않았다면
                answer[i]=answer[v]+1
                queue.append(i)

bfs(graph, X, visited)
answer.sort() # 오름차순으로 

if answer.count(K):
    for i in range(1, N+1):
        if answer[i] == K:
            print(i)
else:
    print(-1)