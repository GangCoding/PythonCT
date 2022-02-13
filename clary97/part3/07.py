n = int(input())
num = int(n/2)

n_list = list(map(int, str(n)))

result = 0
result2 = 0

for i in range(int(len(n_list)/2)) :
    result += n_list[i]
    
for k in range(len(n_list)) :
    result2 += n_list[k]

result2 = result2 - result

if result == result2 :
    print("LUCKY")
else :
    print("READY")