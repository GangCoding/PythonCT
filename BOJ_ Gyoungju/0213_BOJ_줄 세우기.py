# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 16:34:35 2022

@author: qwuni
"""

## 줄 세우기 (위상정렬 알고리즘)
***
입력예시
3 2
1 3
2 3
출력예시
1 2 3
***

from collections import deque

n,m = map(int, input().split())
indegree = [0] *(n+1)  # 모든 노드에 대한 진입차수는 0으로 초기화
graph = [[] for i in range(n+1)]  # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화

# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)  # 학생 a가 학생 b 앞에 서야 한다.
    indegree[b] += 1  # 진입차수 1 증가

# 위상 정렬 함수
def topology_sort():
    result = []  # 알고리즘 수행 결과를 담을 리스트
    q = deque()  # 큐 기능을 위한 deque 라이브러리 사용
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()  # 큐에서 원소 꺼내기
        result.append(now)
        for i in graph[now]:  # 해당 언소와 연결된 노드들의 진입차수에서 1빼기
            indegree[i] -= 1
            if indegree[i] == 0: # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                q.append(i)
    for i in result:
        print(i, end=' ')

topology_sort()            
