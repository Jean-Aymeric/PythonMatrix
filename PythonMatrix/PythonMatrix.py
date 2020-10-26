digitList = []
for i in range (0, 10) :
    digitList.append (i)

for i in range (len (digitList)) :
    print (digitList[i], end="")
    if (digitList[i] == " " or digitList[i] == 0) :
        digitList[i] = " "
    else :
        digitList[i] -= 1
print ()
print(digitList)