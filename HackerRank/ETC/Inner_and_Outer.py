import numpy
import sys

A = numpy.array(list(map(int, sys.stdin.readline().split())))
B = numpy.array(list(map(int, sys.stdin.readline().split())))

print(numpy.inner(A, B))
print(numpy.outer(A, B))