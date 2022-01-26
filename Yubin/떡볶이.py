N, M = list(map(int, input().split()))

rice_cake = list(map(int, input().split()))

start = 0
end = max(rice_cake) # end는 max(rice_cake)

while start <= end:
  total = 0
  mid = (start+end) // 2
  
  for i in rice_cake:
    if i > mid:
      total += i - mid
  if total < M:
    end = mid - 1
  else:
    result = mid
    start = mid + 1
print(result)

# 백준의 예산 문제랑 거의 비슷한 맥락
# 대신, i - mid를 해야함, 이진탐색 문제
