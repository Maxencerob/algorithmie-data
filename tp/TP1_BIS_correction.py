"""
Exercice 1: calcul d'IMC

# On se propose d'implémenter un programme qui permet de calculer l'IMC d'une personne.

### L'utilisateur saisit sa taille et son poids et on lui affiche un message qui indique son IMC et sa catégorie (maigreur, normal, surpoids, obésité ou obésité morbide).

# Les étapes de l'agorithme sont les suivantes:

# 1. Identifier les données d'entrées et initialiser les variables correspondantes
# 2. Calculer l'IMC (le poids divisé par la taille au carré)
# 3. Afficher la catégorie correspondant à l'IMC
"""

# On a besoin de récupérer la taille en cm (entier) et le poids en kg (décimal) de l'utilisateur :
print("Saisir votre taille (en cm)")
taille_saisie = input()
print(type(taille_saisie))  # chaîne de caractères (str)
taille = int(taille_saisie)
print("Saisir votre poids (en kg)")
poids = float(input())

# Calcul de l'IMC
imc = poids / (taille / 100) ** 2
print(imc)

# Afficher la catégorie de l'IMC
if imc < 18.5:
    print("Maigreur")
elif imc < 24.9:
    print("Normal")
elif imc < 29.9:
    print("Surpoids")
elif imc < 40:
    print("Obésité")
else:
    print("Obésité morbide")


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
number_to_guess = randint(1, 10)

has_won = False

while not has_won:
    print("Saisir un nombre en 1 et 10")
    user_propal = int(input())
    if user_propal < 1 or user_propal > 10:
        print("Ce nombre n'est pas compris entre 1 et 10!")
    elif user_propal == number_to_guess:
        print("Vous avez gagné!")
        has_won = True
    elif user_propal < number_to_guess:
        print("Trop petit!")
    elif user_propal > number_to_guess:
        print("Trop grand!")
