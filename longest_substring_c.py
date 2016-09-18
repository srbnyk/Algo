#Given a string, find the length of the longest substring without repeating characters

#Examples:

#Given "abcabcbb", the answer is "abc", which the length is 3.
#Given "bbbbb", the answer is "b", with the length of 1.
#Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
#https://leetcode.com/problems/longest-substring-without-repeating-characters/

str = "xxyzzqw"
count = 0
j = 1
l = []
d = {}
i = 0
for i in range (len(str)):
    if str[i] not in d:
        d[str[i]] = 1
        count += 1

    else:
        l.append((len(str[j-1:i]), str[j-1:i]))
        j=i+1
        count = 1
        d.clear()
        d[str[i]]= 1
l.append((len(str[j-1:len(str)]), str[j-1:len(str)]))

l.sort()
print(l[len(l)-1])
