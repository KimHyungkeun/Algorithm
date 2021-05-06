import sys

# 테스트케이스 n 입력
n = int(sys.stdin.readline())

result = {}
# 이름과 성적을 입력하고, result 딕셔너리에 추가
for _ in range(n) :
    name, score = sys.stdin.readline().split()
    score = int(score)
    result[name] = score

# 성적순대로 오름차순 정렬
down_sort = sorted(result, key = lambda x : x[1])
 
# 출력
for name in down_sort :
    print(name, end=' ')
