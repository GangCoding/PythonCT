# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 19:01:48 2022

@author: qwuni
"""

n,m = map(int, input().split())  # n=5 , m=3
gongs=[]  # 1 3 2 3 2  # 고으이 무게 1 5 4 3 2 4 5 2
cnt =0  # 두 사람이 공을 고르는 경우의 수 25 = 7+ 10 +4 +4  
#/8=1(무게1의개수)*4 +2(무게2의 개수)*2 
for i in range(n):
    gongs.append(int(input()))        
for i in range(1,m):  # 1 > 2
    n -= gongs.count(i)
    cnt += gongs.count(i)*n  
    # cnt = 1*(5-1-gongs.count(0)) 2* (5-2-1)
print(cnt)    