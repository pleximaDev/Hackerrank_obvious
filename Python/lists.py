if __name__ == '__main__':
    my_list = list()
    N = int(raw_input())
    for _ in range(N):
        line = raw_input()
        res = line.count(' ')

        if res == 0:
            command = line
        elif res == 1:
            command, param = line.split()
            param = int(param)
        elif res == 2:
            command, param1, param2 = line.split()
            param1 = int(param1)
            param2 = int(param2)
            
        if command == "insert":
            i = param1
            e = param2
            my_list.insert(i, e)
        elif command == "print":
            print my_list
        elif command == "remove":
            e = param
            my_list.remove(e)
        elif command == "append":
            e = param
            my_list.append(e)
        elif command == "sort":
            my_list.sort()
        elif command == "pop":
            i = param
            my_list.pop(i)
        elif command == "reverse":
            my_list.reverse()

