n = int(input())

for _ in range(n) :
    calender = list(map(int, input().split()))

    M = calender[0]
    N = calender[1]
    x = calender[2] - 1 # 0부터 셈을 하기위해 -1을 한다
    y = calender[3] - 1 # 0부터 셈을 하기위해 -1을 한다
    answer = -1

    for i in range(x, M*N+1, M) : # 해당하는 x값이 나오는 경우에 대해서만 따진다
        if i % N == y : #만약 i를 N으로 나누었을때 나머지값이 y가 나오게 될경우
            answer = i + 1 # 해당 값이 답이된다. (0부터 count했기때문에, 값이 나온 후 +1을 함)
            break

    print(answer)
    
# 참고 https://hjp845.tistory.com/126

    