"""
Aucun module utilisé.
"""
#### Fonction secondaire
CARAC_SUP = "ABCDEFGHIJKLMNOPQRSTUVWXYZÂÊÎÔÛÄËÏÖÜÀÇÉÈÙâêîôûäëïöüàçéèù',;:!.?-_"
CARAC_REPLACE = "abcdefghijklmnopqrstuvwxyzaeiouaeiouaceeuaeiouaeiouaceeu         "
def ispalindrome(p):
    """
    retourne sir la chaine de caractère est un palindrome ou non.

    arg: string object p.

    return: boolean object True or False.
    """
    # votre code ici
    tr_table = str.maketrans(CARAC_SUP, CARAC_REPLACE)
    pt = p.translate(tr_table)
    pt = pt.replace(" ", "")
    pale = pt[::-1]
    return pt == pale

#### Fonction principale

def main():
    """
    Test la fonction ispalindrome.

    arg: None.

    return: None.
    """
    # vos appels à la fonction secondaire ici
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
