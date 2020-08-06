n = int(raw_input())
eng_roll_num = set(raw_input().split())
b = int(raw_input())
french_roll_num = set(raw_input().split())
res = eng_roll_num & french_roll_num
print len(res)
