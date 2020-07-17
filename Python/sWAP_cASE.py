def swap_case(s):
    str = ""
    for _ in range(0, len(s)):
        str += s[_].upper() if s[_].islower() else s[_].lower()
    return str

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
