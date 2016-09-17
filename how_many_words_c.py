#Given a string find out how many words are there

s = " this   ; is a string  \\ of 7 words     "
t=0
count = 0
for i in range(len(s)):

    if (not s[i].isalnum() or i == len(s)-1):
        if t == 1:
            count += 1
        t=0
    elif s[i].isalnum():
        t=1
print (count)
