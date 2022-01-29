# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 20:22:44 2022

@author: qwuni
"""

# 떡볶이 떡 만들기

입력예시
4 6
19 15 10 17

출력예시
15

n,m = map(int, input().split())  # n: 떡의 개수, m : 요청한 떡의 길이
height = list(map(int, input().split()))


# solution
# 이진 탐색을 위한 시작점과 끝점 설정
start=0
end=max(height)

# 이진 탐색 수행(반복적)
result=0
while(start <= end):
    total = 0
    mid = (start+end)//2
    for x in height:
        if x > mid:
            total += x - mid
    if total < m:    # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
        end= mid - 1
    else:            # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
        result = mid   # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result 기록
        start = mid + 1
print(result)        
        




