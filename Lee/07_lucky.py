n = input()

half = int(len(n) / 2)

front = n[0:half]

back = n[half:]

list_1 = []
list_2 = []

for i in range(half):
    list_1.append(front[i])
    list_2.append(back[i])

result_1 = 0
result_2 = 0

for i in range(half):
    result_1 += int(list_1[i])
    result_2 += int(list_2[i])

if result_1 == result_2:
    print('LUCKY')
else:
    print('READY')