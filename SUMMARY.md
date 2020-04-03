# Digital Campus 2019/2020 -- Algorithmie de la Data

## L'essentiel

### Déclaration & affectation d'une variable

Rappel :

* Sert à stocker une valeur (modifiable au cours du programme)
* Définie par un **nom** et un **type**
* Contient toujours la **dernière valeur affectée**

En Python :

On déclare une variable en lui affectant directement une valeur. Le type est déduit dynamiquement :

```python
a_string = "string"  # une chaîne de caractères (se note aussi a_string = 'string')
an_integer = 2  # un entier
a_float = 3.0  # un décimal
a_boolean = True  # un booléen
a_list = ["a", "b", "c"]  # la liste peut être vue comme un tableau à 1 dimension de taille variable
```

L'affectation se fait avec le signe `=` :

```python
a = 1
a += 1  # équivaut à: a = a + 1
a -= 1  # équivaut à: a = a - 1
a, b = 1, 2  # affectation multiple, équivaut à: a = 1 et b = 2
```

| :warning: Le nom d'une variable s'écrit en anglais et en **snake_case**: tout en **minuscules** et on remplace les espaces `" "` par le signe underscore `"_"` 
| :---

### Opérations entre les variables

#### Opérateurs mathématiques

```python
3 + 5  # addition
3 - 5  # soustraction
3 * 5  # multiplication
5 / 3  # division
5 // 3 # division entière (vaut 1)
5 % 3  # modulo (vaut 2)
```

#### Opérateurs logiques / booléens

Rappel :

* Retourne VRAI ou FAUX

* 3 opérateurs logiques: 
    * condition1 ET condition2 : pour vérifier que les deux conditions sont vraies
    * condition1 OU condition2: pour vérifier que l'une des deux conditions est vraie
    * NON condition: pour vérifier que la condition est fausse
    
* Règles de priorité: 
   * NON puis ET puis OU
   * l'utilisation des parenthèses permet de changer l'ordre
   
En Python :

```python
variable_vraie = True
variable_fausse = False
variable_vraie and variable_fausse  # vaut False
variable_vraie or variable_fausse  # vaut True
not variable_vraie  # vaut False
```

#### Opérateurs de comparaison

Rappel :

* Permet de comparer deux valeurs
* Retourne VRAI ou FAUX

En Python:

```python
3 == 5  # égal
3 != 5  # inégal
3 > 5  # strictement supérieur
3 >= 5  # supérieur ou égal
3 < 5  # strictement inférieur
3 <= 5  # inférieur ou égal
```

### Structure conditionnelle

Rappel:

* Permet d'exécuter une portion de code selon une condition

<img height="250" src="/attachments/struct_if.png ">

```python
condition_a = True
condition_b = False
if condition_a:
    print("condition_a est vraie, j'exécute l'action V1")
elif condition_b:
    print("condition_a est fausse et condition_b est vraie, j'exécute l'action V2")
else:
    print("condition_a et condition_b sont fausses, j'exécute l'action F")
```

### Les boucles

* Permet d’exécuter une portion de code plusieurs fois de suite
* Chaque exécution est appelée itération

**TantQue**

On répète l’action tant que la condition est vraie

<img height="250" src="/attachments/loop_while.png ">

```python
condition = True
while condition:
    print("je répète l'action")
```

**For**

* On répète l’action un certain nombre de fois connu à l'avance.
* Pour construire la boucle, on définit:
    * une valeur de départ
    * une borne limite (:warning: toujours exclue)
    * un pas (incrément)

<img height="250" src="/attachments/loop_for.png ">

```python
for i in range(0, 100, 1):  # Pour i allant de 0 à 100 (exclu) par pas de 1
    print("Je répète l'action 100 fois")
```

N.B. par défaut, le pas est égal à 1

```python
for i in range(0, 100):
    print("Je répète l'action 100 fois")
```

**Parcours d'une liste**

```python
une_list = [1, 2, 3]
for i in une_list:
    print(i)
```

### Fonctions utiles

Afficher un texte dans la console :

> La fonction `print` permet d’afficher l’état d’une variable au moment où l'on exécute l’instruction print.
> Il n'a pas d'incidence sur le programme

```python
print("Hello world!")
un_string = "DC"
print(f"Hello {un_string}!")  # Affiche "Hello DC!"
```

Communiquer avec l'utilisateur via la console :

> La fonction `input` permet de récupérer une chaîne de caractères saisie par l'utilisateur.
> Si on souhaite récupérer un type différent, il faut faire la conversion (str -> int, str -> float, ...)
```python
user_input_str = input("Saisir quelque chose: ")   # retourne un objet de type str()
user_input_int = int(input("Saisir un entier: "))  # on transforme la chaîne de caractère dans le type attendu
```


### Utilisation de Git  bash

Pour exécuter une commande, on peut utiliser :

* sous macOs : application Terminal
* sous Windows : programme Git-Bash
* pour tout le monde : PyCharm -> Terminal

Télécharger le projet:
```bash
git clone ssh_url  # télécharge le contenu du projet dans le répertoire courant
```

Sauvegarder des modifications:
```bash
git status                  # affiche la liste des fichiers modifiés
git add .                   # ajoute tous les fichiers modifiés
git commit -m "un message"  # crée le commit
git push                    # pousse les modifications sur Github
```

Commandes bash utiles:
```bash
pwd                # affiche le répertoire courant
cd mon_dossier     # changer de répertoire courant
ls                 # affiche le contenu du repértoire courant
mkdir nom_dossier  # crée un dossier (dans le répertoire courant)
rm -r nom_dossier  # supprime un dossier
rm un_fichier      # supprime un fichier
```

Autres commandes utiles:

```bash
git add nom_fichier # ajoute un fichier modifié
git add nom_dossier # ajoute tous les fichiers présents dans nom_dossier
git add .           # ajoute tous les fichiers modifiés
git add *.py        # ajoute tous les fichiers Python (se termine en .py)
```
