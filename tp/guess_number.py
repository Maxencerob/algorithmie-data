"""
Exercice 2: deviner un nombre

On se propose d'implémenter un jeu dans lequel l'utilisateur doit deviner un nombre.

Le principe :

* Le programme tire un nombre au hasard
* L'utilisateur propose un nombre
* Le programme lui indique si ce nombre est trop petit ou trop grand

Et ainsi de suite jusqu'à ce que l'utilisateur trouve le bon nombre.
"""

from random import randint  # import de la fonction randint

help(randint)  # affichage de l'aide de la fonction: nombre aléatoire entier compris entre 2 valeurs

number_to_guess = randint(0, 10)

print("Saisir un nombre en 0 et 10")
user_propal = int(input())
if 0 <= user_propal <= 10:
    if user_propal == number_to_guess:
        print("Vous avez gagné!")
    elif user_propal < number_to_guess:
        print("Trop petit!")
    elif user_propal > number_to_guess:
        print("Trop grand!")
else:
    print("Ce nombre n'est pas compris entre 0 et 10!")
    break

