
def decor(foo):
    def wraper(*args,**kwargs):
        if len(args) != 2:
            raise Exception("Լength is not equal to 2")
        for i in range(len(args)):
            if not isinstance(args[i],int):
                raise Exception("Pass 2 values of type int") 
              
        return foo(*args,**kwargs)
    return wraper         

@decor
def foo(x,y):
    return x + y

print("result =",foo(5,6))

