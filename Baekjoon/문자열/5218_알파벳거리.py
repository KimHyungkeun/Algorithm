import sys

n = int(sys.stdin.readline())

for _ in range(n) :
    # 문자열을 입력받는다
    string = sys.stdin.readline()
    # 문자열을 공백 기준으로 구분하고, 구분된 문자열의 길이를 구한다
    tmp = string.split()
    length = len(tmp[0])

    distance = []
    for i in range(length) :
        # 만약 후자쪽 문자열의 철자가 더 크다면, 그 철자에서 전자쪽 문자열의 철자를 빼고
        if ord(tmp[0][i]) <= ord(tmp[1][i]) :           
            distance.append(abs(ord(tmp[0][i])-ord(tmp[1][i])))
        # 그 반대의 경우라면, 후자쪽 문자열의 철자에 26을 더하고, 전자쪽 문자열의 철자를 뺀다
        else :
            distance.append(abs(ord(tmp[1][i]) + 26 - ord(tmp[0][i])))
    print("Distances:", *distance)