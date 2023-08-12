##
## Déclaration de la classe
##
class Document:
    def __init__(self) -> None:
        self.titre = ""
        self.auteur = ""
        self.date_mise_a_jour = None
        self.contenu = []

    def __str__(self) -> str:
        tmp = """
        Document : %s
        Crée par : %s

        %s
        """ %(self.titre, self.auteur, self.contenu)
        return tmp

##
## Pour tester la classe
##
if __name__ == '__main__':
    A = Document()
    A.titre = "Mon premier Objet"
    A.auteur = "Mounik"
    A.contenu = "Ceci est un exemple de classe simple"
    print(A)
