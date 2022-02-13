# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 14:35:19 2022

@author: qwuni
"""

## 곱하기 혹은 더하기 (그리디)
# '더하기' 혹은 '곱하기' 연산자를 넣어 만들어질 수 있는 가장 큰 수 구하기
# 단, 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정
# s : 여러개의 숫자로 구성된 하나의 문자열 s (1<= s의 길이 <= 20)
# 만들어질 수 있는 가장 큰 수 출력
***
입력예시 > 출력예시  
02984 > 576   0 + 2 * 9 * 8 * 4
567 > 210   5 * 6 * 7
5104  > 5*1 + 0 *4 =20   5+1+0*4=24
***

s = input()
result =int(s[0])

for i in range(1,len(s)):  
    if int(s[i]) <= 1 or result <= 1 :     
        result += int(s[i])  
    else:    
        result  *=  int(s[i])    
print(result)        