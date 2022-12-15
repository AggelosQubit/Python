sommeCalcule = 0
nombreAAjouter=-1

while nombreAAjouter != 0 :
    nombreAAjouter= int(input("Entrez un nombre : "))
    sommeCalcule = (sommeCalcule + nombreAAjouter) if nombreAAjouter>0 else sommeCalcule

print("sommeCalcule apres ajout :" + str(sommeCalcule))