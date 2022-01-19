n = int(input())
graph = []

for i in range(n) :
    graph.append(list(map(int, input())))
    
def dfs(x,y) :
    global house
    if x <= -1 or x >=n or y <= -1 or y >= n :
        return False
    global num
    if graph[x][y] == 1 :
        house += 1
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x,y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

count = 0
danji = []
house = 0
for i in range(n) :
    for j in range(n) :
        if dfs(i,j) == True :
            count += 1
            danji.append(house)
            house = 0
        
print(count)
danji.sort()
for k in danji :
    print(k)