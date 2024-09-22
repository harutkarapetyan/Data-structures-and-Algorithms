
cashe = {}

def factor(n):
    if n in cashe:
        return cashe[n]
    elif n == 1 or n == 0:
        return 1
    elif n < 0:
        return -1
    else:
        cashe[n] = n * factor(n-1)
    return cashe[n]   

try:
    n = int(input("Write number "))
    res = factor(n)
    print("result =",res) 
except ValueError:
    print("Write integer ")   