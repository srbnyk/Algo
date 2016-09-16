#Equal stack: {https://www.hackerrank.com/contests/master/challenges/equal-stacks?h_r=internal-search}

#You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. You can change the height of a stack by removing and discarding its topmost cylinder any number of times.
#Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. This means you must remove zero or more cylinders from the top of zero or more of the three stacks until they're all the same height, then print the height. The removals must be performed in such a way as to maximize the height.


import sys
 
n1,n2,n3 = input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
h2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
h3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]
 
h1.reverse()
h2.reverse()
h3.reverse()
 
h1Size = sum(h1)
h2Size = sum(h2)
h3Size = sum(h3)
 
while(h1Size != h2Size or h1Size != h3Size or h2Size != h3Size):
    if(h1Size > h2Size or h1Size > h3Size):
        h1Size -= h1.pop()
    elif h2Size > h1Size or h2Size > h3Size:
        h2Size -= h2.pop()
    elif h3Size > h1Size or h3Size > h2Size:
        h3Size -= h3.pop()
print(h1Size)
