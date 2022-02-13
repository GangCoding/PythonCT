import sys

input = sys.stdin.readline

INF = int(1e9)

T = int(input())

for _ in range(T):
    n = int(input())
    graph = []
    for _ in range(n + 2):
        graph.append(list(map(int, input().split())))
    dp = [[INF] * (n + 2) for _ in range(n + 2)]

    for i in range(n + 2):
        for j in range(n + 2):
            if i == j:
                continue
            if abs(graph[i][0] - graph[j][0]) + abs(graph[i][1] - graph[j][1]) <= 1000:
                dp[i][j] = 1
    
    for k in range(n + 2):
        for i in range(n + 2):
            for j in range(n + 2):
                if dp[i][j] > dp[i][k] + dp[k][j]:
                    dp[i][j] = dp[i][k] + dp[k][j] 
    
    
    if 0 <= dp[0][n+1] < INF:
        print('happy')
    else:
        print('sad')