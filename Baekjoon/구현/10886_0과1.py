import sys

n = int(sys.stdin.readline())

# 0은 귀엽지 않다는 의견, 1은 귀엽다는 의견
cnt_0 = 0
cnt_1 = 0


for _ in range(n) :
    # n개의 설문조사를 실시하여 의견을 모은다
    result = int(sys.stdin.readline())
    if result == 0 :
        cnt_0 += 1
    else :
        cnt_1 += 1

# 0이 더 많다면 귀엽지 않다는 의견이 대다수인것이고, 1이 더 많다면 귀엽다는 의견이다
if cnt_0 > cnt_1 :
    print("Junhee is not cute!")

else :
    print("Junhee is cute!")
