
N, M = map(int, input().split())

rice_cake = list(map(int, input().split()))
rice_cake.sort()

h_list = []

## M >= 1 이므로 0<= height < max(rice_cake(i))
for i in range(max(rice_cake)):
    remainder = []
    height = i
    for j in range(N):
        if rice_cake[j] > height:
            remainder.append(rice_cake[j] - height)
        if rice_cake[j] <= height:
            remainder.append(0)
    if sum(remainder) == M:
        h_list.append(height)
    else:
        print('wrong')

print(max(h_list))

