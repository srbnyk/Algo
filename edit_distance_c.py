#Given two strings find out if edit distance between the words is 1.
#Assuming only one space in between words"
s1 = "kitten"
s2 = "sittin"

l1 = len(s1)
l2 = len(s2)

diff = abs(len(s1)-len(s2))
count = diff

if diff > 1:
    print ("no")
    exit()
else:
    if l1 > l2:
        it_count = l2
    else:
        it_count = l1
    for i in range(it_count):
        if s1[i] != s2[i]:
            count +=1
print (count)
if count == 1:
    print ("no")
else:
    print ("yes")
