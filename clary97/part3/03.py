s = input()

all_0 = 0
all_1 = 0

if s[0] == '1' :
    all_0 += 1
else :
    all_1 += 1

for i in range(len(s)-1) :
    if s[i] != s[i+1] :
        if s[i+1] == '1' :
            all_0 += 1
        else :
            all_1 += 1
            
print(min(all_0, all_1))