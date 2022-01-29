import sys
sys.setrecursionlimit(10**9)


sugar = int(input())

dp = [9999999]*5001

dp[3] = 1
dp[5] = 1

for i in range(6, sugar+1) :
    dp[i] = min(dp[i-3], dp[i-5]) + 1
    
if dp[sugar] >= 9999999 :
    print(-1)
else :
    print(dp[sugar])