# 210516 재도전, 아직도 제대로 이해하지 못함
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

seat = [0] * n
for i in range(1, n+1) :
    idx = arr[i-1]
    cnt = 0

    for j in range(n) :
        if cnt == idx and seat[j] == 0 :
            seat[j] = i
            break
        elif seat[j] == 0 :
            cnt += 1 
    # print(seat)

print(*seat)





# import sys

# # 인원 수와, 각 인원이 기억하고 있는 왼쪽에 있었던 본인보다 키큰 사람
# n = int(sys.stdin.readline())
# array = list(map(int, sys.stdin.readline().split()))

# # 실제 서로 서있어야하는 위치
# ans = [0] * n

# for i in range(1, n+1) :
#     tmp = array[i-1]
#     cnt = 0
#     # print(tmp)
#     # 만약 해당 자리가 비어있고, 본인이 기억하는 키큰사람의 수가 맞다면 그 자리에 배치한다
#     for j in range(n) :
#         if cnt == tmp and ans[j] == 0 :
#             ans[j] = i
#             break
#         elif ans[j] == 0 :
#             cnt += 1
        
#         else :
#             continue
        
#         # print(ans, i)

# # 배열 내의 요소들을 출력
# print(*ans)

# https://suri78.tistory.com/205