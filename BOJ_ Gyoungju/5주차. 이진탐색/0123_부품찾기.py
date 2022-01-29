# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 19:35:48 2022

@author: qwuni
"""

# 부품찾기
# n : 부품개수 / m : 손님이 문의한 부품종류의 개수

입력예시
5
8 3 7 9 2
3
5 7 9

출력예시
no yes yes

n= int(input())
array= list(map(int, input().split()))
m= int(input())
target = list(map(int, input().split()))

array.sort()

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)



for i in range(m):
    if binary_search(array, target[i], 0, n-1) == None:
        print("no", end=' ')
    else:
        print("yes", end= ' ')