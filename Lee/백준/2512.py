N = int(input())
money = list(map(int, input().split()))
maximum = int(input())

start = 0
end = max(money)

    
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in money:
        if i <= mid:
            total += i
        else:
            total += mid
    if total <= maximum:         
        start = mid + 1
    else:
        end = mid - 1
print(end)
    
