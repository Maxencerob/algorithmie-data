# Installation des outils

Ne pas hésiter à abuser de Google. Quelques liens utiles :

## Python

### Windows: 

1. Télécharger de Python *3.7.x* sur le site officiel : https://www.python.org/downloads/ 

2. Lancer l'installateur et cocher l'option "add Python 3.7 to PATH":
![alt text](/python_install_win.png "Python for Windows")

3. Vérifier l'installation :

* Ouvrir l'invite de commandes (Menu Démarrer -> Programme -> Invite de commandes)
* Taper la commande `python --version` vous devriez obtenir le message suivant: 
	``` 
	Python 3.7.x
	```

:warning: Si vous avez un message qui ressemble à ça :
```
'python' is not recognized as an internal or external command,
operable program or batch file.
```

c'est sûrement car vous n'avez pas coché l'option indiquée plus haut.

Dans ce cas il vous faut ajouter manuellement Python aux commandes exécutables: suivre les indications [ici](https://datatofish.com/add-python-to-windows-path/)

### macOS :

1. Télécharger de Python *3.7.x* sur le site officiel : https://www.python.org/downloads/ 

2. Vérifier l'installation :

    * Ouvrir l'application `Terminal` :

    * Tapez la commande `python3 --version` vous devriez obtenir le message suivant: 
	``` 
	Python 3.7.x
	```

### Linux :

https://docs.python-guide.org/starting/install3/linux/

## PyCharm
* :warning: Installer la version **community** : https://www.jetbrains.com/fr-fr/pycharm/download

## Git / Github
Etape 1 : installer Git 
* Windows : https://gitforwindows.org/
* macOS et Linux : https://git-scm.com/downloads

Etape 2 : configurer Git 
* https://help.github.com/en/github/getting-started-with-github/set-up-git#setting-up-git

Etape 3 : autoriser la connexion à Github (ssh)
* https://help.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
