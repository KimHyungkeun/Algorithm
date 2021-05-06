import sys

n = int(sys.stdin.readline())

# 집합 원소 갯수가 1개이거나 공집합이면, 접두사X 인 집합이다
if n == 0 :
    print(1)

else :
    arr = []
    # n개의 문자열을 담을 배열
    for _ in range(n) :
        arr.append(sys.stdin.readline().rstrip())

    # arr = sorted(arr, key = lambda x : len(x))
    
    # 문자열 길이를 기준으로 오름차순 정렬한다
    arr.sort(key = lambda x : len(x))
    total_cnt = 0 # 접두사X 인 문자열 갯수

    # print(arr)
    for i in range(n) :
        # 비교갯수
        cnt = 0
        for j in range(i+1, n) :
            is_cor = 0
            # print(arr[i])
            for k in range(len(arr[i])) :
                # arr[i]문자열을 기준으로, arr[j]의 접두어가 되는지 철자 하나하나를 확인해본다
                if arr[i][k] == arr[j][k] :
                    is_cor += 1
            # 만약, 접두어가 맞게된다면 접두사X 라는 조건에 맞지않으므로 다음 arr[i] 문자열을 비교한다
            if is_cor == len(arr[i]) :
                break
            # 접두어가 아니라면 카운트를 하나 증가시킨다
            else :
                cnt += 1
            
            # 만약, 카운트가 i+1에서 n 까지 모두 검사해서, 누적된 cnt와 일치하면 접두사X 문자열 갯수를 1 올린다
            if cnt == n-i-1 :
                # print(arr[i])
                total_cnt += 1

    
    print(total_cnt+1)

