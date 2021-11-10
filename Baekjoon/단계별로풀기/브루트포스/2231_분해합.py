import sys

n = int(sys.stdin.readline())

for i in range(1, 1000001) :
    num_str = str(i)
    total = 0
    for s in num_str :
        total += int(s)
    total += i
    
    # i의 분해합이 n일 경우
    if total == n :
        print(i)
        break

    # 어떠한 생성자도 찾지 못했다면 0을 출력
    if i == n :
        print(0)
        break