# def mod(a):
#     if a >= 0:
#         return a
#     elif a < 0:
#         return -a
def main():
    a, b, m = int(raw_input()), int(raw_input()), int(raw_input())
    print a**b
    print a**b % m

if __name__ == '__main__':
    main()
