import sys

# 사원들의 출퇴근 상태를 기록한 리스트
visit_state = []
# 사원들의 출퇴근 여부에따라 True, False로 판별
visit_dict = {}

# 방문 출입 횟수 n
n = int(sys.stdin.readline())

# 방문 출입을 총 n번 실행한다
for i in range(n) :
    # 이름과 방문 상태여부 확인
    name, state = sys.stdin.readline().split()
    # 사원 이름과 출퇴근 여부를 입력
    visit_state.append((name,state))
    # 사원들의 실제 출퇴근 상태를 나타내는 dict
    if name not in visit_dict :
        visit_dict[name] = False        

for i in range(len(visit_state)) :
    # enter이면 출근이고 leave라면 퇴근이다
    if visit_state[i][1] == 'enter' :
        visit_dict[visit_state[i][0]] = True
    else :
        visit_dict[visit_state[i][0]] = False


# 회사에 남은 사람들의 이름을 사전 역순으로 정렬
sort_state = sorted(visit_dict.items(), reverse=True)

# 출력
for i in range(len(sort_state)) :
    if sort_state[i][1] :
        print(sort_state[i][0])
