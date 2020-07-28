from itertools import combinations

line = raw_input().split()
# print line
str, k = line[0], int(line[1])
str = list(str)
str.sort()
str = "".join(str)
# print str
for __ in range(1, k + 1):
    arr = list(combinations(str, __))
    # arr.sort()
    for _ in range(len(arr)):
        print "".join(arr[_][:])
# print arr
