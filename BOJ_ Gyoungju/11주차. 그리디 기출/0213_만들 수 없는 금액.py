# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 17:00:47 2022

@author: qwuni
"""

## 만들 수 없는 금액 (그리디)
# n개 동전을 이용하여 만들 수 "없는" 양의 정수 금액 중 "최솟값" 출력
***
입력예시
5
3 2 1 1 9
출력예시
8
***

n = int(input())
coin_type=[]

for i in range(n):
    coin_type.append(int(input()))

coin_type.sort()

min_value = 1  # 만들 수 없는 양의 정수 금액 중 최솟값

for coin in coin_type:
    if coin > min_value:  # 동전의 값이 최솟값 1보다 클 경우
        break
    min_value += coin
print(min_value)    