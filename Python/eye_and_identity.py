import numpy
N, M = raw_input().split()
N = int(N)
M = int(M)
print str(numpy.eye(N, M, k = 0)).replace('1',' 1').replace('0',' 0')



