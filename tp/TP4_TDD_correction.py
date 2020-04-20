import unittest  # import de la librairie qui permet de faire des tests unitaires


def is_palindrome(un_mot):
    """
    Un palindrome peut être lu dans les 2 sens
    On retourne le mot et on vérifie qu'on obtient la même chose
    """
    mot_a_comparer = un_mot.replace(" ", "").lower()  # on supprime les espaces et passe le mot en minuscules
    a_l_envers = ''.join(reversed(mot_a_comparer))  # on retourne le mot
    return mot_a_comparer == a_l_envers  # le mot est un palindrome s'il est identique lorsqu'on le retourne


def is_palindrome_boucle(un_mot):
    """
    On vérifie si la première lettre est égale à la dernière, la deuxième lettre est égale à l'avant-dernière, etc.
    Avantage: pas besoin de parcourir le mot en entier
    Dès qu'on trouve deux lettres différentes, on sait que le mot n'est pas un palindrome
    """
    mot_a_comparer = un_mot.replace(" ", "").lower()  # on supprime les espaces et passe le mot en minuscules
    lettres = len(mot_a_comparer)  # nombre de lettres dans le mot
    moitie = lettres // 2
    for i in range(0, moitie):
        if not mot_a_comparer[i] == mot_a_comparer[- 1 - i]:
            return False
    return True


class PalindromeTest(unittest.TestCase):

    def test_word(self):
        self.assertEqual(True, is_palindrome("kayak"))
        self.assertEqual(False, is_palindrome("toto"))

    def test_sentence(self):
        self.assertEqual(True, is_palindrome("engage le jeu que je le gagne"))
        self.assertEqual(True, is_palindrome("Karine alla en Irak"))

    def test_palindrome_boucle(self):
        self.assertEqual(True, is_palindrome_boucle("kayak"))
        self.assertEqual(False, is_palindrome_boucle("toto"))
        self.assertEqual(True, is_palindrome_boucle("engage le jeu que je le gagne"))
        self.assertEqual(True, is_palindrome_boucle("Karine alla en Irak"))
