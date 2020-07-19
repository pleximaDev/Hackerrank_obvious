def mutate_string(string, position, character):
    str = string[:position] + character + string[position + 1:]
    # string = "abracadabra"
    # l = list(string)
    # l[5] = 'k'
    # string = ''.join(l)
    # print string
    return str

if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new
