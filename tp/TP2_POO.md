# Digital Campus 2019/2020 -- Algorithmie de la Data

**Liens utiles**:

* [Documentation officielle de Python3](https://docs.python.org/fr/3)

## Programmation orientée objet (POO)

> Pour la syntaxe, on pourra s'aider de l'exemple présent dans le fichier `examples/classes.py`

On souhaite modéliser la relation suivantTP3_COLLECTIONS.mde :

<img height="300" src="attachments/modelisation1.png ">

### Modéliser des singes

1. Dans le dossier `tp2`, créer un nouveau fichier Python `monkey.py` 

2. Déclarer une classe `Monkey` qui définit un singe

3. Ajouter un constructeur à la classe `Monkey` qui permet d'attribuer un nom à un singe à l'aide de la méthode suivante:
    ```python
    def __init__(self, name):
        self.name = name
    ```        
4. Créer un singe qui s'appelle Pierre à l'aide de la syntaxe suivante :

    ```python
    pierre = Monkey("Pierre")
    ```

5. Créer une classe `Banana` qui définit une banane. Ajouter un constructeur à cette classe qui permet d'attribuer une couleur à une banane.

6. Quelle méthode doit-on ajouter à la classe `Monkey` pour que Pierre mange une banane? L'implémenter.
    
    (Pour rappel)
    ```python
    def ma_methode(self):
       print("J'exécute la méthode")
    ```

7. Ecrire le code qui modélise la relation suivante: __"Un singe nommé Pierre mange une banane de couleur jaune"__.
        
8. Ecrire le code qui modélise la relation suivante: __"Un singe nommé Marie mange une banane de couleur verte"__.
    
9. Modéliser la relation suivante :
   <img height="250" src="attachments/modelisation2.png ">

10. Sauvegarder les modifications dans Github : pousser un commit nommé `POO` qui contient le fichier `monkey.py` 
