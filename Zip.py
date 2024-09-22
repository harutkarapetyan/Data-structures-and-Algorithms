
ls1 = [1, 2, 3]
ls2 = [4, 5, "b","D",6]
ls3 = [1, 4, 8]

def ziip(*args):
    min = len(args[0])

    for i in range(len(args)):
        if len(args[i]) < min:
            min = len(args[i])

    for i in range(min):
        tup = tuple(a[i] for a in args)  
        yield tup

res = list(ziip(ls1, ls2, ls3))
for i in res:
    print(i)

    

