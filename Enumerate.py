def enum(iterable, start = 0):
    for i in iterable:
        yield start, i
        start += 1

iterable = []
caunt = 1

try:
    size = int(input("Input size: "))
except ValueError:
    print("Write integer ")   
else:      
    for i in range(size):
        iterable.append(input(f"Input iterable {caunt}: "))
        caunt += 1
          
res = list(enum(iterable))
'''որպես - 2 րդ պարամետր կարող եք փոխանցել ձեր ցանկալի թիվը'''
print(res)

     
  
        
