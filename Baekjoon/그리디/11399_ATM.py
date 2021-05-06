n = int(input())

waiting = list(map(int, input().split())) # 각 대기인원별, 경과되는 시간
waiting.sort() # 적게걸리는 순서대로 정렬

elapsed_time = 0 # 누적되는 경과시간
total_time = 0 # 각 사람별 누적경과시간들을 모두 더하여 저장하는 변수

for i in range(n) :
    elapsed_time += waiting[i] # i번째 사람일때, 누적되었던 경과시간
    total_time += elapsed_time # 해당 경과시간을 total_time에 누적

print(total_time)
