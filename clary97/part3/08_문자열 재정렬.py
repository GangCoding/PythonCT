s = input()
s = ''.join(sorted(list(s)))

string = ''
num = 0

for ch in s :
    if ch not in "0123456789" :
        string += ch
    else :
        num += int(ch)
        
result = string + str(num)
    
print(result)