s = input()

first = int(s[0])

for i in range(1, len(s)) :
    num = int(s[0])
    
    if num <= 1 or first <= 1 :
        first += num
    else :
        first *= num
        
print(first)