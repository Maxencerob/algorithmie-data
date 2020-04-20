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
