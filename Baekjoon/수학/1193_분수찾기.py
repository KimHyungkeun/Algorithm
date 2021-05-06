import sys

n = int(sys.stdin.readline()) # n번째 분수를 구하려 한다

# 분자 또는 분모의 최대수가, 나타낼 수 있는 경우의 수다
summary_end = 0 
summary_start = 0  

for i in range(1, n+1) :
    summary_end += i # 1부터 n까지 계속 더한다
    if n <= summary_end : # 만약 최대 누적합 갯수가 n보다 크거나 같으면
        summary_start = summary_end - i # 바로 이전 누적합 갯수를 count할때의 시작점으로 설정한다
        break

# print(summary_start)
diff = n - summary_start - 1 # 시작점부터 n번째까지의 차이를 구한다

# 지그재그 순서대로 count를 하므로, i가 홀수이냐 짝수이냐에 따라 분자, 분모를 설정하는 경우가 달라진다.
if i % 2 == 0 :
    son = 1 + diff
    mom = i - diff
else :
    son = i - diff
    mom = 1 + diff

print(str(son)+'/'+str(mom))