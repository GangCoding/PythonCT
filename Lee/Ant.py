N = int(input())
food = list(map(int, input().split()))

answer = []

for i in range(len(food)):
    temp = food[i+2:]
    if len(temp) >= 1:
        k = max(temp)
        answer.append(food[i] + k)


print(max(answer))