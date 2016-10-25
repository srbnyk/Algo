#https://www.hackerrank.com/challenges/ctci-recursive-staircase/submissions/code/30930888

def steps(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if ar[n] != -1:
        return ar[n]
    ar[n]= steps(n-1)+steps(n-2)+steps(n-3)
    return ar[n]

s = int(input().strip())
l = []
    
for a0 in range(s):
    n = int(input().strip())
    l.append(n)

ar = [-1]*37

for n in l:
    t= steps(n)
    print(t)
