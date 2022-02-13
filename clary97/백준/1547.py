m = int(input())

cup = [0, 1, 0, 0]  ## cup[1]에 공이 있음

for i in range(m) :
    a,b = list(map(int, input().split()))
    cup[a], cup[b] = cup[b], cup[a]

if cup[1] == 1 :
    print(1)
elif cup[2] == 1 :
    print(2)
else :
    print(3)