# Digital Campus 2019/2020 -- Algorithmie de la Data

## Premiers pas en Python - Correction

### Exercice 0
   
```python
a = 5.3
b = 9.70
c = a + b
print(c)
c += a
d = c
d -= 1
```

#### Que vaut la variable `c` à la fin du programme?

`c` vaut 20.3 à la fin du programme: 

```python
a = 5.3
b = 9.70
c = a + b  # c vaut 15 (5.3 + 9.7) 
print(c)
c += a     # c vaut 20.3 (c = c + a ==> c = 15 + 5.3) ==> dernière affectation
d = c
d -= 1
print(c)   # on affiche c pour connaître sa valeur
```
   
#### Que vaut la variable `d` à la fin du programme? 

`d` vaut 20.3 à la fin du programme: 

```python
a = 5.3
b = 9.70
c = a + b  # c vaut 15 (5.3 + 9.7) 
print(c)
c += a     # c vaut 20.3 (c = c + a ==> c = 15 + 5.3) 
d = c      # d vaut 20.3 (d = c ==> d = 20.3)
d -= 1     # d vaut 19.3 (d = d - 1 ==> d = 20.3 - 1) ==> dernière affectation
print(d)   # on affiche d pour connaître sa valeur
```

#### Afficher le type de la variable `c`

`c` est une variable de type `float` (nombre décimal):

```python
c_type = type(c)  # on récupère le type de c
print(c_type)     # on affiche le type
```

#### A l'aide la fonction `int()`, créer une nouvelle variable `c_int` qui contient la valeur de la variable `c`    

````python
c_int = int(c)      # on crée un entier qui contient la valeur entière de c 
````

#### Afficher la valeur de `c_int`, que remarquez-vous ?

`c_int` vaut 20, la valeur de `c` est tronquée:

```python
print(c_int)        # on affiche la valeur (vaut 20)
print(type(c_int))  # on affiche le type de c_int (vaut int)
```


### Exercice 1.1

Ecrire un algorithme qui demande un nombre à l'utilisateur puis affiche le carré de ce nombre.

**Algorithme à implémenter:**
```
Début 
    
    nombre: entier
    Afficher('Donnez la valeur dont vous voulez calculer le carré')
    Saisir(nombre)

    carre : entier 
    carre ← valeur * valeur 

    Afficher('Le carré de', valeur, 'est', carre)
Fin
```

**Etapes de l'algorithme:** 

1. Demander un nombre à l'utilisateur
2. Stocker cette valeur dans une variable `nombre`
3. Calculer le carré de `nombre` et stocker cette valeur dans une variable `carre`
4. Afficher la valeur de `carre`

**Implémentation Python:**

```python
# Début du programme

print("Saisir un nombre:") # je demande un nombre à l'utilisateur
valeur_saisie = input() # je stocke la valeur saisie dans une variable
nombre = float(valeur_saisie) # je transforme cette valeur en nombre décimal

squared = nombre * nombre  # je calcule carré de nombre

print("Le carré de", nombre, " est ", squared)  # j'affiche le résultat

# Fin du programme
```

### Exercice 1.2

Afficher les nombres pairs compris entre 0 et 20 :

**Algorithme à implémenter:**
```
Début 
    i : entier 
    Pour i allant de 0 à 20 par pas de 1 Faire 
        Si i % 2 == 0 :
            Afficher(i) 	
    FinPour 
Fin 
```

**Etapes de l'algorithme:** 

1. Créer une boucle qui parcourt les nombres compris entre 0 et 20
3. Pour chaque itération:
   * on vérifie si le nombre est pair
   * si oui: on affiche ce nombre

**Implémentation Python:**

En Python, je crée une boucle en 2 étapes:

1. Créer une liste qui contient les différentes valeurs que `i` doit prendre
2. Parcourir cette liste à l'aide d'une boucle `for`

On doit donc créer une liste qui contient les nombres compris entre 0 et 20.

