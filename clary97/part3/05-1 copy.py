n, m = map(int, input().split())
ball = list(map(int, input().split()))

select = [0] * 11

for x in ball :
    select[x] += 1
    
result = 0

for i in range(1, m+1) :
    n -= select[i]
    result += select[i] * n
    
print(result)