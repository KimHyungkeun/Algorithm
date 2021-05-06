import sys

# 포켓몬 도감 갯수 n과, 제출되는 문제수 m이 나온다
n, m = map(int, sys.stdin.readline().split())
poke_dict = {}

for i in range(n) :
    # 숫자가 키로 들어오면 포켓몬은 값으로 하는 경우와 포켓몬을 key로 하고 번호를 값으로 하는 경우를 모두 설정
    poke_dict[i+1] = sys.stdin.readline().rstrip()
    poke_dict[str(poke_dict[i+1])] = i+1


for _ in range(m) :
    answer = sys.stdin.readline().rstrip()
    # 입력 형태가 숫자이면, 번호에 해당하는 포켓몬 이름을 출력
    if answer.isdigit() :
        answer = int(answer)
        print(poke_dict[answer])
    # 입력 형태가 포켓몬 이름이면, 포켓몬에 해당하는 번호 출력
    else :
        print(poke_dict[answer])
