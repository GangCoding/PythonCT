N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
B = list(map(int, input().split()))

def binary_search(array, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for i in range(len(B)):
    print(binary_search(A, 0, N-1, B[i]))
