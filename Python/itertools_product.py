
from itertools import product

# first_list = raw_input().split(" ")
# second_list = raw_input().split(" ")
first_list = list(map(int, raw_input().split(" ")))
second_list = list(map(int, raw_input().split(" ")))

out = list(product(first_list,second_list))
# print(list(product(first_list, second_list)))
stry = str(out)


# print stry[:5]
# print stry[5 + 1:]

stry = stry.replace('[', '')
stry = stry.replace(']', '')
stry = stry.replace('),', ')')

# for _ in range(len(stry) - 1):
#     print "_ = ", _
#     if stry[_] == '[' or stry[_] == ']':
#         stry = stry[:_] + stry[(_ + 1):]
print stry
# str = "("
# for _ in range(len(out)):
#     for __ in range(len(first_list)):
#         str += out[_][__]
#         if __ < len(first_list) - 1:
#             str += ", "
#     if _ < len(out) - 1:
#         str += ") ("
#     else:
#         str += ")"
# print str

