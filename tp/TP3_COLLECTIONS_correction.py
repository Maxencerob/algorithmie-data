"""
Structures de données Listes, Tuples et dictionnaires
"""

"""
Exercice 1
"""

t = [1, 2, 3, 4, 5]
a = t[0] + t[3]  # 1 + 4 ==> 5
b = t[-1]
c = t[3:]
a = a + t[-2]

print(type(t))  # t est une liste

# Afficher les valeurs de a, b et c:
print(a)
print(b)
print(c)

# Soit `i` un entier quelconque: t[-i] renvoie les i derniers éléments de la liste
# Soit `j` un entier quelconque, que renvoie l'instruction t[j:] renvoie les éléments dont l'indice est plus grand que j
# t[-30] renvoie une erreur car 30 est supérieur à la taille de la liste

abc = ["A", "B", "C", "D", "E"]

# Affiche D
print(abc[3])

# Affiche les 3 dernières lettres
print(abc[-3])

"""
Exercice 2
"""

# On considère le programme suivant:

liste = [1, 4, 1, 2, 1, 5, 3, 1, 12]
a = len(liste)
b = liste[0]
liste.append(0)
c = len(liste)
d = liste[-1]

print(a)
print(b)
print(c)
print(d)

# len(liste) renvoie la taille de la liste
# Soit `i` un entier quelconque, liste.append(i) ajoute l'élément i à la fin de la liste

# Ajouter les entiers suivants à la liste:  `2`, `9`, `1`
liste.append(2)
liste.append(9)
liste.append(1)

liste_2 = [3, 6, 8]

# Ajouter les éléments de `liste_2` à la liste.
liste.extend(liste_2)

# Supprimer tous les `1` de la liste
while liste.count(1) > 0 :
    liste.remove(1)

# Quelle méthode permet de trier une liste ?
help(list())
# ---> méthode sort()

# Trier la liste
liste.sort()

# Afficher le minimum et le maximum de la liste (sans utiliser de fonction).
min_liste = 0
max_liste = 0
for element in liste:
    if element > max_liste:
        max_liste = element
    if element < min_liste:
        min_liste = element

print("Minimum", min_liste, "Maximum", max_liste)
print("Minimum", min(liste), "Maximum", max(liste))

# A l'aide d'une boucle `for`, calculer la somme des éléments de la liste.
somme_liste = 0

for element in liste:
    somme_liste += element

print("Somme", somme_liste)
print("Somme", sum(liste)) # ATTENTION: la méthode sum ne fonctionne que si tous les éléments de la liste sont du même type

"""
Exercice 3: moyenne de la classe
"""

grades = [8, 12, 15, 6, 10, 19, 18, 7, 13, 15, 8, 15, 17, 13, 12, 15, 16, 9, 10, 3, 19, 20, 15]

# Afficher l'écart entre le max et le min de la liste `grades`
min_grades = min(grades)
max_grades = max(grades)
print(max_grades - min_grades)

# Afficher le nombre d'élèves
print(len(grades))

# # Un élève était absent, il a rattrapé le controle et obtenu la note de 14. Rajouter cette note à la liste des notes.
grades.append(14)
print(grades)

#Il y a eu une faute de frappe sur la cinquième note. L'élève a eu en réalité 13. Modifier sa note.
grades[4] = 13
print(grades)

# Quelle est la moyenne de la classe?
moyenne = sum(grades)/(len(grades))
print (moyenne)

#  Quelle est la médiane de la classe?
sorted_grades = sorted(grades)
nb_eleves = len(grades)
moitie = int(nb_eleves / 2)
print(sorted_grades[moitie])

"""
(Bonus) Un élève doit obtenir une note supérieure ou égale à 10 pour valider la matière.
Un élève qui a obtenu entre 8 et 10 peut effectuer une session de rattrapage
Combien de personnes ont validé la matière?
Combien de personnes peuvent aller aux rattrapages? 
Combien de personnes ont échoué (note strictement inférieure à 8)?
"""

nb_personnes_valider = 0
nb_personnes_rattrapage = 0
nb_personnes_echouer = 0

for note in grades:
    if note >= 10:
        nb_personnes_valider = nb_personnes_valider + 1
    elif note >= 8:
        nb_personnes_rattrapage += 1
    else:
        nb_personnes_echouer += 1

print(nb_personnes_valider)
print(nb_personnes_rattrapage)
print(nb_personnes_echouer)



"""
Exercice 4: dictionnaires
"""


awesome_couples = {
    'Batman': 'Robin',
    'Harley Quinn': 'Poison Ivy',
    'Iron man': 'War machine',
    'Phenix' : 'Cyclope',
    'Bob sponge square': 'Patrick'
    }

a = awesome_couples['Phenix']  # On récupère la valeur de la clé Phenix
bob = 'Bob sponge square'
b = (bob, 'Patrick') in awesome_couples.items()  # "Le couple (Bob sponge square, Patrick starfish) est-il dans le dico?
awesome_couples['Ant man'] = 'the Wasp'  # ajout du couple (Ant-Man, the Wasp)
del awesome_couples['Bob sponge square']  # suppression de la clé Bob sponge square
c = bob in awesome_couples   # La clé Bob sponge square est-elle dans le dico?
d = awesome_couples.get(bob, 'unknown')   # On récupère la valeur de la clé Phenix, si on ne la trouve pas on prend comme valeur 'unknown'
e = awesome_couples.get('Ant man', 'toto')  # On récupère la valeur de la clé Ant man, si on ne la trouve pas on prend comme valeur 'toto'

print(a)
print(b)
print(c)
print(d)
print(e)

"""
Afficher le texte suivant à l'écran:
   ```
    L'acolyte de Batman est Robin
    L'acolyte de Harley Quinn est Poison Ivy
    L'acolyte de Iron man est War machine
    L'acolyte de Phenix est Cyclope
    L'acolyte de Ant man est the Wasp
   ```
"""
for (k, v) in awesome_couples.items():
    print("L'acolyte de", k, " est", v)

# Remplacer la valeur de clé `Phenix` par `Jean Grey`
print("Dico avant modif:", awesome_couples)
awesome_couples["Jean Grey"] = awesome_couples["Phenix"]
del awesome_couples["Phenix"]
print("Dico après modif:", awesome_couples)
