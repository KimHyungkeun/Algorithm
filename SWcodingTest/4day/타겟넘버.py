def solution(numbers, target):
    cnt = 0 # 타겟넘버를 찾을때마다 횟수를 올린다

    def dfs(num, idx) :
        nonlocal cnt
        # print(idx)

        # 배열 끝에 다다르기 전
        if idx < len(numbers) :
            # 만약 해당하는 숫자가 원하는 숫자라면 cnt를 올린다
            if idx == len(numbers)-1 and num == target :
                # print("OK")
                cnt += 1
                return None
            
            # 끝에 도달하였으나 원하는 숫자가 아니라면 바로 함수를 종료한다
            elif idx == len(numbers)-1 and num != target :
                return None

            # 해당 숫자를 시점으로 덧셈과 뺄셈을 둘다 시도해본다
            dfs(num + numbers[idx+1], idx+1)
            dfs(num - numbers[idx+1], idx+1)
        
        else :
            return None

    # 시작 숫자 또한 양수와 음수의 경우로 나누어서 시작한다
    dfs(numbers[0], 0)
    dfs(-numbers[0], 0)

    print(cnt)
    return cnt

numbers = [1,1,1,1,1]
target = 3
solution(numbers, target)