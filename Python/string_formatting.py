def print_formatted(number):
    for i in range(number):
        print str(i + 1).rjust(len(bin(number)[2:]),' '), str(oct(i + 1))[1:].rjust(len(bin(number)[2:]),' '), str(hex(i + 1))[2:].upper().rjust(len(bin(number)[2:]),' '), str(bin(i + 1))[2:].rjust(len(bin(number)[2:]),' ')

if __name__ == '__main__':
    n = int(raw_input())
    print_formatted(n)
