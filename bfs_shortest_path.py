def bfs_shortest(graph,initial,distance):
    visited = set()
    stack = [initial]
    distance[initial-1] = 0
    while stack:
        item = stack.pop()
        if item not in visited:
            visited.add(item)
            l = [x for x in graph[item] if x not in visited if x not in stack]
            stack = l+stack
            for elements in l:
                if distance[elements-1] == -1:
                    distance[elements-1] = distance[item-1]+6
    return distance


for i in range(int(input())):
    l = [int(x) for x in input().split()]
    nodes, edges = l[0], l[1]
    distance = [-1]*nodes
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
    distance= bfs_shortest(d,initial,distance)
    #print (distance)
    del distance[initial-1]
    print (" ".join([str(x) for x in distance]))
