import sys

total_time = sys.stdin.readline().rstrip()
play_time = sys.stdin.readline().rstrip()

total_time = total_time.split(":") # 시간을 :를 기준으로 쪼갠다
play_time = play_time.split(":") 

# print(total_time, play_time)

# 시간을 분으로 환산시킨다
total_min = int(total_time[0]) * 60 + int(total_time[1])
# print(total_min)
play_min = int(play_time[0]) * 60 + int(play_time[1])
# print(play_min)

if total_min > play_min :
		print(0)
	
else :
	if play_min - total_min >= 10 :
		print(0)
	
	else :
		print(1)