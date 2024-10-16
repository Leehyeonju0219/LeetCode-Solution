from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        if grid[0][0] == 1 or grid[row-1][col-1] == 1:
            return -1
        
        visited = [[False]*row for _ in range(col)]
        
        dx = [-1, -1, 0, 1, 1, 1, 0, -1]
        dy = [0, 1, 1, 1, 0, -1, -1, -1]
        q = deque()
        q.append((0,0,1))
        visited[0][0] = True
        
        while q:
            cur_x, cur_y, cur_length = q.popleft()
            if cur_x == row-1 and cur_y == col-1:
                return cur_length
            for i in range(8):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                if next_x >= 0 and next_x < row and next_y >= 0 and next_y < col:
                    if grid[next_x][next_y] == 0 and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        q.append((next_x, next_y, cur_length+1))
                   
        return -1