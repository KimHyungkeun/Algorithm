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