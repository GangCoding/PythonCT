# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 19:01:48 2022

@author: qwuni
"""

n,m = map(int, input().split())  # n=5 , m=3
gongs=[]  # 1 3 2 3 2  # 공의 무게 1 5 4 3 2 4 5 2
cnt =0  # 두 사람이 공을 고르는 경우의 수 25 = 7+ 10 +4 +4  

for i in range(n):
    gongs.append(int(input()))        
for i in range(1,m):  # 1 > 2
    n -= gongs.count(i)
    cnt += gongs.count(i)*n  
print(cnt)    
