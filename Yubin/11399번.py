#11399

N = int(input())

money = list(map(int, input().split()))
money = sorted(money)

atm = []
count = 0

for i in money:
  count += i
  atm.append(count)

print(sum(atm))
