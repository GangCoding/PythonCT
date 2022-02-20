N = int(input())
K = int(input())

array = [[0] * N for _ in range(N)]
apple = 1

for _ in range(K):
    a, b = map(int, input().split())
    array[a-1][b-1] = apple

L = int(input())
snake = []

for _ in range(L):
    time, direction = input().split()
    snake.append((int(time), direction))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn_direction(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4   # 왼쪽
    else:
        direction = (direction + 1) % 4   # 오른쪽
    return direction

x, y = 0, 0
array[x][y] = 2
direction = 0
snake_idx = 0
count = 0
q = [(x, y)]  # 뱀 길이

while True:
    nx, ny = x + dx[direction], y + dy[direction]
    if 0 <= nx < N and 0 <= ny < N and array[nx][ny] != 2:
        # 사과가 없을 경우
        if array[nx][ny] == 0:
            array[nx][ny] = 2
            q.append((nx, ny))
            px, py = q.pop(0)
            array[px][py] = 0
        if array[nx][ny] == apple:
            array[nx][ny] = 2
            q.append((nx, ny))
    else:
        count += 1
        break
    count += 1
    x, y = nx, ny

    # 시간이 지나면
    if snake_idx < L and count == snake[snake_idx][0]:
        direction = turn_direction(direction, snake[snake_idx][1])
        snake_idx += 1

print(count)