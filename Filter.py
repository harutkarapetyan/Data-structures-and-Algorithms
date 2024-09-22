
ls = [1,3,8,7,6]

def foo(n):
    if n % 2 == 0:
        return True

def filterr(foo,iter):
    for i in iter:
        if foo(i):
            yield i

res = list(filterr(foo,ls))
print(res)   