s = input()
s = s+str(1)

output = []

for i in range(1,len(s)+1):
    temp = []
    result = []
    answer = []
    for j in range(0, len(s), i):
        temp.append(s[j:j+i])
    ############분 할#############
    start = 0
    end = 0
    for k in range(len(temp) - 1):
        if temp[k] != temp[k+1]:
            end = k+1
            result.append(temp[start:end])
            start = end
    result.append(temp[end:])
    ########### 같은 문자열끼리 분할 ###########
    for l in range(len(result)):
        num = 0
        if len(result[l]) != 1:
            num = result[l].count(result[l][0])
            answer.append(str(num) + result[l][0])
        if len(result[l]) == 1:
            answer.append(result[l][0])
    ################ 같은 문자열 count ##################
    output.append(len(''.join(answer)))

print(min(output) - 1)

