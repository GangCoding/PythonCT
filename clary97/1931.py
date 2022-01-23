n = int(input())

meeting = []
for i in range(n) :
    start, fin = map(int, input().split())
    meeting.append([start, fin])
    
meeting.sort(key = lambda x:(x[1], x[0]))  # 회의 시작 시간으로 오름차순 정렬 이후 끝나는 시간 기준으로 오름차순 정렬

end = 0  # 회의가 끝나는 시간을 저장
cnt = 0  # 회의의 개수를 저장

for i,j in meeting :
    if i >= end :  # 시작시간이 회의 끝나는 시간보다 크거나 같을 경우
        cnt += 1
        end = j
        
print(cnt)