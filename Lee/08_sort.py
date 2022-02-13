a = input()

temp = []
for i in a:
    temp.append(ord(i))

alphabet = []
number = []

for i in temp:
    if i >= 65:
        alphabet.append(chr(i))
    if i < 65:
        number.append(chr(i))

for i in range(len(number)):
    number[i] = int(number[i])

su = str(sum(number))

alphabet = sorted(alphabet)

alphabet.append(su)

for i in alphabet:
    print(i, end='')