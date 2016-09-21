def bfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        item = stack.pop()
        if item not in visited:
            visited.add(item)
            l = [x for x in graph[item] if x not in stack if x not in visited]
            print (l+stack)
            stack = l+stack

graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

bfs (graph, 'A')
