def solution(n):
    answer = []

    # 나올 수 있는 나머지의 경우 (3진법을 베이스로 생각하되, 나머지가 0인값은 4로 대체한다고 생각)
    mod = [4,1,2]

    while n :
        # print(n)
        m = n % 3 # 나머지 값
        n = n // 3 # 몫
        answer.append(str(mod[m]))  # 자릿수를 하나씩 이어나감
        if not m : # 만약 n이 3으로 나누어떨어진다면 n을 1 뺀다
            n -= 1
    
    # answer를 역순으로 배치
    answer.reverse()
    # 리스트 내용을 문자열로 바꾼다
    answer = ''.join(answer)

    print(answer)
    return answer

n = 26
solution(n)

## https://itholic.github.io/kata-124-world/