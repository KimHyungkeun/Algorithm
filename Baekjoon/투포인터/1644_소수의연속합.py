import sys
# import time
import math

# 소수 판별 함수(에라토스테네스의 체)
def is_prime_number(n):
    # 2부터 n까지의 모든 수에 대하여 소수 판별
    array = [True for i in range(n+1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)

    # 에라토스테네스의 체
    for i in range(2, int(math.sqrt(n)) + 1): #2부터 n의 제곱근까지의 모든 수를 확인하며
        if array[i] == True: # i가 소수인 경우(남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    return [ i for i in range(2, n+1) if array[i] ]
# N이 1,000,000 이내로 주어지는 경우 활용할 것 => 이론상 400만번 정도 연산이고 메모리도 충분함


n = int(sys.stdin.readline())

if n == 1 : # n이 1이면 아예 해당되는 경우 없으므로 0 출력
    print(0)

else :
    # start = time.time()
    prime = is_prime_number(n) # n까지의 모든 소수를 구함

    # left right prime 총 길이를 설정
    left = 0
    right = 0
    length = len(prime)

    total = prime[0] # 맨 첫번째 부터 시작함

    cnt = 0
    while left < length and right < length :
        if total < n : # 총합이 n보다 작으면 right를 옮김
            right += 1
            if right == length : # 만약 탐색 범위를 벗어나면 루프문 탈출
                break
            total += prime[right] # 해당 영역내의 부분합 갱신
        
        elif total > n : # 총합이 n보다 크면 left를 옮김
            total -= prime[left] # left가 변함으로써, 영역 밖의 값에 대해서는 차감을 한다
            left += 1 # left 옮김
        
        else :
            cnt += 1 # 맞는 합을 찾았으므로 cnt를 증가
            right += 1 # 다시 right를 옮김
            if right == length : # 만약 탐색 범위를 벗어나면 루프문 탈출
                break
            total += prime[right] # 해당 영역내의 부분합 갱신

    print(cnt)
    # print("time :", time.time() - start) 



# https://www.acmicpc.net/board/view/22085 : 문제 조건 재확인
# https://velog.io/@koyo/python-is-prime-number : 에라토스테네스의 체 더육 빠른 효율로