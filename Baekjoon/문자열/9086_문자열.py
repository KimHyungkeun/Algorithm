import sys

n = int(sys.stdin.readline())

for _ in range(n) :
    # 문자열을 입력받아서, 해당 문자열의 맨처음과 맨끝의 철자를 출력
    string = sys.stdin.readline().rstrip()
    print(string[0]+string[-1])