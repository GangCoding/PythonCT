import re

S = input()

# a = []

# for i in S:
#     a.append(i)
sum = 0
numbers = int(''.join(list(filter(str.isdigit, S))))
numbers = list(map(int, str(numbers)))
string = sorted(list(filter(str.isalpha, S)))

for i in numbers:
    sum += i

result = ''.join(i for i in string)

print(result+str(sum))

