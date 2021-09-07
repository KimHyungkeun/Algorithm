import sys

# 테스트케이스 입력
t = int(sys.stdin.readline())

for _ in range(t) :
    # 대학 갯수 입력
    n = int(sys.stdin.readline())
    university = []

    for i in range(n) :
        # 대학 이름과 술 주량을 입력
        s, l = sys.stdin.readline().split()
        university.append((s,int(l)))
    
    # 주량을 기준으로 내림차순 정렬
    university.sort(key=lambda x : x[1], reverse=True)

    # 가장 많이 마시는 대학의 이름 출력
    print(university[0][0])
    