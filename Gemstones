#John has discovered various rocks. Each rock is composed of various elements, and each element is represented by a lower-case Latin letter from 'a' to 'z'. An element can be present multiple times in a rock. An element is called a gem-element if it occurs at least once in each of the rocks.
#Given the list of  rocks with their compositions, display the number of gem-elements that exist in those rocks.


n = int(input().strip())
d1= {}
d2 ={}
count=0
for i in range(n):
    str1 = input().strip()
    for j in range (len(str1)):
        d1[str1[j]] =1
    for item in d1:
        if item in d2:
            d2[item] = d1[item]+d2[item]
        else:
            d2[item] = d1[item]
    d1 = {}            
for item in d2:
    if d2[item]==n:
        count +=1
print(count)
