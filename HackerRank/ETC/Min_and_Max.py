import numpy
import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n) :
   arr.append(list(map(int, sys.stdin.readline().split())))

my_arr = numpy.array(arr)

ans = numpy.min(my_arr, axis = 1)
print(numpy.max(ans))