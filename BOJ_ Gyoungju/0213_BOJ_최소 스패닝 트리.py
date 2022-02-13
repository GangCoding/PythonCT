# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 15:49:38 2022

@author: qwuni
"""

## 최소 스패닝 트리 (최소 신장트리/ 크루스칼 알고리즘) (이코테 10-5.py와 같음)
***
입력예시
3 3
1 2 1
2 3 2
1 3 3
출력예시
3
***

v,e= map(int, input().split())
#a,b,c : 노드 a, 노드 b, 가중치 c

# 특정 원소가 속한 집합을 찾기
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

v,e = map(int, input().split())
parent = [0]*(v+1)  # 부모 테이블 초기화

edges=[]  # 모든 간선을 담을 리스트
result = 0  # 최종 비용(가중치)을 담을 변수

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] =i

# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a,b,weight = map(int, input().split())
    edges.append((weight,a,b)) 

# 간선을 가중치 순으로 정렬
edges.sort()  

for edge in edges:
    weight,a,b = edge
    if  find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += weight
print(result)        
        