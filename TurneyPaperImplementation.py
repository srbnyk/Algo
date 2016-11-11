Turney, Peter D. 2002. “Thumbs Up or Thumbs Down? Semantic Orientation Applied to Unsupervised Classification of Reviews.” Proceedings of the 40th Annual Meeting of the Association for Computational Linguistics (ACL).

import random
import os
import math

def remove_extra_char(l):
    chars = set('.,;:()!?"')
    temp = []
    for items in l:
        if any((c in chars) for c in items):
            temp.append(items)

    l = [item for item in l if item not in temp]
    return l

def excellent_tuple(a,b,i):
    t = 0
    for j in range(1, 11):
        if i - j > 0:
            if "excellent" in l[i - j]:
                t = 1
        if i + j + 1 < len(l):
            if "excellent" in l[i + j + 1]:
                t = 1
    if t == 1:
        d_excellent[(a[0], b[0])] += 1

def poor_tuple(a,b,i):
    t = 0
    for j in range(1, 11):
        if i - j > 0:
            if "poor" in l[i - j]:
                t = 1
        if i + j + 1 < len(l):
            if "poor" in l[i + j + 1]:
                t = 1
    if t == 1:
        d_poor[(a[0], b[0])] += 1
        

def get_tag ():
    for i in range(len(l) - 1):

        if "_JJ_" in l[i]:
            if ("_NN_" in l[i + 1] or "_NNS_" in l[i + 1]):
                # print (l[i] +" "+l[i+1])
                a = l[i].split("_")
                b = l[i + 1].split("_")
                if (a[0], b[0]) not in d_excellent:
                    d_excellent[(a[0], b[0])] = 0
                if (a[0], b[0]) not in d_poor:
                    d_poor[(a[0], b[0])] = 0
                # if ((a[0],b[0])) within 10 words to excellent
                excellent_tuple(a,b,i)
                poor_tuple(a,b,i)

        if i + 2 < len(l):
            if "_RB_" in l[i] or "_RBR_" in l[i] or "_RBS_" in l[i]:
                if ("_JJ_" in l[i + 1]):
                    if ("_NN_" not in l[i + 2] and "_NNS_" not in l[i + 2]):
                        # print (l[i] +" "+l[i+1])
                        a = l[i].split("_")
                        b = l[i + 1].split("_")
                        if (a[0], b[0]) not in d_excellent:
                            d_excellent[(a[0], b[0])] = 0

                        if (a[0], b[0]) not in d_poor:
                            d_poor[(a[0], b[0])] = 0
                        excellent_tuple(a,b,i)
                        poor_tuple(a,b,i)

        if i + 2 < len(l):
            if "_JJ_" in l[i]:
                if "_JJ_" in l[i + 1]:
                    if ("_NN_" not in l[i + 2] and "_NNS_" not in l[i + 2]):
                        # print (l[i] +" "+l[i+1])
                        a = l[i].split("_")
                        b = l[i + 1].split("_")
                        if (a[0], b[0]) not in d_excellent:
                            d_excellent[(a[0], b[0])] = 0
                        if (a[0], b[0]) not in d_poor:
                            d_poor[(a[0], b[0])] = 0
                        excellent_tuple(a,b,i)
                        poor_tuple(a,b,i)

        if i + 2 < len(l):
            if ("_NN_" in l[i] or "_NNS_" in l[i]):
                if "_JJ_" in l[i + 1]:
                    if ("_NN_" not in l[i + 2] and "_NNS_" not in l[i + 2]):
                        # print (l[i] +" "+l[i+1])
                        a = l[i].split("_")
                        b = l[i + 1].split("_")
                        if (a[0], b[0]) not in d_excellent:
                            d_excellent[(a[0], b[0])] = 0
                        if (a[0], b[0]) not in d_poor:
                            d_poor[(a[0], b[0])] = 0
                        excellent_tuple(a,b,i)
                        poor_tuple(a,b,i)

        if "_RB_" in l[i] or "RBR" in l[i] or "RBS" in l[i]:
            if ("_VB_" in l[i + 1] or "_VBD_" in l[i + 1] or "_VBN_" in l[i + 1] or "_VBG_" in l[i + 1]):
                # print (l[i] +" "+l[i+1])
                a = l[i].split("_")
                b = l[i + 1].split("_")
                if (a[0], b[0]) not in d_excellent:
                    d_excellent[(a[0], b[0])] = 0
                if (a[0], b[0]) not in d_poor:
                    d_poor[(a[0], b[0])] = 0
                excellent_tuple(a,b,i)
                poor_tuple(a,b,i)


