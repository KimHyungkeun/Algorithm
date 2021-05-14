# 210514 풀이
import sys

n, m = map(int, sys.stdin.readline().split())

poke_dict = {} # 도감번호 : 포켓몬 형태의 딕셔너리
poke_dict_rev = {} # 포켓몬 : 도감번호 형태의 딕셔너리

for i in range(1, n+1) :
    pokemon = sys.stdin.readline().rstrip() # 포켓몬을 도감에 입력
    poke_dict[i] = pokemon
    poke_dict_rev[pokemon] = i

for _ in range(m) :
    cmd = sys.stdin.readline().rstrip()

    # 입력값이 포켓몬 이름이면, 이름에 해당하는 포켓몬 도감 번호를 출력
    if cmd.isalpha() :
        print(poke_dict_rev[cmd])
    
    # 입력값이 도감번호라면, 도감번호에 해당하는 포켓몬 이름 출력
    else :
        cmd = int(cmd)
        print(poke_dict[cmd])



# # 포켓몬 도감 갯수 n과, 제출되는 문제수 m이 나온다
# n, m = map(int, sys.stdin.readline().split())
# poke_dict = {}

# for i in range(n) :
#     # 숫자가 키로 들어오면 포켓몬은 값으로 하는 경우와 포켓몬을 key로 하고 번호를 값으로 하는 경우를 모두 설정
#     poke_dict[i+1] = sys.stdin.readline().rstrip()
#     poke_dict[str(poke_dict[i+1])] = i+1


# for _ in range(m) :
#     answer = sys.stdin.readline().rstrip()
#     # 입력 형태가 숫자이면, 번호에 해당하는 포켓몬 이름을 출력
#     if answer.isdigit() :
#         answer = int(answer)
#         print(poke_dict[answer])
#     # 입력 형태가 포켓몬 이름이면, 포켓몬에 해당하는 번호 출력
#     else :
#         print(poke_dict[answer])
