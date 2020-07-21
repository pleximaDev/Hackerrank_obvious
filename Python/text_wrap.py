import textwrap
from textwrap import wrap as wr # another way

def wrap(string, max_width):
	return '\n'.join(wr(string, max_width)) # another way
    counter = 0
    str = ''
    for _ in range(0, len(string)):
        str += string[_]
        if counter == max_width - 1:
            str += '\n'
            counter = 0
        else:
            counter += 1
    return str


if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print result
