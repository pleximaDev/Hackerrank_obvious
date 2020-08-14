import numpy

n, m = map(int, raw_input().split())
array = numpy.array([raw_input().split() for _ in range(n)], int)
print (array.transpose())
print (array.flatten())
