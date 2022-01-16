# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 16:43:04 2022

@author: qwuni
"""

# 1547 공 (시뮬레이션)

m = int(input())
gong = [1, 2, 3]  

for i in range(m):   
    x,y = map(int, input().split()) 
    gong[x-1],gong[y-1] = gong[y-1],gong[x-1]
    
print(gong[0])         
               