import collections
def no_of_Friends(mat):
    col = 4
    row = 4
    circle = 0
    visited = set()
    queue = collections.deque()
    for r in range(row):
        if r not in visited:
            queue.append(r)
            circle += 1
            while queue:
                node = queue.popleft()
                visited.add(node)
                for c in range(col):
                    if mat[node][c] == 1 and c not in visited:
                        queue.append(c)
    return circle

mat = [
	[0, 1, 0, 0],
	[1, 0, 0, 1],
	[0, 0, 0, 0],
	[0, 1, 0, 0]
]
print (no_of_Friends(mat))
