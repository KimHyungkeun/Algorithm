import numpy
import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(m) :
    arr.append(list(map(int, sys.stdin.readline().split())))

my_arr = numpy.array(arr)
ans = numpy.sum(my_arr, axis = 0)
print(numpy.prod(ans))
