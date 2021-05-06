# import sys

# a, b = list(map(int, sys.stdin.readline().split()))
# boolean = [False, False] + [True]*(b-1) # 1,2는 소수이므로 False로 지정하고 나머지는 True로 임시 셋팅한다
# primes = []

# # print(boolean)
# for i in range(2, b+1) :
#     if boolean[i] : # 해당 수가 소수일때만 prime 리스트에 추가시킨다.
#         primes.append(i)
#     for j in range(2*i, b+1, i) : # 해당 배수에 포함하는 수들은 모두 False로 만든다.
#         boolean[j] = False


# for num in primes :
#     if a <= num <= b :
#         print(num)

import sys

n,m = map(int ,sys.stdin.readline().split())
visited = [False, True] + [True] * (m-1)
prime = []

for i in range(2,m+1) :
    if visited[i] :
        visited[i] = False
        prime.append(i)
    for j in range(2*i, m+1, i) :
        visited[j] = False

for p in prime :
    if n <= p <= m :
        print(p,end=' ')


    
    



