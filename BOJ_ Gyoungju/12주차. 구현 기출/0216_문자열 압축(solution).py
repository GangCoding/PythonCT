# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 21:37:16 2022

@author: qwuni
"""
# solution1
def solution(s):
    # 길이가 1인 경우
    if len(s) == 1:
        return 1
    # 변수 초기화
    result =""
    length = []
    cnt = 1  # 해당 문자열 압축되는 횟수 ex) 2abcdabcd에서 "2"
    # abcdabcd abcdabcd  => 2abcdabcd (전체 문자열 개수의 절반인 8만큼 압축)
    for i in range(1, len(s)//2 + 1): # 단위  # 문자열 한 개씩 압축을 했을 때 부터 전체 문자열 개수의 절반까지 압축했을 때
        cnt = 1
        temp_str =s[:i]  # 압축되는 문자열
        for j in range(i, len(s), i):
            if temp_str == s[j:j+i]:  # 현재 : 현재 + 단위
                cnt += 1
            else:
                if cnt == 1:
                    cnt =""
                result += str(cnt) + temp_str
                cnt = 1
                temp_str = s[j:j+i]
        if cnt == 1:
            cnt =""                
        result += str(cnt) + temp_str
        length.append(len(result))
        result =""
    print(length)        
    return min(length)


# solution2
def solution(s):
    answer =10000
    for n in range(1, len(s)//2 +2 ):  # s의 길이가 1인경우 고려하기 위해 +2
        result = ''
        cnt =1
        temp_str =s[:n]  # 단위문자열 초기화
        for i in range(n, len(s)+n, n):
            if temp_str == s[i : i+n]:
                cnt += 1
            else:
                if cnt==1:
                    result +=temp_str
                else:
                    result += str(cnt)+ temp_str
                temp_str = s[i: i+n]
                cnt =1
        answer = min(answer,len(result)) 
    return answer               
    




























