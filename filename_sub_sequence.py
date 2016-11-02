def value (filename,index_file, seq, index_seq):
    if index_seq >= len(seq):
        return 0
    if (len(filename)-index_file) < (len(seq)-index_seq):
        return 0
    
    if (l[index_file][index_seq]  != -1):
        return l[index_file][index_seq]

    for i in range (index_file, len(filename)):
        if seq[index_seq] == filename[i].lower() and filename[i].isupper() :
            index_seq += 1
            l[index_file][index_seq-1] = 3 + value (filename,i+1, seq, index_seq)
            return (l[index_file][index_seq-1])
        
        if seq[index_seq] == filename[i].lower() and filename[i].islower():
            index_seq += 1
            l[index_file][index_seq-1] = max (1 + value (filename,i+1, seq, index_seq), value (filename,i+1, seq, index_seq-1))
            return (l[index_file][index_seq-1])
        
        
   

filename = "abBcC" #abcabc
seq = "abc"
l = [[-1 for i in range(len(seq))] for j in range (len(filename))]
print(value(filename, 0 , seq, 0))



#                                         "aabbcc" "abc"
#                         1 + "abbcc" "bc"                         "abbcc" "abc"
#                         "bbcc" "bc"              1 + "bbcc" "bc"        "bbcc"  "abc"
#     1 + "bcc" "c"             "bcc" "bc"            
    
#     (bbcc,bc) value 
#     (2,1) value
#     (i,j) value
#     (len(fileName) - 1,len(seq)-1) value
#     dp[i][j] = value
#
