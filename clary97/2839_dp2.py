import sys
sys.setrecursionlimit(10**9)


sugar = int(input())

dp = [9999999]*5001

dp[3] = 1
dp[5] = 1

for i in range(6, sugar+1) :
    dp[i] = 9999999
    
    if i-3 >= 0 :
        dp[i] = min(dp[i], dp[i-3]+1)
        
    if i-5 >= 0 :
        dp[i] = min(dp[i], dp[i-5]+1)
    
if dp[sugar] >= 9999999 :
    print(-1)
else :
    print(dp[sugar])