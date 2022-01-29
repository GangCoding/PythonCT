# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 15:52:18 2022

@author: qwuni
"""

## 수찾기
입력예시
5
4 1 5 2 3
5
1 3 7 9 5

출력예시
1
1
0
0
1

n=int(input())
array =list(map(int, input().split()))
m=int(input())
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
        print(0)
    else:
        print(1)    
