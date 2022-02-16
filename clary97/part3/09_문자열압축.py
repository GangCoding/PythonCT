from bz2 import compress


def solution(s):
    answer = len(s)
    
    # 1개의 i부터 압축 단위를 늘려가며 확인
    for i in range(1, (len(s)//2)+1) :
        compressed = ""
        string = s[0:i]
        num = 1
        
        # i 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(i, len(s), i) :
            
            # 이전 상태와 동일하다면 압축 횟수(num) 증가
            if string == s[j:j + i] :
                num += 1
            
            # 다른 문자열이 나왔다면
            else :
                compressed += str(num) + string if num >= 2 else string
                string = s[j:j + i]
                num = 1
                
        # 남아있는 문자열에 대해 처리
        compressed += str(num) + string if num >= 2 else string
        
        answer = min(answer, len(compressed))  # 문자열중 가장 작은것
    
    return answer