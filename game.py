from getpass import getpass
#getpass permet d'entrer une variable sans l'afficher 

mot = getpass("Entrer un mot: ")
nb_error = 0
liste = []
votre_liste = []

for x in mot:
    liste.append(x)
    votre_liste.append('*')

print("".join(votre_liste))


while nb_error < 10:
    lettre = input("Entrez votre lettre: ")
    if len(lettre)>1:
       
       if lettre == mot:
            print("vous avez trouvé")
            break
    
    if lettre in liste:
        for(i,x) in enumerate(liste):
           if x == lettre:
            votre_liste[i] = x
        lettre_correct = "".join(votre_liste)
        print("bonne lettre")

        if liste == votre_liste:
            print("vous avez trouvé le mot ")

    else:
        nb_error +=1
        print("mauvaise lettre, il vous reste %s essais" %(9-nb_error))

if nb_error == 9:
    print("Vous avez perdu")


