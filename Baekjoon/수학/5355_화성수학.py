import sys

# 테스트 횟수 입력
n = int(sys.stdin.readline())

for _ in range(n) :
    # 숫자 및 연산부호 입력
    arr = list(sys.stdin.readline().split())
    total = 0.0
    for a in arr :
        # '@'는 3을 곱함
        if a == '@' :
            total *= 3

        # '%'는 5를 더함
        elif a == '%' :
            total += 5
        
        # '#'은 7을 뺌
        elif a == '#' :
            total -= 7

        # 그 외의 숫자들은 그대로 더함
        else :
            total += float(a)

    print(format("%.2f" % total)) 