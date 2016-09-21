#https://www.hackerrank.com/challenges/bfsshortreach
#Consider an undirected graph consisting of  nodes where each node is labeled from  to  and the edge between any two nodes is always of length . We define node  to be the starting position for a BFS.
#Given  queries in the form of a graph and some starting node, , perform each query by calculating the shortest distance from starting node  to all the other nodes in the graph. Then print a single line of  space-separated integers listing node 's shortest distance to each of the  other nodes (ordered sequentially by node number); if  is disconnected from a node, print  as the distance to that node.

def bfs_shortest(graph,initial,final):
    if not graph[final]:
        return -1
    visited = set()
    stack = [initial]
    path = 0
    while stack:
        item = stack.pop()
        if item not in visited:
            visited.add(item)
            l = [x for x in graph[item] if x not in visited if x not in stack]
            if final in l:
                path += 6
                return path
            else:
                path += 6
            stack = l+stack
    return -1


for i in range(int(input())):
    l = [int(x) for x in input().split()]
    nodes, edges = l[0], l[1]
    #print(nodes)
    d = {}
    for i in range (1, nodes+1):
        d[i] = []
    for i in range(edges):
        map = [int(x) for x in input().split()]
        if d[map[0]] is None:
            d[map[0]] = map[1]
        else:
            d[map[0]].append(map[1])
        if d[map[1]] is None:
            d[map[1]] = map[0]
        else:
            d[map[1]].append(map[0])
    #print(d)
    initial = int(input())
    t=[]
    for i in range(1,nodes+1):
        if i != initial:
            t.append(bfs_shortest(d,initial,i))
    
    s = " ".join([str(x) for x in t])
    print(s)
