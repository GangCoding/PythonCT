#1920

# list를 사용하면 시간초과, set 사용하니깐 오류 벗어남
# 탐색을 하는 용도로만 쓰기 때문에 set이 가장 적합한 자료구조

N = int(input())

list1 = set(map(int, input().split())) # set 사용

M = int(input())

list2 = list(map(int, input().split()))

for i in list2:
  if (i in list1):
    print(1)
  else:
    print(0)
