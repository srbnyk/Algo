#Super Reduced String {https://www.hackerrank.com/challenges/reduced-string}
#Shil has a string, , consisting of  lowercase English letters. In one operation, he can delete any pair of adjacent letters with same value. For example, string "" would become either "" or "" after  operation.
#Shil wants to reduce  as much as possible. To do this, he will repeat the above operation as many times as it can be performed. Help Shil out by finding and printing 's non-reducible form!

#Code:

s = input().strip()
str_length = len(s)
stack = []
if not s:
    print ("Empty String")
elif str_length ==1:
    print(s)
else:
    stack.append(s[0])
    for i in range(1,str_length):
        if stack:
            b = stack[len(stack)-1]
        if not stack:
            stack.append(s[i])
            b = stack[len(stack)-1]
        elif s[i] ==b:
            t = stack.pop()
        else:
            
            stack.append(s[i])
if not stack:
    print ("Empty String")
else:
    print("".join(stack))
        
