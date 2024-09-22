
def selection_sort(ls):
    for i in range(len(ls) - 1):
        min = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[min]:
                min = j
        ls[i], ls[min] = ls[min], ls[i]
    return ls



ls = []
try:
    size = int(input("Write size "))
except ValueError:
    print("Write integer ")
else:
    for i in range(size):
        try:
            ls.append(int(input()))
        except ValueError:
            print("write integer")
    res = selection_sort(ls)
    print(res)

