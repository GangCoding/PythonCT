# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 14:08:23 2022

@author: qwuni
"""

# 2501 약수구하기 (완전탐색)

n,k = map(int, input().split())  
output=[]

for i in range(1,n+1): 
    if n % i == 0:   
        output.append(i)  
      
if len(output) < k:
    print(0)
else:
    print(output[k-1])     
        