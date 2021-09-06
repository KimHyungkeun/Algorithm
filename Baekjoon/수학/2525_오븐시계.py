import sys

hour, minute = map(int, sys.stdin.readline().split())
add_min = int(sys.stdin.readline())

total_time = (hour * 60)  + minute + add_min

after_hour = (total_time // 60) % 24
after_min = total_time % 60

print(after_hour, after_min)