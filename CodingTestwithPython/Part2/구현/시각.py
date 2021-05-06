import sys

# 시각을 입력
n = int(sys.stdin.readline())

cnt = 0
for hour in range(n+1) :
    for miniute in range(60) :        
        for sec in range(60) :
            # 만약 시, 분, 초에 3이 하나라도 들어간다면 횟수를 증가시킨다
            if '3' in str(sec) :
                cnt += 1
            elif '3' in str(miniute) :
                cnt += 1
            elif '3' in str(hour) :
                cnt += 1

print(cnt)

# -------------------------------------------------------------------------------------------------------

# # H를 입력받기
# h = int(input())

# count = 0
# for i in range(h + 1):
#     for j in range(60):
#         for k in range(60):
#             # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
#             if '3' in str(i) + str(j) + str(k):
#                 count += 1

# print(count)