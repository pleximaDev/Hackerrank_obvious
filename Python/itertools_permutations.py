from itertools import permutations

str = raw_input("")
n = int(list(str.split(" "))[1])
str = list(str.split(" "))[0]

# print permutations(['1','2','3'])
# <itertools.permutations object at 0x02A45210>
# print list(permutations('abc',3))

out = list(permutations(str, n))
for _ in range(len(out)):
    out[_] = "".join(out[_])
out.sort()

for _ in range(len(out)):
    print out[_]

