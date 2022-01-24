# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 14:35:35 2022

@author: qwuni
"""

## 회의실배정
# n = 회의수
# 회의 시작시간 끝나는 시간
# 최대 사용할 수 있는 회의의 최대 개수?

입력예시 
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14

출력예시
4

# solution
n = int(input())
array=[]
for i in range(n):
    input_data = input().split()
    array.append((int(input_data[0]), int(input_data[1])) )

# 회의 끝나는 시간을 기준으로 오름차순으로 정렬 -> 시작시간을 기준으로 오름차순
# 먼저 끝나는 시간을 기준으로 정렬해야 시간간격 텀이 짧은 시간이 선택된다.    
array = sorted(array, key= lambda time: (time[1],time[0]))   

last = 0  # 회의의 마지막 시간을 저장할 변수
count = 0  # 회의 개수를 저장할 변수

for i,j in array:
    if i >= last:  # 시작시간이 회의의 마지막 시간보다 크거나 같을 경우
        count += 1
        last = j
print(count)        
