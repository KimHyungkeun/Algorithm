import sys

while True :
    # 문자열 입력
    string = sys.stdin.readline().rstrip()
    # END 입력시 종료
    if string == "END" :
        break

    # 거꾸로 입력을 위해 임시로 리스트로 설정
    arr = list(string)
    # 리스트 순서를 거꾸로 배치
    arr.reverse()

    # 결과 출력
    print(''.join(arr))
    
    
