people = int(input())
pi = list(map(int, input().split()))

pi.sort()

for i in range(1, people) :
    pi[i] += pi[i-1]
    
print(sum(pi))