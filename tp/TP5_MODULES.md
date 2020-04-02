# Digital Campus 2019/2020 -- Algorithmie de la Data

**Liens utiles**:

* [Standard Library Python Documenation](https://docs.python.org/fr/3/library)

## Librairies et modules

### Manipulation de fichiers Json

Dans cet exercice, on se propose de manipuler un fichier au format Json.

#### Le Json

Le format JSON (JavaScript Object Notation) est un format de données qui permet de représenter de l’information structurée.

Exemple d'un fichier au format Json:

```javascript
{
    "spé-data": {
        "école": "digital-campus",
        "étudiants": 19,
        "année": "2019-2020"
    }
}
```

Ce format est très utilisé en data car il permet de stocker facilement des informations structurées dans un fichier peu volumineux.

#### Répondre à un besoin marketing

Le service marketing désire développer une application pour automatiser la segmentation de sa base client.

Il nous demande d'effectuer un POC (Proof Of Concept) pour démontrer la faisabilité d'une telle application.

Pour ce faire, nous disposons d'un extrait de la base de données client au format Json (`tp5/users.json`).

Les questions auxquelles nous devons répondre:

* Quelle la moyenne d'âge des utilisateurs?
* Quel est le hobby le plus apprécié par nos utilisateurs?
* Combien d'utilisateurs ont déclaré aimer le cinéma?
* Le Marketing compte mener une campagne de publicitaire sur le cinéma auprès des jeunes homme entre 25 et 30.
Il souhaite obtenir la liste des utilisateurs qui sont des hommes entre 25 et 30 ans (inclus) qui aiment le cinéma.

Résultats attendus:

* Un fichier `tp5/report.json` qui contient les informations suivantes:

```javascript
{
   "date": "2020-03-20",  // la date du jour au format YYYY-MM-DD
   "age": 0,             // la moyenne d'âge des utilisateurs
   "movieLovers": 0     // le nombre d'utilisateurs qui ont déclaré aimer le cinéma
}
```

* Un fichier `tp5/segmentation.csv` qui contient la liste des identifiants des utilisateurs issus de la segmentation:
(hommes entre 25 et 30 ans (inclus) qui aiment le cinéma)

| user_id 
|:-------
| 1
| ...
| n


#### Déroulé

0. Pour faire l'exercice, vous aurez besoin de trouver:

    * Comment lire et écrire un fichier en Python
    * La librairie qui permet de lire du format Json (Standard Library Python)
    * La librairie qui permet d'écrire un fichier CSV (Standard Library Python)

1. Le code est à écrire dans le fichier `tp5/user_data.py` :

   * Chaque fonction a son test unitaire, il ne reste plus qu'à les faire passer!
   * Vous pouvez commencer par coder la fonction que vous voulez, l'ordre n'a pas d'importance
   * N'hésitez pas à créer de nouvelles fonctions pour mutualiser le code. 

#### Sauvegarde des modifications
Pousser un commit nommé "Modules" qui contient :

* le fichier `user_data.py` qui contient le code de votre application
* les fichiers de sortie: `segmentation.csv` et `report.json`








