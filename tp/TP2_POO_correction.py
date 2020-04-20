"""
Programmation orientée objet (POO)
On souhaite modéliser les relations suivantes:

Un singe nommé Marie mange une banane de couleur verte
Un singe nommé Marie mange une banane de couleur verte
Marie et Pierre ont un bébé qui s'appelle Robert
"""


class Singe:

    def __init__(self, nom):
        self.nom = nom

    def mange(self, banane):
        print(self.nom, "mange une banane de couleur", banane.couleur)

    def copule(self, copain, nom_enfant):
        print(self.nom, "copule avec", copain.nom, "et a un enfant nommé", nom_enfant)


class Banane:

    def __init__(self, couleur):
        self.couleur = couleur


class CoupleDeSinges:

    def __init__(self, maman, papa):
        self.maman = maman
        self.papa = papa

    def reproduit(self, nom_enfant):
        enfant = Singe(nom_enfant)
        print(self.maman.nom, "et", self.papa.nom, "reproduisent", enfant.nom)


# Pierre mange une banane de couleur jaune
pierre = Singe(nom="Pierre")  # on crée le singe Pierre
banane_jaune = Banane(couleur="jaune")  # on crée une banane de couleur jaune
pierre.mange(banane_jaune)

# Marie mange une banane de couleur verte
marie = Singe(nom="Marie")  # on crée le singe Marie
banane_verte = Banane(couleur="verte")  # on crée une banane de couleur verte
marie.mange(banane_verte)


"""
Marie et Pierre ont un bébé qui s'appelle Robert

Deux façons de voir le problème:
* Marie copule avec Pierre: elle a un bébé qui s'appelle Robert
* Le couple Marie et Pierre se reproduisent et font un enfant nommé Robert
"""

marie.copule(copain=pierre, nom_enfant="Robert")

couple = CoupleDeSinges(maman=marie, papa=pierre)
couple.reproduit("Robert")
