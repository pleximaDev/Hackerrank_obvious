mport numpy

n, m, p = map(int, raw_input().split())
first_arr = numpy.array([raw_input().split() for _ in range(m)],int)
second_arr = numpy.array([raw_input().split() for _ in range(n)],int)
print(numpy.concatenate((first_arr, second_arr), axis = 0))
