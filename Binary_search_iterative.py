
def binary_search(ls, x):

    for i in range(len(ls)):
        if ls[i] > ls[i + 1]:
            print("The array is not sorted")
            return
        else:
            start = 0
            end = len(ls) - 1

            while start <= end:
                kes = (end + start) // 2
                if ls[kes] == x:
                    return kes
                elif ls[kes] < x:
                    start = kes + 1   
                else:
                    end = kes - 1
            return -1


try:
    size = int(input("Write size: "))
except ValueError:
    print("Write integer") 
else:    
    ls = []   
    for i in range(size):
        try:
            ls.append(float(input()))
        except ValueError:
            print("Input number")
    ls.sort()

    try:
        x = float(input("Write target number "))
    except ValueError:
        print("Write number")   
    else:
        result = binary_search(ls, x)
        if result != -1:
            print("Index: ", result)
        else:
            print("Chka")
