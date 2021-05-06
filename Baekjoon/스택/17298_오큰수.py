import sys

# n개의 수를 입력
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# 해당 수가 어느 곳에 위치에 있는지 값과 인덱스를 같이 기억한다
arr_idx = []
for i in range(n) :
    arr_idx.append([arr[i], i])

# 오큰수가 없으면 -1로 표현해야하므로, 디폴트로 모두 -1개로 표현한다
answer = [-1]*n
stack = []

for i in range(len(arr_idx)) :
    # 스택이 비어있으면 스택을 채운다
    if not stack :
        stack.append(arr_idx[i])
    
    else :
        while stack :
            # 만약 스택의 top보다 다음에 들어올 수가 더 크다면 그 수가 바로 오큰수가 된다
            if stack[-1][0] < arr_idx[i][0] :
                answer[stack[-1][1]] = arr_idx[i][0]
                stack.pop() # 오큰수를 발견하게되면, 해당 수는 pop한다
            
            # 스택의 top이 더 크면 루프문 탈출
            else :
                break
        # 다음에 들어올 수를 스택에 추가한다.
        stack.append(arr_idx[i])

# 출력
for ans in answer :
    print(ans, end=' ')