```python
# Début du programme

nombres = range(0, 21) # je crée la liste des nombres compris entre 0 et 20
for i in nombres:  # je crée une boucle qui parcourt la liste
    if (i % 2) == 0 :  # je vérifie si i est pair
        print(i)

# Fin du programme
```

**Une autre implémentation:**

On crée directement une liste qui contient les nombres pairs compris entre 0 et 20

```python
# Début du programme

nombres_pairs = range(0, 21, 2)  # on part de 0 et on ajoute 2 jusqu'à arriver à 20
for i in nombres_pairs:  # on parcourt la liste
    print(i)

# Fin du programme
```

### Exercice 1.3

Calculer la somme des n premiers nombres impairs. n est donné par l'utilisateur.

Par exemple, pour n=5 on calculera la somme : _1 + 3 + 5 + 7 + 9 = 25_

**Algorithme à implémenter:**
```
Début
    n: Entier
    Saisir(n)
    somme: Entier
    somme ← 0
    i: Entier
    Pour i allant de 1 à 2*n par pas de 2 Faire
        somme ← somme + i
    FinPour
    Afficher(somme)
Fin
```

**Etapes de l'algorithme:** 

1. Demander un nombre à l'utilisateur
1. Stocker cette valeur dans une variable `n` de type entier
1. Créer une variable entière `somme` pour stocker le résultat (somme vaut 0)
1. Créer une boucle qui parcourt les `n` premiers nombres impairs
1. Pour chaque itération:
    * On ajouter la valeur à la variable `somme`
1. Afficher la valeur de `somme`

**Implémentation Python:**

```python
# Début du programme

print("Saisir un nombre:") # je demande un nombre à l'utilisateur
valeur_saisie = input() # je stocke la valeur saisie dans une variable
n = int(valeur_saisie) # je transforme cette valeur en nombre

somme = 0 # j'initialise ma variable de résultat à 0

nombres_impairs = range(1, n *2, 2) # liste des n premier nombres impairs
for i in nombres_impairs:  # je parcours la liste
    somme = somme + i  # j'ajoute la valeur du ième élément à la somme

print(f"Somme des {n} premier nombres impairs: {somme}")  # j'affiche le résultat

# Fin du programme
```

### Exercice 1.4 

Afficher les n premier entiers, n est demandé à l'utilisateur et doit être compris entre 1 et 100.

**Algorithme à implémenter:**
```
Debut
    n : entier
    Afficher('Donnez un nombre entre 1 et 100')
    Saisir(n)
    Si n < 1 OU n > 100 Alors
        Afficher(n, 'doit être compris entre 1 et 100')
    Sinon
        Pour i allant de 1 à n+1 Faire
            Afficher(i)
        FinPour
    FinSi
Fin
```

**Etapes de l'algorithme:** 

1. Demander un nombre à l'utilisateur
2. Stocker cette valeur dans une variable `n` de type entier
3. Vérifier que la valeur de `n` est comprise entre 0 et 100
    * Si non: 
        * on affiche un message à l'utilisateur et on s'arrête
    * Si oui:
        * créer une boucle qui parcourt les `n` premier entiers (de 1 à `n`) 
        * pour chaque itération: afficher la valeur
        
**Implémentation Python:**

```python
# Début du programme

print("Saisir un nombre:") # je demande un nombre à l'utilisateur
valeur_saisie = input() # je stocke la valeur saisie dans une variable
n = int(valeur_saisie) # je transforme cette valeur en nombre

if n < 1 or n > 100:  # je vérifie que n est compris entre 1 et 100
    print(n, " n'est pas compris entre 1 et 100!")
else:
    liste = range(1, n + 1)  # je crée la liste n premier entiers (en partant de 1)
    for i in liste:   # je parcours la liste
        print(i)      # j'affiche la valeur du i-ème élément

# Fin du programme
```

### Exercice 1.5

Écrire l'algorithme simulant le fonctionnement d'une calculette avec les opérations (+, -, *, /)

