import numpy
import sys

numpy.set_printoptions(sign=' ')
my_arr = numpy.array(input().split(),float)


print(numpy.floor(my_arr))
print(numpy.ceil(my_arr))
print(numpy.rint(my_arr))