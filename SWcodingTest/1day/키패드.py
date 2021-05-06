def solution(numbers, hand):
    
    answer = ""
    # 키패드를 구성한다. *, #은 임의로 11,12로 설정하였다 
    keypad = [[1,2,3],[4,5,6],[7,8,9],[11,0,12]]
    
    L = [1,4,7] # 왼손 패드
    R = [3,6,9] # 오른손 패드
    C = [2,5,8,0] # 가운데 패드
    
    L_pos = [3,0] # 왼손 위치
    R_pos = [3,2] # 오른손 위치
    
    # 해당 번호의 위치를 반환하는 함수
    def search (num) :
        for i in range(len(keypad)) :
            for j in range(len(keypad[i])) :
                if num == keypad[i][j] :
                    return i,j
                
    for num in numbers :
        # 왼손 패드에 해당한다면, 해당 위치로 인덱스 옮김
        if num in L :
            answer += 'L'
            for i in range(4) :
                if keypad[i][0] == num :
                    L_pos = [i,0]
                    break
             
        # 오른손 패드에 해당한다면, 해당 위치로 인덱스 옮김
        elif num in R :
            answer += 'R'
            for i in range(4) :
                if keypad[i][2] == num :
                    R_pos = [i,2]
                    break
        # 만약 가운데 패드의 순서라면 오른손 패드와 왼손 패드와의 거리를 비교한다 (이동해야하는 인덱스 수가 적을수록 가까운것이다)
        elif num in C :
            x,y = search(num)
            L_range = abs(x-L_pos[0]) + abs(y-L_pos[1])
            R_range = abs(x-R_pos[0]) + abs(y-R_pos[1])

            # 오른손과 더 가깝다면 오른손을 옮김
            if L_range > R_range :
                R_pos = [x,y]
                answer += 'R'
            
            # 왼손이 더 가깝다면 왼손을 옮김
            elif L_range < R_range :
                L_pos = [x,y]
                answer += 'L'
            
            # 오른손 왼손 모두 같은거리라면, 왼손잡이 오른손잡이에 따라 결정한다
            else :
                if hand == 'right' :
                    R_pos = [x,y]
                    answer += 'R'
                else :
                    L_pos = [x,y]
                    answer += 'L'
            
            
    return answer




# https://programmers.co.kr/learn/courses/30/lessons/67256