**Algorithme à implémenter:**
```
Début 
   a, b : reels 
   operator : caractère 
   Afficher(‘Donnez le premier nombre :’) 
   Saisir(a) 
   Afficher(‘Donnez le deuxième nombre :’) 
   Saisir(b) 
   Afficher(‘Donnez le symbole de l’opération :‘) 
   Saisir(operator) 
   Selon operator 
      ‘+’ : Afficher (a + b ) 
      ‘-’ : Afficher (a - b ) 
      ‘*’ : Afficher (a * b) 
      ‘/’ : Si (b = 0) Alors 
               Afficher (‘Opération impossible’) 
            Sinon
                Afficher( a / b) 
            FinSi
      Autrement : Afficher (‘Opération inexistante’) 
  FinSelon
Fin
```

**Etapes de l'algorithme:** 

1. Demander les valeurs d'entrées à l'utilisateur:
    * Un nombre décimal: `a`
    * Un second nombre décimal: `b`
    * Un caractère  `operator` qui définit l'opération à appliquer entre les nombres `a` et `b` (addition, soustraction, multplication ou division)
2. Tester la valeur de `operator`, 5 cas possibles:
    * Cas `+` : on affiche la valeur de `a + b`
    * Cas `-`: on affiche la valeur de  `a - b`
    * Cas `*`: on affiche la valeur de `a * b`
    * Cas `/`: on doit vérifier que `b != 0` car on ne peut pas diviser un nombre par 0
        * si `b = 0`: on affiche un message d'erreur
        * sinon: on affiche la valeur de `a / b`
    * Autre cas: l'opération demandée est inconnue, on affiche un message d'erreur
      
**Implémentation en Python**:

En Python, la structure `SELON` n'existe pas: on utilise une structure `SI... SINON SI...`.

```python
# Début du programme

# On demande la valeur de a
print("Saisir un nombre")
valeur_saisie = input()
a = float(valeur_saisie)

# On demande la valeur de b
print("Saisir un second nombre")
valeur_saisie = input()
b = float(valeur_saisie)

# On demande l'opération à effectuer
print(f"Choisir une opération à effectuer entre {a} et {b} ( + , - , * , / ): ")
valeur_saisie = input()
operator = float(valeur_saisie)

# On teste la valeur de operator et on effectue l'opération demandée
if operator == '+':
    print(f"{a} + {b} = {a + b}")
elif operator == '-':
    print(f"{a} - {b} = {a - b}")
elif operator == '*':
    print(f"{a} * {b} = {a * b}")
elif operator == '/':
    if b == 0:  # On vérifie que l'opération est valide
        print(f"{a} n'est pas divisible par 0!")
    else:
        print(f"{a} n'est pas divisible par 0!")
else:  # autre cas
    print(f"{operator} n'est pas une opération valide!")

# Fin du programme
```

### Exercice 2.1 

Écrire un algorithme qui permet de permuter deux éléments d'un tableau.

**Algorithme à implémenter:**
```
Début
    n: Entier
    tableau: Tableau[n] d'Entiers
	tampon, element1, element2: Entier
	tampon ← tableau[i1]
	tableau[i1] ← tableau[i2]
	tableau[i2] ← tampon
Fin
```

**Etapes de l'algorithme:** 

Soient:

* `i` l'indice du premier élément à permuter
* `j` l'indice du second élément à permuter.

1. Stocker la valeur du premier élément dans une variable temporaire `tampon`
1. Stocker la valeur du second élément à la position `i`
1. Stocker la valeur de `tampon` à la position `j`

**Implémentation Python:** 

On considère le tableau suivant `[ 1, 2, 3, 4, 5 ]` et on souhaite permuter le 1er et le 4ème élément.

```python
# Début du programme

tab = [1, 2, 3, 4, 5] # création d'un tableau d'entiers

i = 0  # indice du 1er élément à permuter
j = 3  # indice du 2nd élément à permuter

tampon = tab[i]  # on stocke la valeur du 1er élément dans une variable "tampon"
tab[i] = tab[j]  # on affecte la valeur 4 au premier élément du tableau
tab[j] = tampon  # on affecte la valeur 1 au 4ème élément du tableau

print("Liste après permutation de 1 et 4:")
print(tab)

# Fin du programme
```
