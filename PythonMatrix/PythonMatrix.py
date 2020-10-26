import random
import time
import os

os.system("color 02")
digitList = []
max = 32
for i in range (0, 100) :
    digitList.append (random.randint(32,255))
    if max < digitList[i] :
        max = digitList[i]

atLeastOne = True
while atLeastOne :
    atLeastOne = False
    for i in range (len (digitList)) :
        if (255-digitList[i] < max):
            print(" ", end="")
            atLeastOne = True
        else :
            print (chr(255-digitList[i]+32), end="")
            if (digitList[i] > 32) :
                digitList[i] -= 1
    max -= 1
    print ()
    time.sleep(0.02)