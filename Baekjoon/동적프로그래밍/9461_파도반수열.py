import sys

# 테스트 케이스 갯수
test_case = int(sys.stdin.readline())

# 파도반 수열 목록 (1 <= N <= 100)
a = [1,1,1,2,2,3] + [0]*100

# 테스트 케이스 수만큼 작동
for _ in range(test_case) :
    n = int(sys.stdin.readline())
    idx = n-1 # 인덱싱을 위해 -1 해준다
 
    if idx > 5 :
        for i in range(6, idx+1) : # 6번째 인덱스부터 하여, idx까지 파도반 수열에 맞는 수 입력
            if a[i] != 0 :
                continue
            a[i] = a[i-5] + a[i-1]
            a[i+1] = a[i] + a[i-4]

    # 정답출력
    print(a[idx])

