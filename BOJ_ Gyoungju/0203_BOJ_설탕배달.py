# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 04:40:37 2022

@author: qwuni
"""

# 설탕 배달
***
입력예시 > 출력예시
18 > 4
4 > -1
***
m = int(input())

d = [5001] * (m+1)
d[0]=0
array=[3,5]

for i in range(2):
    for j in range(array[i], m+1):
        if d[j-array[i]] != 5001:
            d[j] = min(d[j], d[j-array[i]] + 1)
if d[m] == 5001:
    print(-1)
else:
    print(d[m])    
