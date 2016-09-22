#https://www.hackerrank.com/contests/master/challenges/lisa-workbook?h_r=internal-search

def lisa_book (l, chapter, ppp):
    page = 1
    count = 0
    for i in range (chapter):
        for j in range(1, l[i]+1):
            if (page == j) :
                #print("page: "+str(page)+" j: "+str(j))
                count += 1
            
            if (j%ppp == 0 or j == l[i]):
                page += 1
                t = 0 
    return count

chapter, ppp = input().split()
chapter, ppp = int(chapter), int(ppp)
l = [int(x) for x in input().split()]
print(lisa_book(l, chapter, ppp))

