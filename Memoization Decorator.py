
d = {}
def decor(foo):
    def wrapper(*args,**kwargs):
        if len(args) != 1:
                raise Exception("Լength is not equal to 1")
        for i in args:
            if not isinstance(i,int):
                raise Exception("Type args not int")
        if args in d:
            return d[args]
        else:
            d[args] = foo(*args,**kwargs)
            return d[args]
    return wrapper     

@decor      
def foo(x):
    return x + 5

print("result =",foo(5))