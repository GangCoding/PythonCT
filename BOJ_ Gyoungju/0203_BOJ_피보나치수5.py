# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 04:31:04 2022

@author: qwuni
"""

# 피보나치수5
***
입력예시
10
출력예시
55
***

n=int(input())

d= [0]*21

d[0]=0
d[1]=1

for i in range(2,n+1):
    d[i]= d[i-1]+d[i-2]
print(d[n])