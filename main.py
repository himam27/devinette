# Crée par Mathéo Hima
# Crée en 2023
# code de TP2

# IMPORTATION RANDOM
import random

# choix d'intervales
num1 = int(input('Entrez votre premier nombre: '))
num2 = int(input('Entrez votre deuxème nombre: '))

# Variables global
nombresEssais = 0
réponse = True
unknown = random.randint(num1, num2)  # Randint permet de générer un nombre au hasard
# print(unknown)

while (réponse):
    essai = int(input('Entrer un nombre de %d et %d :' % (num1, num2)))

    nombresEssais += 1

    # Si la tentative est + grande (>) que l'inconnu (unknown)
    if essai > unknown:
        print('le nombre cherché est plus petit que:  ', essai)


    # Si la tentative est + petite (<) que l'inconnu (unknown)
    elif essai < unknown:
        print('le nombre cherché est plus grand que:  ', essai)


    # Si la tentative est = à l'inconnu (unknown)

    elif essai == unknown:
        print('le nombre recherché étais:', essai)
        réponse = False

# Si la tentative cherchée est = à la réponse
# if tentative == unknown:
