import sys

n = int(sys.stdin.readline())
for _ in range(n) :
    n, string = sys.stdin.readline().split()
    n = int(n)

    for s in string :
        for i in range(n) :
            print(s,end='')
    print()
