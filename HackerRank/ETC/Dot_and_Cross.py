import numpy
import sys

n = int(sys.stdin.readline())

arr1 = []
for _ in range(n) :
   arr1.append(list(map(int, sys.stdin.readline().split())))

arr2 = []
for _ in range(n) :
    arr2.append(list(map(int, sys.stdin.readline().split())))

A = numpy.array(arr1)
B = numpy.array(arr2)

print(numpy.dot(A, B))