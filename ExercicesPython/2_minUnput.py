numInput=-1
numOutput=0
while numInput != 0:
    numInput    =  int(input("Entrez un entier : "))
    numOutput   = numInput if numInput > 0 and numInput < numOutput or numOutput == 0 else numOutput


print("Minimum Entier rentré : " + str(numOutput) )