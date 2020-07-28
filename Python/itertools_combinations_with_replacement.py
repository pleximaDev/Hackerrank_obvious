from itertools import combinations_with_replacement

line = raw_input().split()
# print line
str, k = line[0], int(line[1])
str = list(str)
str.sort()
str = "".join(str)
# print str
arr = list(combinations_with_replacement(str, k))
# arr.sort()
for _ in range(len(arr)):
    print "".join(arr[_][:])
