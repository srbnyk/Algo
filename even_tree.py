# https://www.hackerrank.com/challenges/even-tree/submissions/code/29245507

def even_tree(graph, n):
    #print(graph)
    #print(nodes)
    arr = []
    t = 0
    arr.append(1)
    length_arr = 1
    while (length_arr < n):
        for item in graph[arr[t]]:
            if item not in arr:
                arr.append(item)
                length_arr += 1
                #print(length_arr)
        t += 1
    #print(arr)
    
    nodes_value = [0]*(n+1)
    while arr:
        node = arr.pop()
        #print(node)
        value = 1
        for item in graph[node]:
            if item not in arr:
                    value += nodes_value[item]
        nodes_value[node] = value
    return nodes_value
            
    
    
d ={}
nodes, edges = input().split()
nodes, edges = int(nodes), int(edges)
for i in range(edges):
    m,n = input().split()
    m,n = int(m), int(n)
    if m not in d:
        d[m]  = [n]
    else:
        d[m].append(n)
    if n not in d:
        d[n]  = [m]
    else:
        d[n].append(m)

ret_arr= even_tree(d,nodes)
no = 0
for i in range(2,nodes):
    if ret_arr[i]%2 == 0:
        no += 1
#print(ret_arr)
print(no)
