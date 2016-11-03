import sys

def viterbi (sentence, tag_list_dict, word_tag_dict, tag_tag_dict):

    #print (sentence)
    viterbi_matrix = [[0 for x in range(len(sentence))] for y in range(len(tag_list_dict))]
    back_ptr_matrix = [[0 for x in range(len(sentence))] for y in range(len(tag_list_dict))]
    forward_matrix = [[0 for x in range(len(sentence))] for y in range(len(tag_list_dict)+1 )]
    viterbi_matrix[4][0] = 1
    for k in range (1, len(sentence)):
    #for k in range(1, 4):

        for tag2 in tag_list_dict:
            max_prob = 0
            sum_forward = 0
            back_ptr_tag = ""
            for tag1 in tag_list_dict:

#viterbi_matrix[tag_list_dict[tag2]][k] = max(viterbi_matrix[tag_list_dict[tag1]][k - 1]) * tag_tag_dict[(tag1, tag2)] * word_tag_dict[(sentence[k], tag2)]
                #print ("checking for: previous tag: "+ tag1 + " current tag: "+tag2)
                if (tag1, tag2) not in tag_tag_dict:
                    tag_tag_dict[(tag1, tag2)] = 0.0001
                if (sentence[k], tag2) not in word_tag_dict:
                    word_tag_dict[(sentence[k], tag2)] = 0.0001

                temp = (viterbi_matrix[tag_list_dict[tag1]][k - 1]) * float(tag_tag_dict[(tag1, tag2)]) * float(word_tag_dict[(sentence[k], tag2)])
                sum_forward += temp
                if temp > max_prob:
                    max_prob = temp
                    back_ptr_tag = tag1
            viterbi_matrix[tag_list_dict[tag2]][k] = max_prob
            back_ptr_matrix[tag_list_dict[tag2]][k] = back_ptr_tag
            forward_matrix[tag_list_dict[tag2]][k] = sum_forward

    tag2 = "fin"
    for tag1 in tag_list_dict:
        #viterbi_matrix[tag_list_dict[tag1]][len(sentence)-1]=
        if (tag1, tag2) not in tag_tag_dict:
            tag_tag_dict[(tag1, tag2)] = 0.0001
        viterbi_matrix[tag_list_dict[tag1]][len(sentence) - 1] = (viterbi_matrix[tag_list_dict[tag1]][len(sentence)-2]) * float(tag_tag_dict[(tag1, tag2)])

    # print (viterbi_matrix)
    # print (back_ptr_matrix)
    # print (forward_matrix)

    #reducing the length of sentence here:

    sentence.remove("fin")
    sentence.remove(("phi"))

    print ("\n\nPROCESSING SENTENCE: "+" ".join(sentence))
    print("\nFINAL VITERBI NETWORK")
    length_sentence = len(sentence)
    for k in range(1, length_sentence+1):
        for items in tag_list_dict:
            if items != "fin" and items!= "phi":
                no = "{0:.10f}".format(viterbi_matrix[tag_list_dict[items]][k])
                print ("P("+sentence[k-1]+"="+items+")="+str(no))

    print ("\nFINAL BACKPTR NETWORK")
    best_tag_seq = 0
    tag_greatest_prob = ""

    for i in range(2,length_sentence):
        for items in tag_list_dict:
            if items != "fin" and items != "phi":
                temp1 = back_ptr_matrix[tag_list_dict[items]][i]
                print ("Backptr("+sentence[i-1]+"="+items+") = "+ temp1)

    for items in tag_list_dict:
        if items != "fin" and items != "phi":
            temp1 = back_ptr_matrix[tag_list_dict[items]][length_sentence]
            temp2 = viterbi_matrix[tag_list_dict[items]][length_sentence+1]
            print ("Backptr("+sentence[length_sentence-1]+"="+items+") = "+ temp1)
            if temp2 > best_tag_seq:
                best_tag_seq = temp2
                tag_greatest_prob = items
    no = "{0:.10f}".format(best_tag_seq)
    print ("\nBEST TAG SEQUENCE HAS PROBABILITY = "+str(no))
    print (sentence[length_sentence-1]+" -> "+tag_greatest_prob)

    for i in range (1, length_sentence):
        tag_greatest_prob = back_ptr_matrix[tag_list_dict[tag_greatest_prob]][length_sentence-i+1]
        print (sentence[length_sentence-1-i]+" -> "+ tag_greatest_prob)

    for i in range(1,len(sentence)+1):
        sum_temp_forward = 0
        for j in range(len(tag_list_dict)-2):
            sum_temp_forward += forward_matrix[j][i]
        forward_matrix[len(tag_list_dict)][i] = sum_temp_forward

#Normalizing the forward matrix:
    for i in range(1, len(sentence) + 1):
        for j in range(len(tag_list_dict) - 2):
            forward_matrix[j][i] = forward_matrix[j][i]/forward_matrix[len(tag_list_dict)][i]

#Display the forward matrix:
    print ("\nFORWARD ALGORITHM RESULTS")
    for k in range(1, length_sentence + 1):
        for items in tag_list_dict:
            if items != "fin" and items != "phi":
                no = "{0:.10f}".format(forward_matrix[tag_list_dict[items]][k])
                print ("P(" + sentence[k - 1] + "=" + items + ")=" + str(no))

tag_list_dict = {"noun":0,"verb":1,"inf": 2, "prep": 3,"phi":4, "fin":5}
word_tag_dict = {}
tag_tag_dict = {}
t = 0

filename1 = sys.argv[1]
f = open(filename1)
for line in f:
    t= 0
    l = line.split()
    if l[0] not in tag_list_dict or l[1] not in tag_list_dict:
        t = 1
    #no = "%.2f" % float(l[2])

    if t ==1:
        word_tag_dict[(l[0],l[1])]=l[2]
    else:
        tag_tag_dict[(l[1],l[0])]= l[2]
# print (word_tag_dict)
# print (tag_tag_dict)

filename2 = sys.argv[2]
f = open(filename2)
for line in f:
    sentence = line.split()
    sentence = [content.lower() for content in sentence]
    sentence.insert(0,"phi")
    sentence.append("fin")
    viterbi (sentence, tag_list_dict, word_tag_dict, tag_tag_dict)
