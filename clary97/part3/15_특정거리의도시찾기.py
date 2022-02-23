from collections import deque
import sys
sys.setrecursionlimit(10**9)


n, m, k, x = map(int, input().split())
graph = [[] for _ in range(1 + n)]

for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    
distance = [-1] * (n+1)
distance[x] = 0
    
## 기본 bfs 코드 https://heytech.tistory.com/56 

# BFS 메서드 정의
def bfs (graph, node):
    # 큐 구현을 위한 deque 라이브러리 활용
    queue = deque([node])
    
    # 큐가 완전히 빌 때까지 반복
    while queue:           
        # 큐에 삽입된 순서대로 노드 하나 꺼내기
        v = queue.popleft()
            
        # 현재 처리 중인 노드에서 방문하지 않은 인접 노드를 모두 큐에 삽입
        for next in graph[v]:
            if distance[next] == -1 :  # 방문하지 않은 도시인 경우
                distance[next] = distance[v] +1   # 최단거리 갱신, 현재 도시와 출발 도시사이 거리 +1
                queue.append(next)
              

bfs(graph, x)

answer = []
for i in range(1, n+1) :
    if distance[i] == k :
        answer.append(i)
        
answer = sorted(answer)

if len(answer) == 0 :
    print(-1)
else :
    for i in answer :
        print(i)