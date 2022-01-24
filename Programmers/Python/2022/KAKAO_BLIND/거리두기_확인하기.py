def bfs(x, y, places) :
    dx = [0,0,1,-1,1,1,-1,-1]
    dy = [1,-1,0,0,1,-1,1,-1]
    
    for i in range(8) :
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx <= -1 or nx >= 5 or ny <= -1 or ny >= 5 :
            continue
            
        if i < 4 and places[nx][ny] == 'P':
            return False
        
        if i < 4 and places[nx][ny] == 'O' :
            if dx[i] == 1 and dy[i] == 0 and nx + 1 < 5 :
                if places[nx+1][ny] == 'P' :
                    return False
            if dx[i] == -1 and dy[i] == 0 and nx - 1 >= 0 : 
                if places[nx-1][ny] == 'P' :
                    return False
            if dx[i] == 0 and dy[i] == 1 and ny + 1 < 5 : 
                if places[nx][ny+1] == 'P' :
                    return False
            if dx[i] == 0 and dy[i] == -1 and ny - 1 >= 0 : 
                if places[nx][ny-1] == 'P' :
                    return False

        
        if i >= 4 and places[nx][ny] == 'P':
            if dx[i] == 1 and dy[i] == 1 and x + 1 < 5 and y + 1 < 5 :
                if places[x+1][y] == 'O' or places[x][y+1] == 'O' :
                    return False
            if dx[i] == 1 and dy[i] == -1 and x + 1 < 5 and y - 1 >= 0 :
                if places[x+1][y] == 'O' or places[x][y-1] == 'O' :
                    return False
            if dx[i] == -1 and dy[i] == 1 and x - 1 >= 0 and y + 1 < 5 :
                if places[x-1][y] == 'O' or places[x][y+1] == 'O' :
                    return False
            if dx[i] == -1 and dy[i] == -1 and x - 1 >= 0 and y - 1 >= 0 :
                if places[x-1][y] == 'O' or places[x][y-1] == 'O' :
                    return False
     
    return True
            
def search(places) :

    for i in range(len(places)) :
        for j in range(len(places[i])) :
            if places[i][j] == 'P' :
                if not bfs(i,j,places) :
                    return False
    return True

def solution(places):
    answer = []
    
    for i in range(len(places)) :
        if search(places[i]) :
            answer.append(1)
        else :
            answer.append(0)
            
    return answer