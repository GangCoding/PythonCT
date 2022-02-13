money = int(input())
money = 1000-money
count = 0

money_types = [500, 100, 50, 10, 5, 1]

for mon in money_types :
    count += money // mon
    money %= mon
    
print(count)