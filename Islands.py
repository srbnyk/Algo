https://leetcode.com/problems/number-of-islands/
    
    
class Solution(object):
    
    def find_neighbour(self,grid, test,s):
        temp = []
        if (test[0]+1 < height) and ((test[0]+1,test[1]) not in s) and grid[test[0]+1][test[1]] == "1":
            new = (test[0]+1, test[1])
            temp.append(new)

        if (test[1]+1 < length) and ((test[0],test[1]+1) not in s) and grid[test[0]][test[1]+1] == "1":
            new = (test[0], test[1]+1)
            temp.append(new)

        if (test[1]-1 >= 0) and ((test[0],test[1]-1) not in s) and grid[test[0]][test[1]-1] == "1":
            new = (test[0], test[1]-1)
            temp.append(new)

        if (test[0]-1 >= 0) and ((test[0]-1,test[1]) not in s) and grid[test[0]-1][test[1]] == "1":
            new = (test[0]-1, test[1])
            temp.append(new)
        return temp
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        height = len(grid)
        length = len(grid[0])
        island = 0
        s = set()
        queue = []
        
        for row in range(height):
            for col in range(length):
            
                if grid[row][col] == "1" and (row,col) not in s:
                    island += 1
                    s.add((row,col))
                    queue.append((row,col))

                    while queue:
                        test = queue.pop(0)
                        temp = self.find_neighbour(grid,test,s)
                        queue.extend(temp)
                        for items in temp:
                            s.add(items)
            
        return island
