import sys

# 집 갯수 n 입력
n = int(sys.stdin.readline())

# 한 집에 색을 칠하는데에 있어 드는 RGB 각각의 비용
RGB = []
for i in range(n) :
    color = list(map(int,sys.stdin.readline().split()))
    RGB.append(color)

# 이전 색깔과 다음 색깔이 서로 다르도록 색칠해야한다. (이전 집에 R을 칠했다면, 다음 집에는 G,B를 칠해야한다)
for i in range(1, n) :
    RGB[i][0] = min(RGB[i-1][1], RGB[i-1][2]) + RGB[i][0]
    RGB[i][1] = min(RGB[i-1][0], RGB[i-1][2]) + RGB[i][1]
    RGB[i][2] = min(RGB[i-1][0], RGB[i-1][1]) + RGB[i][2]
    print(RGB)

print(min(RGB[n-1]))

# 참고 : https://namhandong.tistory.com/131
# total = 0
# for i in range(len(RGB)) :
#     if not DP :
#         minimum = min(RGB[i])
#         DP.append((minimum, RGB[i].index(minimum)))
        
#     else :
#         RGB[i][DP[-1][1]] = 1000000
#         minimum = min(RGB[i])
#         DP.append((minimum, RGB[i].index(minimum)))

#     total += minimum
# print(total)  



# print(DP)
# print(RGB)
