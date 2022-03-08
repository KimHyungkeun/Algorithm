# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
import sys
n, m = map(int, sys.stdin.readline().split())

arr = []
for _ in range(n) :
    word = sys.stdin.readline().rstrip()
    arr.append(word)
    
for i in range(m) :
    find = sys.stdin.readline().rstrip()
    if find not in arr :
        print(-1)
    else :
        for j in range(n) :
            if arr[j] == find :
                print(j+1, end=' ')
        print()