n = int(input())
l = input().split(" ")
insert = l[n-1]
if (l[n-2]<l[n-1] or l[n-2] == l[n-1]):
    print(" ".join(l))   
else:
    l[n-1] = l[n-2]
    print(" ".join(l))
for i in range(n-2):
    if (l[n-3-i]>insert):
        l[n-2-i] = l[n-3-i]
        print(" ".join(l))
    else:
        l[n-2-i] = insert
        print(" ".join(l))
        break
if (l[0]>insert):
    l[0] = insert
    print (" ".join(l))
