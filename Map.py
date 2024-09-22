def foo(x):
   return x

def maping(foo,value):
    for i in value:
        yield foo(i)

value = []
caunt = 1
try:
    size = int(input("Input caunt value: "))
except ValueError:
    print("Invalid value")  
      
for i in range(size):
    value.append(input(f"Write value {caunt}: "))
    caunt += 1

result = list(maping(foo,value))
print(" ".join(result))





