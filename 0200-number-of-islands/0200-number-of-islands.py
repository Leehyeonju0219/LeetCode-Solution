from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nums_of_islands = 0
        row = len(grid)
        col = len(grid[0])
        visited = [[False]*col for _ in range(row)]
        
        def bfs(x, y):
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            q = deque()
            q.append((x, y))
            visited[x][y] = True
        
            while q:
                cur_x, cur_y = q.popleft()
                for i in range(4):
                    next_x = cur_x + dx[i]
                    next_y = cur_y + dy[i]
                    if next_x >= 0 and next_x < row and next_y >= 0 and next_y < col:
                        if grid[next_x][next_y] == "1" and not visited[next_x][next_y]:
                            visited[next_x][next_y] = True
                            q.append((next_x, next_y))
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(i, j)
                    nums_of_islands += 1
                    
        return nums_of_islands