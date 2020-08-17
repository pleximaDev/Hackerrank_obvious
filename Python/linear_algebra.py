import numpy
n = int(raw_input())
arr = list()
for _ in range(n):
    arr.append( list(map(float, raw_input().split())) )
print round(numpy.linalg.det(numpy.array(arr)), 2)
