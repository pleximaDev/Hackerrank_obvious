inp = ""
for _ in range(4): inp += raw_input() + " "
a, b, c, d = inp.split()
a, b, c, d = int(a), int(b), int(c), int(d)

print a**b + c**d

