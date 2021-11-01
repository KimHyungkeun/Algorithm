import sys

# n = sys.stdin.readline().rstrip()
# start = n
# arr = [0,0]

# round = 0
# while True :
#     if round == 0 and len(n) == 1 :
#         print(round+1)
#         break
    
#     if round == 0 :
#         arr[0] = int(n[0])
#         arr[1] = int(n[1])
#         n = str(int(n[0]) + int(n[1]))
            
         
#     else :
#         if len(n) == 1 :
#             backup = int(n[0])
#             n = str(arr[1]) + n[0]

#             arr[0] = int(n[0])
#             arr[1] = int(n[1])

#         else :
            
#             n = str(arr[0] + arr[1])
#             backup = int(n[-1])

#             arr[0] = arr[1]
#             arr[1] = backup

            
    
#     # print(n)
#     if int(str(arr[0])+str(arr[1])) == int(start) and round > 0:
#         print(round)
#         break
    
#     round += 1


n = int(sys.stdin.readline())
cnt = 0
start = n

while True :
    num1 = n // 10
    num2 = n % 10
    total = num1 + num2

    cnt += 1
    n = int(str(num2) + str(total)[-1])

    if n == start :
        print(cnt)
        break

# 참고 : https://somjang.tistory.com/entry/BaekJoon-1110%EB%B2%88-%EB%8D%94%ED%95%98%EA%B8%B0-%EC%82%AC%EC%9D%B4%ED%81%B4-Python





