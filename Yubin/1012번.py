def dfs(x, y):
  if x <= -1 or x >= M or y <= -1 or y>= N:
    return False
  if field[x][y] == 1:
    field[x][y] = 0
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
  return False

T = int(input())
for i in range(T):
  M, N, K = map(int, input().split())

  field =[[0]*(N) for _ in range(M)]
  for i in range(K):
    X, Y = map(int, input().split())
    field[X][Y] = 1
  
  result = 0
  for i in range(M):
    for j in range(N):
      if dfs(i, j) == True:
        result += 1
  print(result)
