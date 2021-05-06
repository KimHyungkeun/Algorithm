import sys

odd = []
for _ in range(7) :
    n = int(sys.stdin.readline()) # 숫자입력
    if n % 2 != 0 :
        odd.append(n) # 홀수이면 odd리스트에 담는다

if len(odd) > 1 :
    odd.sort() # 홀수가 2개 이상있을때면 오름차순 정렬을 한다 

if not odd : # 홀수가 없으면 -1 출력
    print(-1)
else : # 모든 홀수들의 합과, 홀수들중 최소값 출력
    print(sum(odd))
    print(odd[0])