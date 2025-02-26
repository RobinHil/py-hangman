import random

choix = ["souris","clavier","hexadecimal","ecran","ordinateur","processeur","guitare","feuille","argent","corde"]
# Sélection aléatoire d'un mot dans la liste
solution = random.choice(choix)

# Initialisation du nombre de tentatives et des variables pour l'affichage et les lettres trouvées
tentatives = 7
affichage = ""
lettres_trouvees = ""

# Création de l'affichage initial avec des underscores pour chaque lettre du mot
for l in solution:
    affichage = affichage + "_ "

# Message de bienvenue
print("\nBienvenue dans mon pendu,\namusez-vous bien !")

# Boucle principale
while tentatives > 0:
    # Affichage du mot à deviner avec les lettres déjà trouvées
    print("\nmot à deviner : ", affichage)

    proposition = input("proposez une lettre : ")

    # Vérification si la lettre proposée est dans le mot
    if proposition in solution:
        lettres_trouvees = lettres_trouvees + proposition
        print(" - bravo, une lettre de plus !")
    else:
        tentatives = tentatives - 1
        print(" - mauvaise réponse !\n")
        if tentatives==0:
            print(" ==========Y= ")
        if tentatives<=1:
            print(" ||/       |  ")
        if tentatives<=2:
            print(" ||        0  ")
        if tentatives<=3:
            print(" ||       /|\\ ")
        if tentatives<=4:
            print(" ||       /|  ")
        if tentatives<=5:                    
            print("/||           ")
        if tentatives<=6:
            print("==============\n")

    # Mise à jour de l'affichage avec les lettres trouvées
    affichage = ""
    for x in solution:
        if x in lettres_trouvees:
            affichage += x + " "
        else:
            affichage += "_ "

    # Vérification si le mot a été entièrement deviné
    if "_" not in affichage:
        print("\nvous avez gagné, félicitations !!")
        break
     
print("\nLa partie est terminée !")