digitList = []
for i in range (0, 10) :
    digitList.append (i)

for i in range (len (digitList)) :
    if (digitList[i] == -1) :
        print (" ", end="")
    else :
        print (digitList[i], end="")
        digitList[i] -= 1
print ()
print(digitList)