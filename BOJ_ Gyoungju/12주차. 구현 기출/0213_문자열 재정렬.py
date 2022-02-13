# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 19:55:36 2022

@author: qwuni
"""


import re

string = input()
numbers = re.findall('\d', string)  # 숫자분리
alphas = re.findall('[A-Z]', string)  # 문자분리

alphas_sort =sorted(alphas, reverse=False)   # 알파벳 오름차수 ㄴ정렬

numbers_int=list(map(int, numbers))  # 숫자 int로 바꾸기

all_sum = 0

for i in numbers_int:   # 숫자 다 합한 값을 all_sum에 저장
    all_sum += i
print(all_sum)    

result =  "".join(alphas_sort)  # 공백 없이 문자열 결합

print(result+str(all_sum))  # 결합한 문자열과 all_sum 값을 결합해 출력
