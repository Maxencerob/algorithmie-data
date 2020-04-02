# Digital Campus 2019/2020 -- Algorithmie de la Data

**Liens utiles**:

* [Documentation officielle de Python3](https://docs.python.org/fr/3)

## Fonctions, tests unitaires et TDD

### Refactoring

Votre collègue est parti en vacances et vous a laissé un gentil post-it sur votre bureau :

_"Coucou! J'ai pas eu le temps de finir, tu pourras t'en occuper? A charge de revanche!"_

0. Rendez-vous sur `tp4/cracra.py` et faire passer les tests
0. Pousser un commit nommé `Refacto` qui contient le fichier `cracra.py` 

### Palindrome

Un palindrome est un mot ou une phrase qui peut se lire dans les deux sens, par exemple _kayak_.

Le but de cet exercice est de définir une fonction qui vérifie si une séquence est palindromique ou non.

Quelques exemples de palindromes: [Wikipédia](https://fr.wikipedia.org/wiki/Liste_de_palindromes_fran%C3%A7ais)

### Vérifier si un mot est un palindrome

On se propose tout d'abord de vérifier si un mot est un palindrome.

0. Dans le dossier `tp4/`, créer un fichier `palindrome.py`

0. Créer une fonction `is_palindrome` qui prend un mot en paramètre et retourne la valeur `True`

0. Créer un test unitaire `test_word` qui vérifie le comportement de la fonction `is_palindrome`:

    * La fonction doit retourner `True` lorsque le mot passé en paramètre est un palindrome
    * La fonction doit retourner `False` lorsque ce mot n'est pas un palindrome
    
0. Lancer ce test et vérifier qu'il échoue

0. Modifier la fonction `is_palindrome` pour qu'elle retourne les résultats attendus:

    _(Indications)_ :

    * Une chaîne de caractères peut se manipuler comme une liste de caractères:
        ```python
       my_word = "kayak"
       my_word[0] == "k"   # première lettre du mot
       my_word[-1] == "k"  # dernière lettre du mot
       length = len(my_word)
       for i in range(0, length):
           print(my_word[i])
       ```
      
0. Lancer le test et vérifier qu'il fonctionne.

0. Est-on obligé de parcourir le mot en entier pour savoir s'il est un palindrome? Modifier la fonction `is_palindrome` en conséquence.

0. Lancer le test et vérifier qu'il fonctionne.

> Pour les tests unitaires:
> * on pourra s'aider de l'exemple présent dans le fichier `examples/unit_test.py`
>
> Pour la manipulation de listes:
> * on pourra s'aider de l'exemple présent dans le fichier `tp3/examples/listes.py`


### Sauvegarde des modifications dans Github

Pousser un commit nommé `Palindrome` qui contient le fichier `palindrome.py` 
