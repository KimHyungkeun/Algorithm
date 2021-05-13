def solution(num):
    cnt = 0

    # num이 1이 될때까지 아래 연산을 반복
    while num != 1 :
         # 만일 횟수가 500번 이상인데도 1이 나오지 않으면 -1을 리턴
        if cnt >= 500 :
            cnt = -1
            break

        # num이 짝수이면 2로 나눈다
        if num % 2 == 0:
            num //= 2
        
        # num이 홀수이면 3을 곱하고 1을 더한다
        else :
            num *= 3
            num += 1
        
        # 횟수를 증가시킨다
        cnt += 1
        
       
    return cnt