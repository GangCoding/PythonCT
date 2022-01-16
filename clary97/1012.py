from sys import stdin

t = int(input())
result_list = []

def make_graph(m, n, k) :
    graph = [[0]*m for _ in range(n)]  ## m x n 배열 생성, 0으로 초기화
    
    result = 0   #전체 지렁이 수
    
    for _ in range(k) :  #배추의 총 개수만큼 반복
        x, y = map(int, input().split())
        graph[y][x] = 1  #배추 위치(1로 입력됨), x와 y가 바뀌어야 한다. 아니면 범위를 벗어남!
    return graph
        
def dfs(y, x) :
    if x < 0 or x >= m or y < 0 or y >= n :
        return False
    
    if graph[y][x] == 1 :
        
        graph[y][x] = 0
        
        dfs(y-1, x)
        dfs(y+1, x)
        dfs(y, x-1)
        dfs(y, x+1)
        return True
    return False
    
for _ in range(t) :
    result = 0
    m, n, k = map(int, stdin.readline().split())
    graph = make_graph(m, n, k)
    for i in range(n) :           
        for j in range(m) :       
            if dfs(i,j) == True : # 배추가 심어져있는 경우
                result += 1
    result_list.append(result)

print(*result_list, sep = '\n')