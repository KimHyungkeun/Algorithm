import sys

# 테스트케이스를 지정
t = int(sys.stdin.readline())

for _ in range(t) :
    cases = [1,2,4] # 1,2,3으로 1을 나타내는 경우의 수/ 2를 나타내는 경우의수/ 3을 나타내는 경우의수
    num = int(sys.stdin.readline())
    idx = num - 1

    # 인덱스가 2 이하 (즉, 입력된 숫자가 3이하) 이면 해당 인덱스에 해당하는 수를 출력
    if idx <= 2 :
        print(cases[idx])
    
    else :
        add = num - len(cases)
        cases = cases + [0]*add #현재 케이스에서 add 만큼 배열크기를 더 늘린다
        # i번째의 경우의 수는 i-3, i-2, i-1 번째 경우의수들을 모두 더한 값이다
        for i in range(3, num) :
            cases[i] = cases[i-3] + cases[i-2] + cases[i-1]
        print(cases[idx]) 
        