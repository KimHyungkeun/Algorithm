import sys

n = int(sys.stdin.readline())
cnt = 0

for _ in range(n) :
    # 단어입력
    word = sys.stdin.readline().rstrip()
    arr = ""
    advent = {}

    for w in word :
        # arr가 비었으면 철자 w를 대입
        if not arr :
            arr = w
        
        # 다음에 오는 철자가 같은 글자이면 패스
        if arr == w :
            continue
        
        else :
            # 현재 글자의 빈도수를 advent 딕셔너리에서 조정 
            if arr in advent :
                advent[arr] += 1
            
            else :
                advent[arr] = 1
            
            # 새로운 철자를 arr에 넣음
            arr = w
    
    if arr in advent :
        advent[arr] += 1
            
    else :
        advent[arr] = 1
    
    # 그룹 단어는 해당 철자의 그룹빈도수가 1이어야한다.
    # 만약, 해당 철자의 그룹단어 빈도수가 2개 이상이면 그룹단어가 아니다
    max_val = max(advent.values())
    if max_val == 1 :
        cnt += 1

print(cnt)
    

