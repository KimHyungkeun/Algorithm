import numpy
import sys


n, m = map(int, sys.stdin.readline().split())
arr = []

for _ in range(n) :
    arr.append(list(map(int, sys.stdin.readline().split())))

my_arr = numpy.array(arr)
print(numpy.mean(my_arr, axis=1))
print(numpy.var(my_arr, axis=0))
print(round(numpy.std(my_arr, axis=None), 11))