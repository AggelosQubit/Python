import os

numLine=0
fieldWellConstituted=True
   
def checkLine(arrLine) -> bool:
    boolToReturn    =False
    boolToPrint     =False
    lineRecap       =""

    boolToPrint     =type(arrLine[0]) == type("") and str(arrLine[0]) != ""
    boolToReturn    =type(arrLine[0]) == type("") and str(arrLine[0]) != ""
    lineRecap       =" [0] : "+str(boolToReturn)+";"

    boolToPrint     = type(int(arrLine[1])) == type(0)
    boolToReturn    =boolToReturn and ( type(int(arrLine[1])) == type(0))
    lineRecap       =lineRecap+" [1] : "+str(boolToPrint)+";"

    boolToPrint     =type(int(arrLine[2])) == type(0)
    boolToReturn    =boolToReturn and (type(int(arrLine[2])) == type(0))
    lineRecap       =lineRecap+" [2] : "+str(boolToPrint)+";"

    boolToPrint     =type(int(arrLine[3])) == type(0)
    boolToReturn    =boolToReturn and ((type(int(arrLine[3])) == type(0)))
    lineRecap       =lineRecap+" [3] : "+str(boolToPrint)

    print(lineRecap)
    return boolToReturn

listOfLines=open("./exemple.csv", 'r').readlines()
#print( listOfLines )
for line in listOfLines: 
    arrLine=line.strip()
    arrLine=arrLine.split(";")
    fieldWellConstituted=checkLine(arrLine) and fieldWellConstituted


strfieldWellConstituted= "les Champs ne sont pas bien contitués!" if not fieldWellConstituted else "Les Champs sont bien constitués!"
print(strfieldWellConstituted)
        

