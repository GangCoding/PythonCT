n = int(input())

def pibo(x):
    if x == 1:
        return 1
    if x == 0:
        return 0
    else:
        return pibo(x-1) + pibo(x-2)


print(pibo(n))
