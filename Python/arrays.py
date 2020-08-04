import numpy

def arrays(arr):
    return numpy.flip(numpy.array(arr).astype(numpy.float))

arr = raw_input().strip().split(' ')
result = arrays(arr)
print(result)
