n, m = raw_input().split()
array = raw_input().split()
A = list(set(raw_input().split()))
B = list(set(raw_input().split()))
happiness = 0
array = list(set(array))

for _ in range(0, len(array)):
    for __ in range(0, len(A)):
        if array[_] == A[__]:
            happiness += 1
        elif array[_] == B[__]:
            happiness -= 1
print happiness
