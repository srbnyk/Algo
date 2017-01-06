#http://www.geeksforgeeks.org/find-next-greater-number-set-digits/

def nextLarge(l):
    n = len(l)-1
    while n > 0:
        if l[n] > l[n-1]:
            break
        n -= 1

    if n == 0:
        return "Not Possible"
    index = n
    min = l[n-1]
    max = l[n]
    for i in range(n,len(l)):
        if l[i] > min and l[i] < max:
            max = l[i]
            index = i
    l[n-1],l [index] = l[index], l[n-1]
    l[n:] = sorted(l[n:])
    for i in range(len(l)):
        l[i] = str(l[i])
    return "".join(l)


l = [3,2,1]
print(nextLarge(l))
