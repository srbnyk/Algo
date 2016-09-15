#Bigger is Greater {https://www.hackerrank.com/challenges/bigger-is-greater}
#Given a word , rearrange the letters of  to construct another word  in such a way that  is lexicographically greater than . In case of multiple possible answers, find the lexicographically smallest one among them.

#Code:

def lex(str):
    l = list(str)
    c= int()
    length = len(l)
    if length < 2:
        return "no answer"
    t=0
    count1=1
    count2=1
    for i in range(0,length-1):
        if l[length-2-i] > l[length-1-i]:
            count2 += 1
       
        elif l[length-1-i] > l[length-2-i]:
            t=1
            imbig = l[length-1-i]
            c =length-1-i
            for k in range(0,i):
                if l[length-2-i] < l[length-k-1]:
                    if imbig > l[length-k-1]:
                        imbig = l[length-k-1]
                        c = length -k -1
            l[length-2-i], l[c] = l[c], l[length-2-i]
            l1 = l[:length-i-1]
            l2 = l[-i-1:]
            #l3 = l2[::-1]
            l2.sort()
            l4 = l1+l2
            str = ''.join(l4)
            return str
        
        else:
            count1 += 1

    if count1 == length:
        return "no answer"
    if count1+count2-1 ==length:
        
        return "no answer"
    if count2 ==length:
        return "no answer"


noi = int(input())
for i in range(0,noi):
    print(lex(input()))
    

