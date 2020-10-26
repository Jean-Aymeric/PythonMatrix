digitList = []
for i in range (0, 10) :
    digitList.append (i)

atLeastOne = True
while atLeastOne :
    atLeastOne = False
    for i in range (len (digitList)) :
        if (digitList[i] == -1) :
            print (" ", end="")
        else :
            print (digitList[i], end="")
            digitList[i] -= 1
            atLeastOne = True
    print ()