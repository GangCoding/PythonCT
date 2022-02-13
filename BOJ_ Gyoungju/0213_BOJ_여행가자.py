# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 16:33:36 2022

@author: qwuni
"""

## 여행계획
# n : 도시 수 / m : 여행계획에 속한 도시들의 수
***
입력예시
3
3
0 1 0
1 0 1
0 1 0
1 2 3
출력예시
YES
***

n = int(input())
m = int(input())

# 경로 압축 기법 (# 특정 원소가 속한 집합을 찾기)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]   

# 두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b]=a
    else:
        parent[a]=b

parent = [0]*(n+1)  # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1,n+1):
    parent[i]=i

for i in range(1,n+1):
    data = list(map(int, input().split()))
    for j in range(1,len(data)+1):
        if data[j-1] == 1:
            union_parent(parent,i,j)

plan = list(map(int, input().split()))
result=[]

for i in plan:
    result.append(find_parent(parent, i))
print(len(result))
if result.nunique() ==1:
    print('YES')
else:
    print('NO')           
                