n = int(input())

mo = list(map(int, input().split()))

mo.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in mo:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)



