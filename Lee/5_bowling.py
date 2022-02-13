n, m = map(int,input().split())

ball = list(map(int, input().split()))

ball_b = list(set(ball))

diff = len(ball) - len(ball_b)

def factorial(n): 
    if(n > 1): 
        return n * factorial(n - 1) 
    else: 
        return 1

def combination(n, m):
    return int(factorial(n) / (factorial(n-m) * factorial(m)))

print(combination(n, 2) - diff)