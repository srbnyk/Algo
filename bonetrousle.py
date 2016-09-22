#https://www.hackerrank.com/challenges/bonetrousle

def no_of_box (sum, seq, boxes): #sum = 12, boxes = 3, seq = 8
    l = [0]*boxes
    seq_arr = []
    seq_arr.append(0)
    for i in range(1, seq+1):
        seq_arr.append(i)
    t = 0
    sum_check1 = 0
    sum_check2 = 0
    #print ("seq_arr")
    #print (seq_arr)

    for i in range (boxes):
        sum_check1 += seq_arr[seq-i]
    if sum_check1 < sum:
        return -1

    for i in range(1, boxes+1):
        sum_check2 += seq_arr[i]
    if sum_check2 > sum:
        return -1


    index = int(sum/boxes)
    #print ("index: "+str(index))

    if seq - index >= boxes:
        for i in range(boxes):
            l[i] = seq_arr[index+i]

    else:
        for i in range(boxes):
            l[boxes-i-1] = seq_arr [seq-i]
    #print (l)

    sum_final = 0
    for i in range(len(l)):
        sum_final += l[i]
    if sum_final == sum:
        return (' '.join(str(x) for x in l))

    t = sum_final - sum
    #print (sum_final)

   
    
    len_l= len(l)
    l2 = l
    shift = int(t/boxes)
    #print ("shift"+str(shift))
    for i in range(len_l):
        l2[i] = seq_arr[l[i]-shift]
 
    l2_sum = 0
    for i in range(len_l):
        l2_sum += l2[i]
    
    t = t %boxes
    if (t%boxes != 0):
        l2[t-1], seq_arr[l2[0]-1] = seq_arr[l2[0]-1], l2[t-1]
    return (' '.join(str(x) for x in l))

for i in range(int(input())):
    sum, boxes, seq = input().split()
    sum, boxes, seq = int(sum), int(boxes), int(seq)
    l= []
    l = no_of_box(sum,boxes,seq)
    print (l)
