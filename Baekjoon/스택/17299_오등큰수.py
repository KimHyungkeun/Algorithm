import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


exist = {} # 숫자별 카운트를 위한 dict 자료형
answer = [-1]*n # 오등큰수를 찾지못하면 -1로 표시하므로 디폴트는 -1로 초기화한다 
stack = [] 

# 해당 수가 어느 곳에 위치에 있는지 값과 인덱스를 같이 기억한다
arr_idx = []
for i in range(n) :
    arr_idx.append([arr[i], i])

# 오등큰수는 숫자의 출현횟수를 비교하기때문에, 숫자별로 카운트를 실시하여 dict자료형으로 만든다
for num in arr :
    if num not in exist :
        exist[num] = 1
    else :
        exist[num] += 1

for i in range(len(arr_idx)) :
    
    # 스택이 비어있으면 스택을 채운다
    if not stack :
        stack.append(arr_idx[i])
    
    else :
        while stack :
            # 만약 스택의 top의 등장횟수보다 다음수의 등장횟수가 더 크다면 그 수가 바로 오등큰수가 된다
            if exist[stack[-1][0]] < exist[arr_idx[i][0]] :
                answer[stack[-1][1]] = arr_idx[i][0]
                stack.pop() # 오등큰수를 발견하게되면, 해당 수는 pop한다
            
            # 스택의 top의 수가 더 크면 루프문 탈출
            else :
                break
        # 다음에 들어올 수를 스택에 추가한다.
        stack.append(arr_idx[i])

# 출력
for ans in answer :
    print(ans, end=' ')