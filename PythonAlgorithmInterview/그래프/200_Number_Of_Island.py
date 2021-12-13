from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
# bfs 풀이는 추후 다시 보기
#         def bfs(grid, i, j, visited) :
#             q = deque()
#             q.append((i,j))
#             grid[i][j] = "0"

#             dx = [0,0,1,-1]
#             dy = [1,-1,0,0]

#             while q :
#                 x,y = q.popleft()
#                 for k in range(4) :
#                     nx = x + dx[k]
#                     ny = y + dy[k]

#                     if nx <= -1 or nx >= len(grid) or ny <= -1 or ny >= len(grid[0]) :
#                         continue

#                     if grid[nx][ny] == "1" and (nx,ny) not in visited :
#                         grid[nx][ny] = "0"
#                         q.append((nx,ny))
#                         visited.append((nx, ny))
        def dfs(grid, x, y) :
            if x <= -1 or x >= len(grid) or y <= -1 or y >= len(grid[0]) :
                return False
            
            if grid[x][y] == "1" :
                grid[x][y] = "0"
            
                dfs(grid, x+1, y)
                dfs(grid, x, y+1)
                dfs(grid, x-1, y)
                dfs(grid, x, y-1)
                
                return True
            
            else :
                return False
            
            
        # visited = []
        cnt = 0
        for i in range(len(grid)) :
            for j in range(len(grid[i])) :
                if grid[i][j] == "1" :
                    # bfs(grid,i,j,visited)
                    dfs(grid,i,j)
                    cnt += 1
        return cnt