# Digital Campus 2019/2020 -- Algorithmie de la Data

**Liens utiles**:

* [Documentation officielle de Python3](https://docs.python.org/fr/3)
* [Structures de données en Python](https://docs.python.org/fr/3.7/tutorial/datastructures.html#)

## Structures de données Listes, Tuples et dictionnaires

> Pour la syntaxe, on pourra s'aider des exemples présents dans le dossier `tp3/examples/`

## Listes

Dans le dossier `tp3/`, créer un fichier `listes.py`

### Exercice 1

On considère le programme suivant:

```python
t = [1, 2, 3, 4, 5]
a = t[0] + t[3]
b = t[-1]
c = t[3:]
a = a + t[-2]
```

1. Afficher le type de la variable `t`

2. Que vaut la variable `a` à la fin du programme?

3. Afficher le type des variables `b` et `c`

4. Que valent les variables `b` et `c` à la fin du programme?

5. Soit `i` un entier quelconque, que renvoie l'instruction `t[-i]` ?

6. Soit `j` un entier quelconque, que renvoie l'instruction `t[j:]` ?

7. Exécuter l'instruction `t[-30]`. Conclusion?

7. Créer une liste `abc` qui contient 5 les premiers lettres de l'alphabet (de A à E)

8. Afficher la lettre `D` contenue dans `abc`

9. Afficher les trois dernières lettres de `abc`

### Exercice 2

On considère le programme suivant:

```python
liste = [1, 4, 1, 2, 1, 5, 3, 1, 12]
a = len(liste)
b = liste[0]
liste.append(0)
c = len(liste)
d = liste[-1]
```

1. Que valent les variables `a`, `b`, `c` et `d` à la fin du programme?

1. Soit `l` une liste quelconque, que renvoie l'instruction `len(l)` ?

1. Soit `i` un entier quelconque, que renvoie l'instruction `liste.append(i)` ?

1. Ajouter les entiers suivants à la liste:  `2`, `9`, `1`

1. Soit `liste_2 = [3, 6, 8]`, ajouter les éléments de `liste_2` à la liste.

1. A l'aide de la méthode `remove`, supprimer l'entier `1` de la liste. Que vaut la valeur de `liste` ? Supprimer tous les `1` de la liste.

1. A l'aide de la fonction `help`, afficher l'aide de la classe `list`. Quelle méthode permet de trier une liste ?

1. Trier la liste.

1. Afficher le minimum et le maximum de la liste (sans utiliser de fonction).

1. A l'aide des fonctions `min` et `max` retrouver le résultat de la question précédente.

1. A l'aide d'une boucle `for`, calculer la somme des éléments de la liste.

1. Retrouver le résultat de la question précédente à l'aide de la fonction `sum`.

1. Ajouter l'élément `"a"` à la liste puis exécuter l'instruction `sum(liste)`. Conclusion?

### Moyenne de la classe

On considère la liste suivante:
```python
grades = [8, 12, 15, 6, 10, 19, 18, 7, 13, 15, 8, 15, 17, 13, 12, 15, 16, 9, 10, 3, 19, 20, 15]
```

1. Afficher l'écart entre le max et le min de la liste `grades`

2. Cette liste correspond en fait aux notes des élèves à un DS de maths:

    1. Afficher le nombre d'élèves
    
    2. Un élève était absent, il a rattrapé le controle et obtenu la note de 14. Rajouter cette note à la liste des notes.
    
    3. Il y a eu une faute de frappe sur la cinquième note. L'élève a eu en réalité 13. Modifier sa note.
        
    4. Quelle est la moyenne de la classe?
    
    5. (Bonus) Quelle est la médiane de la classe?

    6. (Bonus) Un élève doit obtenir une note supérieure ou égale à 10 pour valider la matière. Combien de personnes ont validé la matière?
    
    7. (Bonus) Un élève qui a obtenu entre 8 et 10 peut effectuer une session de rattrapage. Combien de personnes peuvent aller aux rattrapages? Combien de personnes ont échoué (note strictement inférieure à 8)?

### Sauvegarde des modifications
Pousser un commit nommé `Listes` qui contient le fichier `listes.py` 


## Dictionnaires

Dans le dossier `tp3/`, créer un fichier `dico.py`

Créer un dictionnaire `awesome_couples` qui contient les couples clé-valeur suivants :

On considère le programme suivant:

```python
awesome_couples = {
    'Batman': 'Robin',
    'Harley Quinn': 'Poison Ivy',
    'Iron man': 'War machine',
    'Phenix' : 'Cyclope',
    'Bob sponge square': 'Patrick'
    }

a = awesome_couples['Phenix']
bob = 'Bob sponge square'
b = (bob, 'Patrick starfish') in awesome_couples
awesome_couples['Ant man'] = 'the Wasp'
del awesome_couples['Bob sponge square']
c = bob in awesome_couples
d = awesome_couples.get(bob, 'unknown')
e = awesome_couples.get('Ant man', 'toto')
```

1. Que valent les variables `a`, `b`, `c`, `d` et `e` à la fin du programme?
1. Soit `key` une clé du dictionnaire quelconque, que fait l'instruction `del awesome_couples[key}` ?
1. Soient `valeur1` et `valeur2` deux variables de type str, que retourne l'instruction `awesome_couples.get(valeur1, valeur2)`?
1. L'instruction `awesome_couples.items()` permet d'obtenir la liste des éléments du dictionnaires. Afficher le texte suivant à l'écran:
   ```
    L'acolyte de Batman est Robin
    L'acolyte de Harley Quinn est Poison Ivy
    L'acolyte de Iron man est War machine
    L'acolyte de Phenix est Cyclope
    L'acolyte de Ant man est the Wasp
   ```
1. Remplacer la valeur de clé `Phenix` par `Jean Grey`

### Sauvegarde des modifications sur Github
Pousser un commit nommé `Dictionnaires` qui contient le fichier `dico.py` 


## Bonus

### Multiplication de matrices

Le produit matriciel permet de multiplier deux matrices de taille `a x b` et `b x c`.
En multipliant termes à termes les éléments en ligne de la matrice de gauche avec les éléments en colonne de la matrice de droite puis en sommant le tout, on obtient une matrice de taille `a x c`

Exemple: 
```
|5, 6, 1|            |21, 84|
|5, 4, 2|   |1, 8|   |21, 80|
|1, 4, 3|   |2, 6|   |21, 56|
|2, 4, 5| x |4, 8| = |30, 80|
```

1. Implémenter un programme qui calcule le produit matriciel des matrices `matrix_A` et `matrix_B` suivantes:
    ```python
    matrix_A = [[5, 6, 1], [5, 4, 2], [1, 4, 3], [2, 4, 5]]
    matrix_B = [[1, 8], [2, 6], [4, 8]]
    ```

2. Sauvegarde des modifications sur Github : 
    pousser un commit nommé `Matrices` qui contient ce programme.
