n, m = map(int, input().split())
array = list(map(int, input().split()))

array.sort()

start = 0
end = max(array)

def binary_search(array, start, end) :
    while start < end : # 같아지면 루프 종료
        mid = (start + end + 1) // 2
        
        result = 0
        for i in range(len(array)) :  # for i in range 는 i에 값이 들어감(2, 6, 5, 3)
            if (array[i] - mid) > 0 :
                result += (array[i] - mid)
          
        if result >= m :
            start = mid
        else:
            end = mid - 1
    return start # return end 를 해도 같음.

h = binary_search(array, start, end)
print(h) 