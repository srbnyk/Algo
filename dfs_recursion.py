def dfs(graph, start, visited= None):
    if visited is None:
        visited = set()
    visited.add(start)
    queue = []
    for item in graph[start] - visited:
        queue.append(item)
    print (queue)
    for item in queue:
        dfs(graph,item,visited)
    return visited



graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


t = dfs(graph, 'C')
print (t)
