n = int(input())   # n은 지역의 수
local = list(map(int, input().split()))   # 지역별 필요한 예산
m = int(input())   # m은 예산 총액

start = 0
end = max(local)

def binary_search(array, start, end) :
    while start < end :
        mid = (start + end+1) // 2
        total = 0
    
        for x in array :
            if x > mid :  # 중간값보다 배열의 값이 크면
                total += mid   # 중간값을 더함
            else :        # 중간값보다 배열의 값이 작거나 같으면
                total += x     # 배열의 값을 더함
        if total <= m :   # 모두 더한 합이 예산 총액보다 작거나 같은 경우
            start = mid  # 상한값 조정을 위해 start를 중간값보다 크게 잡음
        else :            # 모두 더한 합이 예산 총액보다 큰 경우
            end = mid - 1    # 상한값을 작게 만들어야 하므로 end를 중간값보다 작게 잡음
        
        # start값이 end값보다 작은 경우에만 while문이 돌아가므로 start와 end 범위를 줄이다 보면 mid가 결정됨
    return end

result = binary_search(local, start, end)

print(result)