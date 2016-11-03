#mat = [[1,2,3], [10,11,4],[9,12,5],[8,7,6],[13,14,15]]
mat = [[1,2,3,4,5],[12,13,14,15,6],[11,10,9,8,7]]
print(mat)
row = 3
col = 5
rn = row
cn = col
r0 = 0
c0 = 0

while (c0 < cn and r0 < rn):


    for i in range(c0,cn):
        print(mat[r0][i])
    r0 += 1

    for i in range(r0,rn):
        print (mat[i][cn-1])
    cn -= 1

    if ( r0 < rn):
        for i in range(c0,cn):
            print (mat[rn-1][cn-1-i])
    rn -= 1

    if (c0 < cn  ):
        for i in range(r0,rn):
            print (mat[rn-i][c0])

    c0 += 1
