# Complete the cavityMap function below.
def cavityMap(grid):
    new_grid = []
    # 해당 grid를 리스트 형태로 변환
    for g in grid :
        new_grid.append(list(g))
    
    # 가장 깊이가 깊은곳의 위치를 담는 리스트
    max_depth = []
    for i in range(1, len(new_grid)-1) :
        for j in range(1, len(new_grid[i])-1) :
            # 현재 위치에 있는 값을 저장
            curr = new_grid[i][j]
            # print(i,j)
            # 동서남북으로 둘러보았을때, 현재 위치가 가장 깊은곳이라면 해당 위치를 max_depth에 저장
            if new_grid[i][j-1] < curr and new_grid[i][j+1] < curr and new_grid[i-1][j] < curr and new_grid[i+1][j] < curr :
                max_depth.append((i,j))
            else :
                continue
                
    # print(new_grid)

    # 저장한 위치에 'X'를 표시
    for pos in max_depth :
        new_grid[pos[0]][pos[1]] = 'X'
    
    grid = []
    # 리스트로 되었던 값들을 문자열로 변환
    for g in new_grid :
        grid.append(''.join(g))
    
    # print(grid)
    # 값 리턴
    return grid

grid = ['1112', '1912', '1892', '1234']
cavityMap(grid)