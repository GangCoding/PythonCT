import sys
sys.setrecursionlimit(10**9)

n = int(input())
A = list(map(int, input().split()))
A.sort()

m = int(input())
x = list(map(int, input().split()))

def binary_search(array, target, start, end) :
    while start <= end :
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target :
            return mid
        elif array[mid] > target :
            end = mid - 1
        else :
            start = mid + 1 
    return None

for i in x :
    result = binary_search(A, i, 0, n-1)
    
    if result == None :
        print("0")
    else :
        print("1")