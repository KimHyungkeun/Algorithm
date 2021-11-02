import sys

n = int(sys.stdin.readline())

for _ in range(n) :
    arr = list(map(int,sys.stdin.readline().rstrip().split()))
    avg = sum(arr[1:]) / arr[0]

    cnt = 0
    for i in range(1, len(arr)) :
        if arr[i] > avg :
            cnt += 1
    ans = (cnt / arr[0])*100
    print("{:.3f}".format(ans)+"%")