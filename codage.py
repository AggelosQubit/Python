import random
import os

def genereFichierAvecText(fic_g,text):
    #print("IN genereFichierAvecText")
    #Maintenant qu'on a le text , on l'append dans fic_g
    # Open a file with access mode 'a'
    if os.path.exists(fic_g):
        os.remove(fic_g)
    #AJOUT DE LA CLE DANS LE FICHIER
    file_object = open(fic_g, 'a')
    file_object.write(text)
    file_object.close()


#long Longueur de la Clé
#fic fichier de sortie contenant cette derniere
def genereVernam (longueurMessage, fichier):
    #print("IN VERNAM")
    #POUR NE PAS AVOIR D'ESPACE AU DEBUT DE LA CLE DANS LE FICHIER
    cle=str(random.randrange(128))
    for _ in range(longueurMessage-1):
        cle=cle+" "+str(random.randrange(128))
    genereFichierAvecText("vernam.txt",cle)

def encode(fic_m, fic_enc):
    #print("IN ENCODE")
    f = open(fic_m, "r")
    messageAEncoder=list(f.read())
    f.close()
    charAEncoder=str(ord(messageAEncoder[0]))
    for indexCharAEncoder in range(1, len(messageAEncoder) ):
        charAEncoder = charAEncoder+" "+str( ord( messageAEncoder[indexCharAEncoder] ) )   
    genereFichierAvecText(fic_enc,charAEncoder)
    return len(messageAEncoder)

def chiffrage(fic_encoder,fic_cle):
    #print("IN CHIFFRAGE")
    f = open(fic_encoder, "r")
    g = open(fic_cle, "r")

    fTab=f.read().split(" ")
    gTab=g.read().split(" ")

    f.close()
    f.close()
    if len(fTab) != len(gTab) :
        print("LONGUEUR DE LA CLE ET DU FICHIER ENCODE DIFFERENTE!")
    else:
        #ADDITION DE CHAQUE ELEMENT 
        #MODULO 256???????
        charAChiffrer=str(   ( int(fTab[0]) + int(gTab[0]) ) % 256  )
        for i in range(1, len(fTab) ):
            charAChiffrer = charAChiffrer+" "+str( ( int(fTab[i]) + int(gTab[i]) ) % 256 )
    genereFichierAvecText("chiffrage.txt",charAChiffrer)


def main():
    print("Chiffrement de Vernam")
    message='message.txt'
    lecoder='le_coder.txt'
    vernam='vernam.txt'
    genereVernam( encode(message,lecoder) ,vernam)
    chiffrage(lecoder,vernam)
    print("\nChiffrement de Vernam Effectué!\nVeuillez consultez les TXTs Associés.")

main()