#Quicksort :

def partition(arr):
    if len(arr) < 2:
        return arr
    arrL = []
    arrR = []
    arrE = []
    pivot = arr[0]
    
    for item in arr:
        if item>pivot:
            arrR.append(item)
        elif item<pivot:
            arrL.append(item)
        else:
            arrE.append(item)
    sub = partition(arrL) + arrE + partition(arrR)
    print(' '.join([str(x) for x in sub]))
    return(sub)
        
n = int(input())
arr = [int(i) for i in input().split()]
t = partition(arr)
