def count_substring(string, sub_string):
    __ = 0
    count = 0
    for _ in range(0, len(string)):
        if string[_] == sub_string[__]:
            __ += 1
            if __ == len(sub_string):
                __ = 0
                count += 1
                if string[_] == sub_string[0]:
                    __ += 1
        else:
            __ = 0
    
    return count

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count
