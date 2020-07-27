first_lowest = 100
second_lowest = first_lowest
lis = list()
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    lis.append([name, score])
# print lis
lis.sort()
# print lis
for _ in range (len(lis)):
    if lis[_][1] < first_lowest:
        first_lowest = lis[_][1]
    # print lis[_][1]

for _ in range (len(lis)):
    if first_lowest < lis[_][1] < second_lowest:
        second_lowest = lis[_][1]

for _ in range (len(lis)):
    if lis[_][1] == second_lowest:
        print lis[_][0]

