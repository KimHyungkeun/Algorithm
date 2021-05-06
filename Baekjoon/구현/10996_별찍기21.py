import sys

n = int(sys.stdin.readline())

# 별 1개일 경우
if n == 1 :
    print("*")

else :
    # 별 여러개일 경우 n*2개의 별찍기를 i번 진행한다
    for i in range(n) :

        for j in range(2) :
            for k in range(n) :
                # 만약 0번째 j인 경우
                if j == 0 :
                    # 짝수번째 인덱스일때 별을 찍고
                    if k % 2 == 0 :
                        print("*", end='')
                    # 홀수번째에서는 공백을 넣는다
                    else :
                        print(" ",end='')
                # 만약 1번째 j인 경우
                else :
                    # 홀수 번째 인덱스일때 별을 찍고
                    if k % 2 == 1 :
                        print("*", end='')
                    else :
                        # 마지막 인덱스에서는 어떤 글자도 찍지않고 출력을 종료한다
                        if k == n-1 :
                            break
                        # 그 외의경우는 공백을 출력한다
                        else :
                            print(" ",end='')
            print()
                
                
                