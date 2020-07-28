# didn't passed
import sys, errno
strr = raw_input()
counter = 1

out = ""

# _ = 1
# while _ < len(strr):
for _ in range(1, len(strr)):
    
    if strr[_] == strr[_ - 1]:
        counter += 1
        if _  == len(strr) - 1:
            #++++++++++++++++++++++++++++++++++++++++++++++++++++++
            out += "(" + str(counter) + ", " + strr[_ - 1] + ") "
            break
            #++++++++++++++++++++++++++++++++++++++++++++++++++++++

            #___________________________________________________
            # out = "(" + str(counter) + ", " + strr[_ - 1] + ") "
            # sys.stdout.write(out)
            # sys.stdout.flush()
            #___________________________________________________

            # try:
            #     sys.stdout.write(out)
            # except IOError:
            #     if IOError.errno == errno.EPIPE:
            #         print ""
    else:
        if _  == len(strr) - 1:
            #++++++++++++++++++++++++++++++++++++++++++++++++++++++
            out += "(" + str(counter) + ", " + strr[_ - 1] + ") "
            break
            #++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++
        out += "(" + str(counter) + ", " + strr[_ - 1] + ") "
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++

        #___________________________________________________
        # out = "(" + str(counter) + ", " + strr[_ - 1] + ") "
        # sys.stdout.write(out)
        # sys.stdout.flush()
        #___________________________________________________

        # print "" % out, end=" "
        # sys.stdout.write(out)
        # try:
        #     sys.stdout.write(out)
        # except IOError:
        #     if IOError.errno == errno.EPIPE:
        #         print ""
        # print ("(" + str(counter) + ", " + strr[_ - 1] + ")", end = '')
        # print "(", counter,",", int(strr[_ - 1]), ")"
        counter = 1
    # _ += 1
# out[len(out) - 1] = ""
#++++++++++++++++++++++++++++++++++++++++++++++++++
print out[:len(out) - 1] # erasing " " at the end
#++++++++++++++++++++++++++++++++++++++++++++++++++
