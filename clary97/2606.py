computer = int(input())
con_computer = int(input())


graph = [[]*computer for _ in range(computer+1)]
for _ in range(con_computer) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
count = 0
visited = [0]*(computer+1)

def dfs(start) :
    global count
    visited[start] = 1
    
    for i in graph[start] :
        if visited[i] == 0 :
            dfs(i)
            count += 1            
               

dfs(1)

print(count)