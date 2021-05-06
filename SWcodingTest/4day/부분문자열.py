import sys

# 문자열 입력
string = sys.stdin.readline().rstrip()

# i번째 문자까지 처음부터 증가하는 순서대로 출력
for i in range(1, len(string)+1) :
	print(string[:i])