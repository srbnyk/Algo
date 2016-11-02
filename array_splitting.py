#https://www.hackerrank.com/challenges/array-splitting

def value (arr, start, end, sum):
 
    if (sum == 0 ):
        return end
    if (sum%2 != 0):
        return 0
    
    temp = 0
    index = start
    
    for i in range(start,end+1):
        temp += arr[i]
        index = i
        if (temp == int(sum/2)):
            break
    ret_sum = int(sum/2)
    
    if (index == end):
        return 0
    
    return (1+ max (value(arr, start, index, ret_sum), value(arr, index+1, end, ret_sum)))
    
for i in range(int(input())):
    length = int(input())
    arr = input().split()
    sum = 0
    for i in range(length):
        arr[i] = int(arr[i])
        sum += arr[i]
    print(value(arr, 0, length-1, sum))
