import numpy
shape = list(map(int, raw_input().split()))
print (numpy.zeros(shape, dtype = numpy.int))
print (numpy.ones(shape, dtype = numpy.int))
# i, j, k = map(int, raw_input().split())
# for __ in range(k):
#     print numpy.zeros((i,j), dtype = numpy.int)
#     if _ is not k - 1:
#         print
# for _ in range(k):
#     print numpy.ones((i,j), dtype = numpy.int)
#     if _ is not k - 1:
#         print
