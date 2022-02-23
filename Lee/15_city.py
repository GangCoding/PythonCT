n, m, k, x = map(int, input().split())

x = [x-1]

graph = [[0 for _ in range(n)] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

global count
count = 0

def func(list):
    global count
    global coord

    if count == k:
        if len(coord) != 0:
            for i in coord:
                print(i+1)
        else:
            print(-1)
        return
    else:
        coord = []
        for i in list:
            for j in range(m):
                if graph[i][j] == 1 and j not in list:
                    coord.append(j)
        count += 1
        func(coord)
    
func(x)

