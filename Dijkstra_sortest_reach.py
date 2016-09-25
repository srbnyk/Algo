#https://www.hackerrank.com/challenges/dijkstrashortreach

def Dijkstra (initial, graph, distance):
    
    #print(distance)
    visited = []
    queue= []
    queue.append(initial)
    distance[initial] = 0
    
    while queue:
        
        cur_node = queue.pop()
        #print("cur_node: "+str(cur_node))
        n_node = graph[cur_node] #brings out tuple with the neighbour node and distance
        for tup in n_node:
            new_dist = distance[cur_node] + tup[1]
            #print("tup: "+str(tup))
            
            if distance[tup[0]] == -1:
                distance[tup[0]] = new_dist
                l = [tup[0]]
                queue = l+queue
               
            else:
                if distance[tup[0]] > new_dist:
                    distance[tup[0]] = new_dist
                    l = [tup[0]]
                    queue = l+queue          
    return distance

for i in range (int(input())):
    d={}
    n, e = input().split()
    n, e = int(n), int(e)
    for i in range (e):
        n1, n2, dist = input().split()
        n1, n2, dist = int(n1), int(n2), int(dist)
        if n1 not in d:
            d[n1] = [(n2,dist)]
        else:
            d[n1].append((n2,dist))
            
        if n2 not in d:
            d[n2] = [(n1,dist)]
        else:
            d[n2].append((n1,dist))
    initial = int(input())
    distance = [-1]*(n+1)
    distance[0] = -10
    t = Dijkstra(initial, d, distance)
    #print(t)
    s = []
    for items in t:
        if items != 0 and items != -10:
            s.append(str(items))
    print(" ".join(s))
                     
                  
