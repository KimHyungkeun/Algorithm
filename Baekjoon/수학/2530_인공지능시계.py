import sys

# 시, 분, 초를 입력하고 추가 add_sec 시간을 입력
h, m, s = map(int, sys.stdin.readline().split())
add_sec = int(sys.stdin.readline())

# 시,분,초를 초단위로 통합
total_time = h * 3600 + m * 60 + s + add_sec

# add_sec를 추가한 후의 시,분,초를 구함
after_hour = (total_time // 3600) 
after_min = (total_time - (after_hour * 3600)) // 60
after_sec = total_time - (after_hour * 3600) - (after_min * 60)

print(after_hour % 24, after_min, after_sec)