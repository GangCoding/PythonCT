money = int(input())

money_types = [300, 60, 10]
counts = []
for mon in money_types :
    counts.append(money // mon)
    money %= mon

if money == 0:
    print(f"{counts[0]} {counts[1]} {counts[2]}")
else:
    print(-1)