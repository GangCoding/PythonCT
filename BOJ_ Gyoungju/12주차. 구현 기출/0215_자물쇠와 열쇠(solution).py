# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 13:42:40 2022

@author: qwuni
"""

## 자물쇠와 열쇠 (구현)

# solution1
def match(arr, key, rot, row, column):  # 자물쇠 값과 열쇠 값을 매칭
    n = len(key)  # 열쇠의 크기
    for i in range(n):
        for j in range(n):
            if rot == 0:  # 회전이 없는 경우
                arr[row+i][column+j] += key[i][j]
            elif rot == 1:   # 시계방향으로 90도 회전
                arr[row + i][column + j] += key[n-1 -j][i]
            elif rot == 2:
                arr[row + i][column + j] += key[n-1 -i][n-1 -j]
            else:
                arr[row + i][column + j] += key[j][n-1 -i]

def check(arr, offset, n):   # 자물쇠 값이 모두 1이면 True 반환
    for i in range(n):
        for j in range(n):
            if arr[offset + i][offset + j] != 1:
                return False
    return True

def solution(key, lock):
    offset = len(key)-1   # 자물쇠의 위치  = 열쇠의 길이에서 1만큼 떨어져야 함
    for row in range(offset + len(lock)):   # 키의 위치 = offset + 자물쇠의 길이
        for column in range(offset + len(lock)):
            for rot in range(4):   # 열쇠 90도 회전 총 4번 필요
                arr = [[0 for _ in range(58)] for _ in range(58)]   # 2차원 배열 형태로 0으로 초기화 : 20+20+20 -2 = 58 (열쇠최대길이 20, 자물쇠 최대길이 20)
                for i in range(len(lock)):   # 자물쇠 복사(offset만큼 떨어진 위치에 복사)
                    for j in range(len(lock)):
                        arr[offset + i][offset + j] = lock[i][j]
                match(arr,key,rot,row,column)
                if check(arr, offset, len(lock)):
                    return True
    return False  







# solution2 (이코테)

# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(a):
    n = len(a)  # 행 길이 계산
    m = len(a[0])  # 열 길이 계산
    result = [[0]*n for _ in range(m)]  # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] =a[i][j]
    return result

# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0] *(n*3) for _ in range(n*3)] 
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    # 4가지 방향에 대해서 확인
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)  # 열쇠 회전
        for x in range(n * 2):
            for y in range(n * 2):
                # 자물쇠에 열쇠를 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(new_lock) == True:
                    return True
                # 자물쇠에서 열쇠를 다시 빼기????
                for i in range(m):
                    for j in range(m):
                         new_lock[x+i][y+j] -= key[i][j]
    return False



























              