def binary_search_recur (ar,first,last,item):
    if first>last :
        return False

    mid = (first+last)/2
    if ar[mid] == item:
        return True

    if ar[mid]> item:
        last = mid-1
        return binary_search_recur(ar,first,last,item)
    else:
        first = mid+1
        return binary_search_recur(ar,first,last,item)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, 50]
bool = binary_search_recur(testlist,0,len(testlist)-1,0)
print (bool)
