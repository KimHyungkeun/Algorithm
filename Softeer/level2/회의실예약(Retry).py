import sys
from collections import deque
time_table = {i:set([]) for i in range(9,19)}
car_type = []
n, m = map(int, sys.stdin.readline().split())

for _ in range(n) :
    car = sys.stdin.readline().rstrip()
    car_type.append(car)
car_type.sort()

for _ in range(m) :
    car, start, end = sys.stdin.readline().split()
    for time in range(int(start), int(end)+1) :
        time_table[time].add(car)

for c in car_type :
    print("Room " + c + ":")
    all_case = []
    possible = deque()
    for time in time_table.keys() :
        if c not in time_table[time] :
            possible.append(time)
        else :
            if possible :
                if possible[0] > 9 :
                    possible.appendleft(possible[0]-1)
                if possible[-1] < 18 :
                    possible.append(possible[-1]+1)

                start = str(possible[0])
                end = str(possible[-1])
                if start == "9" :
                    start = "09"
                log = start + "-" + end
                all_case.append(log)
                possible.clear()

    if possible :
            if possible[0] > 9 :
                possible.appendleft(possible[0]-1)
            if possible[-1] < 18 :
                possible.append(possible[-1]+1)

            start = str(possible[0])
            end = str(possible[-1])
            if start == "9" :
                start = "09"
            log = start + "-" + end
            all_case.append(log)
            possible.clear()
    
    if not all_case :
        print("Not available")
    else :
        print(str(len(all_case)) + " available:")
        for l in all_case :
            print(l)

    if car_type.index(c) != len(car_type)-1 :
        print("-----")
# ------------------------------------------------------------------
# 220102 재풀이
import sys
from collections import deque
room_type = []
time_table = {}
n, m = map(int, sys.stdin.readline().split())

for _ in range(n) :
    room = sys.stdin.readline().rstrip()
    time_table[room] = [0] * 18

for _ in range(m) :
    room, start, end = sys.stdin.readline().split()
    start = int(start)
    end = int(end)
    for i in range(start, end) :
        time_table[room][i] = 1

time_table = sorted(time_table.items(), key = lambda x : x[0])

idx = 0
for room, time in time_table :
    print("Room " + room + ":")
    possible = []

    tmp = [] 
    for i in range(9,18) :
        if time[i] == 0 :
            tmp.append(i)
        else :
            if tmp :        
                tmp.append(tmp[-1]+1)
                possible.append(tmp)
                tmp = []
    if tmp :
        tmp.append(tmp[-1]+1)
        possible.append(tmp)
        tmp = []

    if not possible :
        print("Not available")
    else :
        print(str(len(possible)) + " available:")
        log = ""
        for p in possible :
            if p[0] == 9 :
                start = "09"
            else :
                start = str(p[0])
            end = str(p[-1])
            log = start + "-" + end
            print(log)
    
    idx += 1
    if idx != len(time_table) :
        print("-----")