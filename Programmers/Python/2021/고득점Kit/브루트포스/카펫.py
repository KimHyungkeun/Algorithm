def solution(brown, yellow):

    total = brown + yellow # 전체 카펫의 넓이
    divisor = [] # yellow의 약수를 담기위한 리스트
    for n in range(1, yellow+1) : 
        if yellow % n == 0 : # yellow의 약수를 담음
            divisor.append(n)

    mid = len(divisor) // 2 # yellow의 약수의 중간지점
    end = len(divisor)-1 # yellow의 약수의 끝지점

    for i in range(mid+1) :
        # yellow의 가로+2, 세로+2를 하면 전체 카펫의 가로, 세로와 일치한다
        if (divisor[end-i] + 2) * (divisor[i] + 2) == total :
            answer = [divisor[end-i]+2, divisor[i]+2]
            break

    print(answer)
    return answer

brown = 24
yellow = 24
solution(brown, yellow)