def fibon(n):
    if n <= 0:
        print("Invalid value")
    elif n == 1 or n == 2:
        return 1
    else:
        return fibon(n-1) + fibon(n - 2)

try:
    n = int(input("Write num: "))
    res = fibon(n)
    print("result =",res)
except ValueError:
    print("Write integer")    