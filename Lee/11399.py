N = int(input())

time = list(map(int, input().split()))

# 총 소요 시간 = N*1번 소요시간 + N-1*2번 소요시간 + ... + 1*N번 소요시간
time.sort(reverse=True)

summation = 0

for i in range(0,N):
    summation += time[i] * (i+1)
    
print(summation)
