import sys

# 테스트케이스 n개 입력
n = int(sys.stdin.readline())
first_cmd = input() # 첫번째 명령어를 입력(기준이 되는 첫번째 명령어)
alphabet_count = [1] * len(first_cmd) # 각 자리의 알파벳의 등장횟수를 적어놓는다


# 명령어를 차례대로 모두 입력
cmd_total = []
for _ in range(n-1) :
    cmd = input()
    cmd_total.append(cmd)

for w in range(len(first_cmd)) :
    count = 0
    # 만약 입력했던 모든 명령어에 대하여, w번째 철자가 모두 갖다면 alphabet_count의 w번째 갯수를 더욱 증가시킨다
    for j in range(len(cmd_total)) :
        if first_cmd[w] == cmd_total[j][w] :
            count += 1
    alphabet_count[w] += count

# print(alphabet_count)

for i in range(len(alphabet_count)) :
    # i번째 철자의 등장횟수가 테스트케이스 n개와 같다면 철자를 그대로 출력하고, 다르다면 "?"로 출력한다.
    if alphabet_count[i] == n :
        print(first_cmd[i],end='')
    else :
        print("?",end='')
        

