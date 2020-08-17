import numpy

N, M = map(int, raw_input().split())
A_line = list()
B_line = list()
for _ in range(N):
    A_line.append( list(map(int, raw_input().split())) )
for _ in range(N):
    B_line.append( list(map(int, raw_input().split())) )
A = numpy.array(A_line)
B = numpy.array(B_line)

print A + B, '\n', A - B, '\n', A * B, '\n', A / B, '\n', A % B, '\n', A ** B
