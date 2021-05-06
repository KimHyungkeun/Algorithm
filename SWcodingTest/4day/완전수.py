import sys

# a,b 입력
a, b = map(int, sys.stdin.readline().split())

for i in range(a,b+1) :
    # a부터 b까지의 수 에서 완전수를 구한다
	cnt = 0
    # 본인을 제외한 나머지 약수들의 합이 본인과 같으면 완전수이다
	for j in range(1, i) :
		if i % j == 0 :
			cnt += j
	
	if cnt == i :
		print(i, end=' ')