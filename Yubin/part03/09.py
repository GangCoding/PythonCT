def solution(s):
    length = []

    if len(s) == 1: # 1이면 1을 리턴
        return 1

    for i in range(1, len(s)//2+1): # for문 돌리기
        result = ''
        count = 1 # 1로 초기화
        compare = s[:i] # 자를 곳까지 저장한다.

        for j in range(i, len(s), i): # for문에서 고생했는데 그만큼 뛰어넘으면서 for문 돌림
            if compare == s[j:i+j]: # i만큼이면 더함.
                count += 1
            else:
                if count != 1:
                    result = result + str(count)+ compare
                else:
                    result = result + compare
                compare = s[j:j+i]
                count = 1 # 1로 초기화
        if count != 1:
            result = result + str(count) + compare
        else:
            result = result + compare
        
        result.append(len(result))
    return min(length) # 최소값을 리턴함