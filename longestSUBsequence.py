
def generateSUB(s1,s2):
    row = len(s1)
    col = len(s2)
    mat = [[0 for j in range(col+1)] for i in range(row+1)]
    
    for i in range(0,row):
        for j in range(0,col):
            if s1[i] == s2[j]:
                mat[i+1][j+1] = mat[i][j] + 1
            else:
                mat[i+1][j+1] = max(mat[i][j+1],mat[i+1][j])
    print(mat)
    return mat[row][col]
        

    
s1 = "AGGTAB"
s2 = "GXTXAYB"

print(generateSUB(s1,s2))
