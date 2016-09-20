#http://www.geeksforgeeks.org/sort-a-stack-using-recursion/

def push(self, item):
    return self.append(item)

def top(self):
    return (self[len(self)-1])

def is_empty(self):
    if not self:
        return True
    else:
        return False

def stack_sort(s):
    if s:
        item = s.pop()
        stack_sort(s)
        insert_sort(s,item)

def insert_sort(s, item):
    if not s or item > top(s):
        push(s, item)
    else:
        temp = s.pop()
        insert_sort(s,item)
        push(s, temp)

stack = [10,2,3,4,5]
stack_sort(stack)
print (stack)
