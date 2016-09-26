#https://www.hackerrank.com/challenges/primsmstsub

import heapq

def prims (initial, graph, dist,n):
    queue = []
    visited = []
    queue.append((0,initial))
    dist[initial] = 0
    heapq.heapify(queue)
     
    while queue :
        node = heapq.heappop(queue) #node = (distance, node)
        if node[1] not in visited:
            dist[node[1]] = node[0]
        visited.append(node[1])
      
        for item in graph[node[1]]: #item = (node, distance) {from graph}
            if item[0] not in visited and dist[item[0]] == -1:
                heapq.heappush(queue,(item[1],item[0]))
                
    return dist  
n, e = input().split()
n, e = int(n), int(e)
d= {}
for i in range (e):
    n1, n2, w = input().split()
    n1, n2, w = int(n1), int(n2), int(w)
    if n1 in d:
        d[n1].append((n2,w))
    else:
        d[n1] = [(n2,w)]
        
    if n2 in d:
        d[n2].append((n1,w))
    else:
        d[n2] = [(n1,w)]
initial = int(input())
dist = [-1]*(n+1) # dist[0] will always be -1. {Inorder to avoid the confusion}
t= prims(initial, d, dist, n)

sum = 0
for item in t:
    if item !=0 and item != -1:
        sum += item
print(sum)
