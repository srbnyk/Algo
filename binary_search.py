def binary_search(ar, item):
    value = False
    first = 0
    last = len(ar)-1
    while first <= last:
        midpoint = (first+last)/2
        if item == ar[midpoint]:
            return True
        if ar[midpoint]>item:
            last = midpoint-1
        else:
            first = midpoint+1
    return  value

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, 50]
print(binary_search(testlist,12))
