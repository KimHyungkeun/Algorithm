import sys

t = int(sys.stdin.readline())

for _ in range(t) :
    # 시즌제 쿠폰 n개, 일반쿠폰 m개
    n, m = map(int, sys.stdin.readline().split())

    # k를 5로 나누어서 최소한의 5개 이상의 시즌제 쿠폰을 마련한다
    k1 = n // 5
    # 시즌제 + 일반 쿠폰의 갯수가 12의 배수여야한다
    k2 = (m+n) // 12

    # 시즌제가 일반쿠폰보다 적다면 시즌제쿠폰으로 비교
    if k1 < k2 :
        k = k1
    else :
        k = k2

    
    while n+m < 12*k :
        if k == 0 :
            break
        k -= 1
    
    print(k)

# https://level.goorm.io/exam/47878/%EC%82%AC%EC%9D%80%ED%92%88-%EA%B5%90%ED%99%98%ED%95%98%EA%B8%B0/quiz/1
    


