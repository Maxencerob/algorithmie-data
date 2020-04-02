# Digital Campus 2019/2020 -- Algorithmie de la Data

**Liens utiles**:

* [Documentation officielle de Python3](https://docs.python.org/fr/3)
* [Structures de données en Python](https://docs.python.org/fr/3.7/tutorial/datastructures.html#)

## Structures de données Listes, Tuples et dictionnaires

> Pour la syntaxe, on pourra s'aider des exemples présents dans le dossier `tp3/examples/`

## Tuples

Dans le dossier `tp3/`, créer un fichier `tuples.py`

### Les bases

1. Créer un tuple `abc` qui contient 5 les premiers lettres de l'alphabet (de A à E)
2. Afficher la lettre `D` contenue dans `abc`
3. Afficher les trois dernières lettres de `abc`

### Manipulation de tuples

```
t1 = (1, 2, 3, 4)
t2 = (4, 5, 6)
t3 = (2, 4, 6)
```

1. Créer une variable `t4` qui contient la concaténation les tuples `t1` et `t3`

2. Afficher le nombre de `4` contenus dans `t4`

3. Créer une variable `t2_4` qui contient les tuples `t2` et `t4`

4. Afficher la 4ème valeur du deuxième tuple de `t2_4`

### Sauvegarde des modifications
Pousser un commit nommé `Tuples` qui contient le fichier `tuples.py` 

## Listes

Dans le dossier `tp3/`, créer un fichier `listes.py`

On considère la liste :

```
list_1 = [8, 12, 15, 6, 10, 19, 18, 7, 13, 15, 8, 15, 17, 13, 12, 15, 16, 11, 10, 3, 19, 20, 15]
```

1. Afficher l'écart entre le max et le min de la list_1

2. Cette liste correspond en fait aux notes des élèves à un DS de maths:

    1. Afficher le nombre d'élèves
    
    2. Un élève était absent, il a rattrapé le controle et obtenu la note de 14. Rajouter cette note à la liste des notes.
    
    3. Il y a eu une faute de frappe sur la cinquième note. L'élève a eu en réalité 13. Modifier sa note.
    
    4. Quelle est la moyenne de la classe?
    
    5. Quelle est la médiane de la classe?

### Sauvegarde des modifications
Pousser un commit nommé `Listes` qui contient le fichier `listes.py` 


## Dictionnaires

Dans le dossier `tp3/`, créer un fichier `dico.py`

Créer un dictionnaire `awesome_couples` qui contient les couples clé-valeur suivants :

```
('Batman','Robin')
('Harley Quinn','Poison Ivy')
('Iron man','War machine')
('Phenix','Cyclope')
```

1. Afficher le partenaire de Phenix (alias Jean Grey)
2. Remplacer la valeur de clé `Phenix` par `Jean Grey`
3. Ajouter le duo "Ant man" et "the Wasp" au dictionnaire `awesome_couples`

### Sauvegarde des modifications
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

2. Sauvegarde des modifications : pousser un commit nommé `Matrices` qui contient ce programme.
