import sys

n = int(sys.stdin.readline())

for _ in range(n) :
    # 삭제할 위치인 idx와 검사할 문자열 string을 설정한다
    idx, string = sys.stdin.readline().split()
    # 입력한 위치를 정수형으로 변환한다
    idx = int(idx)-1
    # 해당 문자열을 리스트로 설정한다
    array = list(string)
    # 입력한 위치에 있는 철자를 삭제하고, 그 뒤의 남은 결과를 문자열로 출력한다
    del array[idx]
    print(''.join(array))