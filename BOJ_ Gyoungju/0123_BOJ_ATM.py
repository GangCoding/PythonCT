# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 13:55:16 2022

@author: qwuni
"""

# ATM
# n = 줄을 서 있는 사람의 수 / pi = 각 사람이 돈을 인출하는데 걸리는 시간

***
입력예시
5
3 1 4 3 2

출력예시
32
***

n = int(input())   # n=5
i_time = list(map(int, input().split()))   # 3 1 4 3 2

i_time.sort()
result=[0] *n

for i in range(n):
    result[i] = sum(i_time[:i+1])
print(sum(result))    




# error : IndexError: list assignment index out of range
문제점 : 처음에 result=[] 으로 빈리스트를 생성했는데, 빈 리스트에 i번째 인덱스에 값을 넣으려고 하니,
         빈 리스트인데 i번째 인덱스가 어디있니? 라는 문제가 생김
해결방법 : 1) append() 나 insert() 함수 사용
          2) 리스트 자체를 초기화해서 사용할 리스트 갯수를 미리 잡아놓는다.
             ex)  result=[0] * 5      

# sum & slicing    
a= [1,2,3]
print(sum(a[:2]))