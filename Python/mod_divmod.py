from __future__ import division
def divmod(a, b):
    print a // b
    print a % b
    out = "(" + str(a // b) + ", " + str(a % b) + ")"
    return out
def main():
    a, b = int(raw_input()), int(raw_input())
    print divmod(a, b)
if __name__ == '__main__':
    main()
