# Digital Campus 2019/2020 -- Algorithmie de la Data

**Prérequis**: 

* créer son compte Github :white_check_mark:
* installer Python, PyCharm et Git :white_check_mark:

**Liens utiles**:

* [Documentation officielle de Python3](https://docs.python.org/fr/3)

## Premiers pas en Python

### Initialisation du projet

1. Créer son "repo" personnel:
    https://classroom.github.com/a/oRTRGTTl

2. Cloner le repo en local en utilisant PyCharm:

<img height="250" src="attachments/pycharm_clone1.png ">
<img height="250" src="attachments/pycharm_clone2.png ">


### Manipulation de variables

> On pourra s'aider des exemples présents dans le dossier `examples/`

1. Dans le dossier `tp1/`, créer un fichier Python `exercice_0.py` et copier les lignes suivantes : 
   
    ```python
    a = 5.3
    b = 9.70
    c = a + b
    print(c)
    c += a
    d = c
    d -= 1
    ```
   
2. Que vaut la variable `c` à la fin du programme? Ajouter un commentaire qui indique cette valeur.

3. Que vaut la variable `d` à la fin du programme? Ajouter un commentaire qui indique cette valeur.

4. Afficher le type de la variable `c`

5. A l'aide la fonction `int()`, créer une nouvelle variable `c_int` qui contient la valeur de la variable `c`    
   Afficher la valeur de `c_int`, que remarquez-vous ?
  
  
### Sauvegarde des modifications dans Github

Pousser un commit nommé `Manipulation de variables` qui contient le fichier `exercice_0.py` 

Pour les allergiques au Terminal:

<img height="250" src="attachments/pycharm_commit1.png ">
<img height="250" src="attachments/pycharm_commit2.png ">
<img height="250" src="attachments/pycharm_push1.png ">
<img height="250" src="attachments/pycharm_push2.png ">

Pour rappel, voici l'équivalent en lignes de commande:
```
git add -p . # L'option -p permet de voir les lignes modifiées
git commit -m "Manipulation de variables"
git push
```

### Algorithmie simple

Reprendre la correction des **exercices 1 à 5 du TD1** "Algorithmie Simple" et implémenter les solutions en Python:

Pour chaque exercice :

- Créer un fichier python dans le dossier `tp1: `exercice_td1_numeroExercice.py`
- Créer un commit par exercice
- Pousser le commit sur Github

> Pour la syntaxe, on pourra s'aider des exemples présents dans le dossier `tp1/examples/`

La correction: [Correction](td/Algorithmie%20de%20la%20data%20-%20TD1%20-%20Algorithmie%20simple%20-%20CORRECTION.pdf)

### Tableau à 1 dimension

Reprendre la correction des **exercices 1 à 4 du TD2** "Tableaux" et implémenter les solutions en Python:
   
> Pour la syntaxe, on pourra s'aider des exemples présents dans le fichier `tp1/examples/listes.py`

La correction: [Correction](td/Algorithmie%20de%20la%20data%20-%20TD2%20-%20Tableaux%20-%20CORRECTION.pdf)


### Bonus

Reprendre les **exercices 6 et 7 du TD1** "Algorithmie Simple" et implémenter les solutions en Python:

    - Fonction utile pour l'exercice 6:
    ```python
    from math import sqrt
    x = 4
    sqrt_x = sqrt(x)  # racine carrée de x, vaut 2
    ```
    
    - Fonction utile pour l'exercice 7:
    ```python
    from random import random
    random_number = random()  # retourne un nombre aléatoire compris entre 0 et 1
    ```
