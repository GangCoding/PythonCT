# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 19:36:05 2022

@author: qwuni
"""

n = int(input())  # str
n = str(n)

x = len(n)//2  # 점수를 반으로 나눠줌    

left=0
right=0

for i in range(x):
    left += int(n[:int(x)][i])   # 각 자릿수 int형으로 바꿔서 더하기
    right += int(n[int(x):][i])
    
if left == right:
        print("LUCKY")
else:
    print("READY")    
    
    
    
    
#print(len(n)//2)
#print(n[:int(x)][0])
#type(n[:int(x)][0])     