def get_phrase():
    for i in range(len(l) - 1):
        if "_JJ_" in l[i]:
            if ("_NN_" in l[i + 1] or "_NNS_" in l[i + 1]):
                a = l[i].split("_")
                b = l[i + 1].split("_")
                if (a[0], b[0]) not in d_test:
                    d_test[(a[0], b[0])] = 0


        if i + 2 < len(l):
            if "_RB_" in l[i] or "_RBR_" in l[i] or "_RBS_" in l[i]:
                if ("_JJ_" in l[i + 1]):
                    if ("_NN_" not in l[i + 2] and "_NNS_" not in l[i + 2]):
                        a = l[i].split("_")
                        b = l[i + 1].split("_")
                        if (a[0], b[0]) not in d_test:
                            d_test[(a[0], b[0])] = 0



        if i + 2 < len(l):
            if "_JJ_" in l[i]:
                if "_JJ_" in l[i + 1]:
                    if ("_NN_" not in l[i + 2] and "_NNS_" not in l[i + 2]):
                        # print (l[i] +" "+l[i+1])
                        a = l[i].split("_")
                        b = l[i + 1].split("_")
                        if (a[0], b[0]) not in d_test:
                            d_test[(a[0], b[0])] = 0



        if i + 2 < len(l):
            if ("_NN_" in l[i] or "_NNS_" in l[i]):
                if "_JJ_" in l[i + 1]:
                    if ("_NN_" not in l[i + 2] and "_NNS_" not in l[i + 2]):
                        # print (l[i] +" "+l[i+1])
                        a = l[i].split("_")
                        b = l[i + 1].split("_")
                        if (a[0], b[0]) not in d_test:
                            d_test[(a[0], b[0])] = 0


        if "_RB_" in l[i] or "RBR" in l[i] or "RBS" in l[i]:
            if ("_VB_" in l[i + 1] or "_VBD_" in l[i + 1] or "_VBN_" in l[i + 1] or "_VBG_" in l[i + 1]):
                # print (l[i] +" "+l[i+1])
                a = l[i].split("_")
                b = l[i + 1].split("_")
                if (a[0], b[0]) not in d_test:
                    d_test[(a[0], b[0])] = 0




pos_file = os.getcwd() + "/pos"
neg_file = os.getcwd() + "/neg"

final_count = 0.000
for t in range(10):
    main_list_pos = []
    main_list_neg = []
    #for filename in os.listdir(file_name):
    for files in os.listdir(pos_file):
        main_list_pos.append(files)
    for files in os.listdir(neg_file):
        main_list_neg.append(files)

    train_list_pos = random.sample(main_list_pos, 900)
    train_list_neg = random.sample(main_list_neg, 900)

    #l = [item for item in l if item not in temp]
    test_list_pos = [item for item in main_list_pos if item not in train_list_pos]
    test_list_neg = [item for item in main_list_neg if item not in train_list_neg]

    d_excellent = {}
    d_poor = {}
    hit_excellent = 0
    hit_poor = 0
    excellent_poor = []

    for file in train_list_pos:
        f = open(pos_file+"/"+file)
        s = f.read()
        l = s.split()
        l = remove_extra_char(l)

        get_tag()

        for i in range(len(l) - 1):

            if "excellent" in l[i]:
                hit_excellent += 1

            if "poor" in l[i]:
                hit_poor += 1

    # get the d_excellent and d_poor dictionaries for 900 pos files

    for file in train_list_neg:
        f = open(neg_file + "/" + file)
        s = f.read()
        l = s.split()
        l = remove_extra_char(l)

        get_tag()

        for i in range(len(l) - 1):

            if "excellent" in l[i]:
                hit_excellent += 1
                #print ("yes")

            if "poor" in l[i]:
                hit_poor += 1

    # Testing starts here:
    count = 0.000

    # for each test file in pos test cases:
    for file in test_list_pos:

        d_test = {}

        hit_phrase_near_excellent = 0
        hit_phrase_near_poor = 0
        SO = 0
        f = open(pos_file + "/" + file)
        s = f.read()
        l = s.split()
        l = remove_extra_char(l)
        get_phrase()

        for item in d_test:
            if item in d_excellent:
                hit_phrase_near_excellent = d_excellent[item]
            else:
                hit_phrase_near_excellent = 0.01

            if item in d_poor:
                hit_phrase_near_poor = d_poor[item]
            else:
                hit_phrase_near_poor = 0.01


            if hit_phrase_near_excellent == 0:
                hit_phrase_near_excellent = 0.01

            if hit_phrase_near_poor == 0:
                hit_phrase_near_poor = 0.01

            if (hit_phrase_near_excellent != 0.01 or hit_phrase_near_poor != 0.01):
                SO += math.log(float(hit_phrase_near_excellent*hit_poor) / float(hit_phrase_near_poor*hit_excellent))
        if SO > 0:
            count += 1

    # for each test file in pos test cases:
    for file in test_list_neg:

        d_test = {}

        hit_phrase_near_excellent = 0
        hit_phrase_near_poor = 0
        SO = 0
        f = open(neg_file + "/" + file)
        s = f.read()
        l = s.split()
        l = remove_extra_char(l)
        get_phrase()

        for item in d_test:

            if item in d_excellent:
                hit_phrase_near_excellent = d_excellent[item]
            else:
                hit_phrase_near_excellent = 0.01

            if item in d_poor:
                hit_phrase_near_poor = d_poor[item]
            else:
                hit_phrase_near_poor = 0.01

            if hit_phrase_near_excellent == 0:
                hit_phrase_near_excellent = 0.01

            if hit_phrase_near_poor == 0:
                hit_phrase_near_poor = 0.01

            if (hit_phrase_near_excellent != 0.01 or hit_phrase_near_poor != 0.01):
                SO += math.log(float(hit_phrase_near_excellent * hit_poor) / float(hit_phrase_near_poor * hit_excellent))
        if SO <= 0:
            count += 1
    final_count += float(count/2)
    print ("[INFO] Fold "+str(t)+" Accuracy: "+str(float(count/200)))
    #print(float(count/2))

#print (final_count)
print ("[INFO] Accuracy: "+str(float(final_count/1000)))
#print (float(final_count/10))
