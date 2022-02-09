T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    dist = [ [0]*(N+2) for _ in range(N+2) ] # (N+2)x(N+2)의 0으로 채워진 2차원 리스트]
    pos = [ ] # 
    # dist[u][v] : u->v 로 갈 수 있으면 1, 아니면 0

    for i in range(N+2):
        x,y = list(map(int, input().split()))
        pos.append((x,y))
    
    # pos[i] : i번째 좌표 (x,y)

    # dist 초기 설정
    for i in range(N+2):
        for j in range(N+2):
            if abs(pos[i][0] - pos[j][0]) + abs(pos[i][1] - pos[j][1]) <= 1000:
                dist[i][j] = 1
    
    # Floyd 구조
    for k in range(N+2):
        for i in range(N+2):
            for j in range(N+2):
                if dist[i][k] == 1 and dist[k][j] == 1:
                    dist[i][j] = 1
    
    if dist[0][N+1] == 1:
        print("happy")
    else:
        print("sad")