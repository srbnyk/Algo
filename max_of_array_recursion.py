#Write a recursive Python function that has a
#parameter representing a list of integers and returns the maximum
#stored in the list. Thinking recursively, the maximum is either the
#first value in the list or the maximum of the rest of the list,
#whichever is larger. If the list only has 1 integer, then its maximum
#is this single value, naturally.
#Helpful Python syntax:
#If A is a list of integers, and you want to set the list B to all of the
#integers in A except the first one, you can write
#B = A[1:len(A)] or B = A[1:]
#(This sets B to the integers in A starting at index 1 and ending at
#index len(A)-1, the last index. The integer in the first position of A
#at index 0 is not included.)


def max_recusion(ar):
    if len(ar)==1:
        return ar[0]

    return (max(ar[0],max_recusion(ar[1:])))

testlist = [0, 100, 2, 8, 13, 17, 19, 320, 42, 5]
print(max_recusion(testlist))
