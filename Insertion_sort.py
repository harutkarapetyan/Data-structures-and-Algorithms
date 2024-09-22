def insertion_sort(ls):
    for i in range(1,len(ls)):
        value = ls[i]
        
        while ls[i - 1] > value and i > 0:
            ls[i - 1], ls[i] = ls[i], ls[i - 1]
            i = i - 1

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
    print(insertion_sort(ls))   