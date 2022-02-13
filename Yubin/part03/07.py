N = input()

a = []

for i in N:
    a.append(i)

half = len(a)//2
right_list = list(map(int, a[half:]))
left_list = list(map(int, a[:half]))

sum1, sum2 = 0

for i in right_list:
    sum1 += i

for i in left_list:
    sum2 += i

if sum1 == sum2:
    print('LUCKY')
else:
    print('READY')
