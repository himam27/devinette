# Crée par Mathéo Hima
# Crée en 2023
# Code TP3


import random


def regles():
    print('''Bienvenu dans le château.Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire. Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.Dans ce cas, le niveau de vie de l’usager est diminué de la force del’adversaire.La partie se termine lorsque les points de vie de l’usager tombent sous 0.
L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.''')


# choix de l'usager
def menu():
    return int(input("1-Combattre cet adversaire\n"
                     "2-Contourner cet adversaire et aller ouvrir une autre porte\n"
                     "3-Afficher les règles du jeu\n"
                     "4-Quitter la partie\n"))


# fonction du jeu

def jeu():
    victoires_consécutives = 0

    import random
    nombre_potions = 20
    nombre_ennemis = 1
    vies = 20
    victoires = 0
    winstreak = 0
    defaites = 0
    potion_vie = 1

    while vies > 0:  # si quantité de vies est suffisante, le joueur peu combattre l'ennemi

        force_adversaires = random.randint(1, 5)
        print("L'adversaire a", force_adversaires, "points de force")
        choix = menu()

        if choix == 1:  # combattre le monstre

            # la force représenté par l`addition des dés
            d1 = random.randint(1, 6)
            d2 = random.randint(1, 6)
            total_d = d1 + d2

            print("Vous combattez cet adversaire")
            print("Force de l’adversaire : ", force_adversaires)
            print("Niveau de vie de l’usager: ", vies)
            print("Combat numero_combat: ", defaites)

            if total_d > force_adversaires:
                print("Sur vos dés, vous avez :", total_d)
                print("vous avez vaincus cet adversaire. Bravo !")
                nombre_victoires = victoires + 1
                print("Vous avez gagné", nombre_victoires, "victoire(s)")

                victoires_consécutives += 1

            if total_d <= force_adversaires:
                print("Vous avez perdu contre votre adversaire")
                print("vous avez perdu", force_adversaires, "vies")
                vies -= force_adversaires

        if choix == 2:  # éviter le monstre

            print("Vous contourner cet adversaire ")
            vies -= 1
            print("Vous perdez 1 point de vie")

        if choix == 3:
            print('''Bienvenu dans le château.Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire. Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.La partie se termine lorsque les points de vie de l’usager tombent sous 0.
      L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.''')

        if choix == 4:
            print("Vous avez quitté la partie, bye!")
            exit()

            # CODE BOSS FIGHT

    vies_boss = 10

    while vies_boss >= 0:
        print("vies de l'usager: ", vies)
        print("potions restantes : ", nombre_potions)


jeu()
