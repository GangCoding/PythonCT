N = int(input())

d = [0] * 21 # 20보다 작거나 같은 자연수 혹은 0이니깐 그만큼 할당

d[0] = 0 # 0은 0
d[1] = 1 # 1은 1

for i in range(2, N+1):
    d[i] = d[i-2]+d[i-1]

print(d[N])
