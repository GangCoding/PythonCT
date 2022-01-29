# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 16:08:28 2022

@author: qwuni
"""
## 예산
# n: 지방의 수 /  각 지방의 예산요청 / m : 총 예산

입력예시&출력예시
4
120 110 140 150
485

> 127

5
70 80 30 40 100
450

> 100

n = int(input())
array = list(map(int, input().split()))
m = int(input())

start=0
end= max(array)  # 150

result=0
while(start<=end):   
    total=0  #  예산 총합
    mid = (start+end)//2  # mid = (0+150)//2=75
    for x in array:  # 120 > 110 > 140 >150
        if x > mid:  # 120 > 75
            total += mid
        else:
            total += x
    if total < m:
        start = mid+1
        result = mid
    else:
        end= mid-1
print(result)        