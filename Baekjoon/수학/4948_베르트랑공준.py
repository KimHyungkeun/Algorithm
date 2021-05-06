import sys

b = 123456*2

boolean = [False, False] + [True]*(b-1) # 1,2는 소수이므로 False로 지정하고 나머지는 True로 임시 셋팅한다
primes = []


# print(boolean)
for i in range(2, b+1) :
    if boolean[i] : # 해당 수가 소수일때만 prime 리스트에 추가시킨다.
        primes.append(i)
    for j in range(2*i, b+1, i) : # 해당 배수에 포함하는 수들은 모두 False로 만든다.
        boolean[j] = False

while True :
   
    n = int(sys.stdin.readline())

    if n == 0 : # n입력시 종료
        break
    
    count = 0
    for num in primes :
        if n < num <= 2*n : # 소수인 수들만 판별하여 카운트 증가
            count += 1

    print(count) # 횟수 출력





    

    
        