n = int(input())

array = []
for i in range(n):
    x = input().split()
    array.append([x[0],x[1]])

array.sort(key=lambda x: (x[1], x[0]))

for k in array:
    print(k[0], end=' ')