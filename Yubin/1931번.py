# 코드 참고, 정렬은 했는데 그 뒤로 알고리즘 생각이 안 나서...

N = int(input())

room = []
for i in range(N):
  room.append(list(map(int, input().split())))

room.sort(key=lambda x : x[0]) # 앞 기준으로 정렬
room.sort(key=lambda x : x[1]) # 뒤 기준으로 정렬 또 다시

last = 0 # 마지막 시간 정해놓고
count = 0

for i,j in room: 
  if i >= last:
    count += 1 # 카운트
    last = j # 같다

print(count)
