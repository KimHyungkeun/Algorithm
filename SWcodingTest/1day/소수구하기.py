def solution(n):
    
    answer = 0


    boolean = [False, False] + [True]*(n-1) # 1,2는 소수이므로 False로 지정하고 나머지는 True로 임시 셋팅한다
    primes = []

    # 에라토스테네스의 체를 사용
    # print(boolean)
    for i in range(2, n+1) :
        if boolean[i] : # 해당 수가 소수일때만 prime 리스트에 추가시킨다.
            primes.append(i)
        for j in range(2*i, n+1, i) : # 해당 배수에 포함하는 수들은 모두 False로 만든다.
            boolean[j] = False


    for num in primes :
        if 2 <= num <= n :
            answer += 1
   
    return answer

# https://programmers.co.kr/learn/courses/30/lessons/12921