sumThirdColumn=0
listOfLines=open("./exemple.csv", 'r').readlines()
for line in listOfLines: 
    arrLine=line.split(";")
    sumThirdColumn=sumThirdColumn+int(arrLine[2])
    print(arrLine)


print("sumThirdColumn :" + str(sumThirdColumn))