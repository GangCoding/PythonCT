sugar = int(input())

answer = -1 # 초기 답안은 -1 (불가능)

for i in range(5):# 3kg 을 몇 번 사용할 것인지(i)
    sugar_remain = sugar - 3*i #  3kg를 처리하고 남은 양(5kg만 써서 처리해야 함)
    if sugar_remain>=0 and sugar_remain%5==0: # 남은 양이 5kg만 써서 처리 가능한가?
        answer = i + sugar_remain//5 # 답 = (3kg 사용횟수) + (5kg 사용횟수)
        break
    
print(answer)