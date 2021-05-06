# def fibonacci(n, count_zero, count_one) :

#     print("count_zero : ", count_zero)
#     print("count_one : ", count_one)

#     if n == 0 :
#         count_zero += 1
#         return 0, count_zero, count_one
    
#     elif n == 1 :
#         count_one += 1
#         return 1, count_zero, count_one
    
#     else :
#         return fibonacci(n-1,count_zero,count_one) + fibonacci(n-2,count_zero,count_one), count_zero, count_one

# n = int(input())

# for _ in range(n) :
#     num = int(input())
#     count_zero = 0
#     count_one = 0

#     result, zero, one = fibonacci(num, count_zero, count_one)
#     print(zero, one)

# -------------------------------------------------------------------------

import sys

def count_fibo(n) :
    arr = [1,0] # 각각 0의 갯수와 1의 갯수
    new_arr0 = arr[1] # 새 0의 개수는 이전 테스트케이스의 1의 개수와 같음
    new_arr1 = arr[0] + arr[1] # 새 1의 개수는 이전 테스트케이스의 0의개수+1의개수와 같음
    
    for _ in range(1,n+1) :
        arr[0] = new_arr0 # 새로운 개수 입력
        arr[1] = new_arr1 
        
        new_arr0 = arr[1] # 사전에 미리 갯수를 계산해놓음
        new_arr1 = arr[0] + arr[1]

    return arr 

# 갯수 입력
num = int(sys.stdin.readline())

for _ in range(num) :
    n = int(sys.stdin.readline()) # 피보나치 테스트케이스 입력
    result = count_fibo(n) 
    print(result[0], result[1]) # 각각 0의 개수, 1의 개수를 구함 