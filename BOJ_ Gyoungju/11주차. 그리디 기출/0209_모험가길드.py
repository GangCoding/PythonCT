# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 13:50:52 2022

@author: qwuni
"""

# 모험가 길드 (그리디)
# n : 모험가 인원 / 각각의 공포도
# 공포도가 x인 모험가는 반드시 x명 이상으로 구성한 모험가 그룹에 참여해야 여행 가능
***
입력예시
5
2 3 1 2 2 
출력예시
여행을 떠날 수 있는 그룹 수의 최댓값 2
***

n = int(input())
fear =[]
for i in range(n):
    fear.append(int(input()))
print(fear)

fear.sort(reverse=True)

group = 0

for x in fear:   # 3 > 2 > 2 > 2 > 1
    if x <= len(fear):  # 3 <= 5   > 2 <= 2   
        fear = fear[x:]   # fear = fear[3:] =[2,1]  > fear = fear[2:] =0
        group += 1  # group =1 > group =2
    else:  # 2 > 0
        break
print(group)    