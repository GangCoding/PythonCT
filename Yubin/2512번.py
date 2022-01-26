N = int(input())
number = list(map(int, input().split()))
M = int(input())

start = 0 # 0으로 두고
end = max(number) # 굳이 if문 비교 없이 end를 max로 둠 

while start <= end:
  mid = (start+end) // 2

  total = 0
  for i in number:
    total += min(mid, i) # mid랑 i 중 더 나은 값

  if total > M:
    end = mid - 1
  else:
    start = mid + 1
print(end)
