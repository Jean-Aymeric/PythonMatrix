digitList = []
for i in range (0, 10) :
    digitList.append (i)

for j in range(10):
    for i in range (len (digitList)) :
        print (digitList[i], end="")
        if (digitList[i] == 0 or digitList[i] == " ") :
            digitList[i] = " "
        else :
            digitList[i] -= 1
    print ()