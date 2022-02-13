n, m = map(int, input().split())
ball = list(map(int, input().split()))

select = []

for i in range(len(ball)) :
    for j in range(len(ball)) :
        if ball[i] == ball[j] :
            pass
        else :
            select.append([ball[i],ball[j]])
            

print(int(len(select)/2))