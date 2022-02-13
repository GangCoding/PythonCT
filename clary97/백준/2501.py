n, k = map(int, input().split())
result = 0
list = []

for i in range(1,n+1) :
    if n % i == 0 :
        list.append(i)
    else :
        continue

if len(list) < k :
    print(result)
else :
    result = list[k-1]
    print(result)