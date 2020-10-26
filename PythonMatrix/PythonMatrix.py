import random
import time

digitList = []
for i in range (0, 100) :
    digitList.append (random.randint(31,255))

atLeastOne = True
while atLeastOne :
    atLeastOne = False
    for i in range (len (digitList)) :
        print (chr(digitList[i]), end="")
        if (digitList[i] != 32) :
            digitList[i] -= 1
            atLeastOne = True
    print ()
    time.sleep(0.02)