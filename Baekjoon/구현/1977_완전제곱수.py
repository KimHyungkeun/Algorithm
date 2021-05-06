import sys

# n과 m입력
n = int(sys.stdin.readline()) 
m = int(sys.stdin.readline())

summary = 0 # 완전제곱수들의 합을 담을 변수
minimum = 10000 # 완전제곱수들중 최소값을 담을 변수

for num in range(n,m+1) :
    result = num**(0.5)

    if result.is_integer() : # 만약 해당 수가 완전제곱수이면(제곱근을 씌웠을때도 정수 결과값이라면)
        summary += num # 해당 수를 누적한다(더한다)
        if num < minimum :
            minimum = num 

# 완전제곱수가 존재하지 않는다면, -1 출력
if summary == 0 :
    print(-1)

# 완전제곱수들의 합과, 그 제곱수들중 가장 최소값을 출력
else :
    print(int(summary))
    print(int(minimum))

# print(x.is_integer())