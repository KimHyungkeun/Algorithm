import sys

# 테스트케이스 n 입력
n = int(sys.stdin.readline())

for _ in range(n) :
    # 고려해야할 케이스 p
    p = int(sys.stdin.readline())
    name_dict = []

    # 선수의 가격과 선수 이름을 입력받고, name_dict에 저장
    for _ in range(p) :
        c, name = sys.stdin.readline().split()
        name_dict.append((int(c), name))
    
    # 선수가격을 기준으로 내림차순 정렬 후, 가장 비싼 선수의 이름을 출력
    name_dict.sort(key = lambda x : x[0], reverse=True)
    print(name_dict[0][1])