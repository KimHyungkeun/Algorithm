import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n) :
    # O,X 등의 결과
    result = sys.stdin.readline().rstrip()
    arr.append(result)

for a in arr :
    total = 0
    plus = 1 # 연속 정답일 경우의 추가 점수
    tmp = []
    for i in range(len(a)) :
        # 만약 'O'이면 추가점수 획득
        if a[i] == 'O' :
            tmp.append(plus)
            plus += 1
        
        # 그렇지 않다면, 0점추가 및 추가점수없음
        else :          
            if not tmp :
                total += 0
            else :
                total += sum(tmp)
            tmp = []
            plus = 1
        
    
    if tmp :
        total += sum(tmp)

    
    print(total)
