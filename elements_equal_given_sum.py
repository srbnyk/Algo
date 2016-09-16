#Given a list of numbers and a sum as input, display any one pair of numbers from the list whose sum is equal to the given sum. 

def elements_equal_sum(ar,item):
    ar.sort()
    ans = []
    first = 0
    last = len(ar)-1
    while first <= last:
        if ar[first]+ar[last] == item:
            ans.append((ar[last],ar[first]))
            last -= 1
            first +=1

        elif ar[first]+ar[last] > item:
            last -= 1
        else:
            first += 1
    return ans

testlist = [0, 100, 2, 102, 99, 3, 19, 320, 42, 5]
print(elements_equal_sum(testlist,102))
