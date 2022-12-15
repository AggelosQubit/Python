import random
import os

nbLignToGenerate = int(input("Combien de ligne Voulez-vous générez? : "))
text="identifiant;age\n"

def genereLine() -> str:
    genre = "M" if random.randint(1,2)==1 else "F"
    id='{:0>5}'.format(random.randint(00000,99999))
    age=random.randint(1,120)

    return genre+""+str(id)+";"+str(age)

for x in range(nbLignToGenerate):
    text=text+genereLine()+"\n"

fic_g="./generate.csv"
if os.path.exists(fic_g):
    os.remove(fic_g)
#    AJOUT DE LA CLE DANS LE FICHIER
file_object = open(fic_g, 'a')
file_object.write(text)
file_object.close()