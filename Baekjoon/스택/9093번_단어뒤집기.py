import sys
input=sys.stdin.readline

n = int(input())
stack = []

for i in range(n) :
    result = input()
    length = len(result.split())

    for j in range(length) :
        for k in range(len(result.split()[j])-1, -1, -1) :
            stack.append(result.split()[j][k])
        print(''.join(stack))
        stack = []

