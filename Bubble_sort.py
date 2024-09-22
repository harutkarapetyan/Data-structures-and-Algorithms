
def bubble_sort(ls):
    for i in range(len(ls) - 1):
        for j in range(len(ls) - i - 1):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
    
    return ls
      
try:
    size = int(input("Write size "))
except ValueError:
    print("Write integer ")  
else:
    ls = []
    for i in range(size):
        try:
            ls.append(int(input()))
        except ValueError:
            print("Write integer ")          
    res = bubble_sort(ls)
    print("result = ",res)