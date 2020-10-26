import random

digitList = []
for i in range (0, 100) :
    digitList.append (random.randint(0,9))

atLeastOne = True
while atLeastOne :
    atLeastOne = False
    for i in range (len (digitList)) :
        print (digitList[i], end="")
        if (digitList[i] == 0 or digitList[i] == " ") :
            digitList[i] = " "
        else :
            digitList[i] -= 1
            atLeastOne = True
    print ()