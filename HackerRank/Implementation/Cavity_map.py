# Complete the cavityMap function below.

# 210514 풀이
def cavityMap(grid):
    # Write your code here
    n = len(grid)
    check = []
    
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    for i in range(1, n-1) :
        for j in range(1, n-1) :
            flag = True
            for d in range(4) :
                px = i + dx[d]
                py = j + dy[d]
                
                if 0 <= px < n and 0 <= py < n :
                    if grid[i][j] <= grid[px][py] :
                        flag = False
                        break
                 
                        
            if flag :
                check.append((i,j))
    
    result = []
    for i in range(n) :
        tmp = ""
        for j in range(n) :
            if (i,j) in check :
                tmp += "X"
            else :
                tmp += str(grid[i][j])
        result.append(tmp)
    
    return result

# 210512 힌트 보고 풀어서 이해한게 아님
# def cavityMap(grid):
#     # Write your code here
#     dx = [-1,0,1,0]
#     dy = [0,-1,0,1]
#     n = len(grid)
    
#     check = []
#     for i in range(1,n-1) :
#         for j in range(1, n-1) :            
#             flag = True
#             for d in range(4) :
#                 p_i = i + dx[d]
#                 p_j = j + dy[d]
                
#                 if 0 <= p_i < n and 0 <= p_j < n :
#                     if grid[i][j] > grid[p_i][p_j] :
#                         continue
#                     else :
#                         flag = False
#                         break
#             if flag :
#                 check.append((i,j))
    
#     new_grid = []
#     for i in range(n) :
#         tmp = ""
#         for j in range(n) :
#             if (i,j) in check :
#                 tmp += 'X'
#             else :
#                 tmp += str(grid[i][j])
#         new_grid.append(tmp)
            
#     return new_grid

# def cavityMap(grid):
#     new_grid = []
#     # 해당 grid를 리스트 형태로 변환
#     for g in grid :
#         new_grid.append(list(g))
    
#     # 가장 깊이가 깊은곳의 위치를 담는 리스트
#     max_depth = []
#     for i in range(1, len(new_grid)-1) :
#         for j in range(1, len(new_grid[i])-1) :
#             # 현재 위치에 있는 값을 저장
#             curr = new_grid[i][j]
#             # print(i,j)
#             # 동서남북으로 둘러보았을때, 현재 위치가 가장 깊은곳이라면 해당 위치를 max_depth에 저장
#             if new_grid[i][j-1] < curr and new_grid[i][j+1] < curr and new_grid[i-1][j] < curr and new_grid[i+1][j] < curr :
#                 max_depth.append((i,j))
#             else :
#                 continue
                
#     # print(new_grid)

#     # 저장한 위치에 'X'를 표시
#     for pos in max_depth :
#         new_grid[pos[0]][pos[1]] = 'X'
    
#     grid = []
#     # 리스트로 되었던 값들을 문자열로 변환
#     for g in new_grid :
#         grid.append(''.join(g))
    
#     # print(grid)
#     # 값 리턴
#     return grid

grid = ['1112', '1912', '1892', '1234']
cavityMap(grid)