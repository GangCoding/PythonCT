sugar = int(input())

answer = -1
for i in range(5):# 0 ~ 4
    if (sugar - i*3)>=0 and (sugar - i*3)%5==0:
        answer = i + (sugar - i*3)//5
        break
    
print(answer)