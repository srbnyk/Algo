#Given a matrix of 0's and 1's, 0's represent empty spaces and 1's represent blocked ones, and a starting positon, find the closest exit.

import collections
def find_neighbor(r,c,row,col,visited):
    temp = []
    if r+1 < row and mat[r+1][c] == 0 and (r+1,c) not in visited:
        temp.append((r+1,c))
    if r-1 >=0 and mat[r-1][c] == 0 and (r-1,c) not in visited:
        temp.append((r-1,c))
    if c+1 < col and mat[r][c+1] == 0 and (r,c+1) not in visited:
        temp.append((r,c+1))
    if c-1 >= 0 and mat[r][c-1] == 0 and (r,c-1) not in visited:
        temp.append((r,c-1))
    return temp
    
def closest_exit(mat,start):
    row = len(mat)
    col = len(mat[0])
    queue = collections.deque()  
    queue.append(start)
    visited = set()
    d = {}
    d[start] = None
    i = 0
    ans = []
    while i < len(queue):
            cell = queue[i]
            i += 1
            visited.add(cell)
            #print(cell)
            r = cell[0]
            c = cell[1]
            if r == row-1 or c == col -1 or r == 0 or c == 0:
                parent = (r,c)
                while parent:
                    ans.append(parent)
                    parent = d[parent]
                ans.reverse()
                return ans
            temp = find_neighbor(r,c,row,col,visited)
            for node in temp:
                queue.append(node) #[parent,child]
                visited.add(node)
                d[node] = cell
            
    return "no answer"

mat = [[1, 1, 1, 1,0],[1, 0, 0, 0,1], [0, 1, 0, 0, 0], [1, 0, 0, 1, 1], [1, 1, 1, 1, 1]]
#mat = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 1], [1,1, 1, 1]]
start = (3,1)
print(closest_exit(mat,start))
