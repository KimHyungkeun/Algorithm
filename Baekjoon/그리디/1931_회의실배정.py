import sys

# 회의 갯수 n
n = int(sys.stdin.readline())

# 회의 시간표 리스트
time_table = []
for _ in range(n) :
    # 시작시간과 끝시간을 적어 시간표에 기입
    start, end = map(int, sys.stdin.readline().split())
    time_table.append([start, end])

# 시작시간을 기준으로 오름차순 정렬 후, 끝나는 시간이 빠른것으로 한번더 오름차순 정렬
sort_by_starttime = sorted(time_table, key = lambda x : x[0])
sort_by_endtime = sorted(sort_by_starttime, key = lambda x : x[1])
# print(sort_by_starttime)
# print(sort_by_endtime)

# 사용가능한 회의의 최대갯수 카운팅
cur = sort_by_endtime[0]
cnt = 1
for i in range(len(sort_by_endtime)-1) :
    # 현 회의가 끝나는 시간 다음으로, 먼저 오게될 회의를 탐색하여 카운팅한다
    if cur[1] <= sort_by_endtime[i+1][0] :
        cur = sort_by_endtime[i+1]
        # print(cur)
        cnt += 1

print(cnt)


