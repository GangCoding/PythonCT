s = input()

temp = []

for i in range(len(s)):
    temp.append(int(s[i]))

result = 1

for i in temp:
    if i == 0:
        pass
    else:
        result = result * i


print(result)