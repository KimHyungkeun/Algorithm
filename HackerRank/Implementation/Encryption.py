# Complete the encryption function below.
def encryption(s):
    # 해당 문자열의 제곱길이를 구하고, 가우스 범위로 나타낸다
    L = len(s)**0.5
    # floor <= L < ceil
    ceil = int(L)+1  
    floor = int(L)  
    
    # floor와 ceil의 곱이, 문자열 본래길이 미만이라면 아래와 같이 테이블 생성
    if floor*ceil < len(s) :
        board = [['0'] * ceil for _ in range(ceil)]
        floor = ceil # floor 값 또한 ceil과 같게함
    
    # floor 제곱이, 문자열 본래 길이와 같다면 아래와 같이 테이블 생성
    elif floor**2 == len(s) :
        board = [['0'] * floor for _ in range(floor)]
        ceil = floor # ceil값 또한 floor와 같게 함
    
    # 그 외의 경우는 아래와 같이 처리(보통의 경우)
    else :
        board = [['0'] * ceil for _ in range(floor)]


    i = 0
    j = 0
    for w in s :
        # 생성한 테이블에 값을 집어넣음
        board[i][j] = w
        j += 1
        # 해당 행의 처리가 끝났다면, 다음 행으로 넘어감
        if j == ceil :
            i += 1
            j = 0
    
    result = []
    for i in range(ceil) :
        # 해당 테이블을 컬럼을 기준으로 문자열을 합친다.
        tmp = ""
        for j in range(floor) :
            # '0'을 만나면, 해당 컬럼의 문자열 병합을 마치고 다음 컬럼으로 넘어간다
            if board[j][i] != '0' :
                tmp += board[j][i]
            else :
                break
        result.append(tmp)
    
    # 문자열을 이어붙인다
    answer = ""
    for r in result :
        answer += (r+' ')
        
    
    print(answer)
    return answer

# s = "ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots"
# s = "haveaniceday"
# s = "chillout"
s = "iffactsdontfittotheorychangethefacts"
encryption(s)