from xmlrpc.client import Boolean
from classes.Personnage import Personnage

class Mechant(Personnage):

    def __init__(self, nom, prenom, obscur = True):
        '''
        Constructeur de la classe Mechant qui hérite de la classe Personnage
    
            Paramètres:
                nom (str): Nom du Personnage méchant
                prenom (str): Prénom du Personnage méchant
        '''
        # On appel le constructeur de la classe parent (Personnage)
        super().__init__(nom, prenom)

        self.obscur = obscur



    ### ---------------------------- ###
    ###            GETTERS           ###
    ### ---------------------------- ###
    def getObscur(self) -> Boolean:
        '''
        Accesseur de l'attribut obscur

            Retourne:
                self.obscur (Boolean): Retourne True ou False
        '''
        return self.obscur
    ### ---------------------------- ###
    ###            -------           ###
    ### ---------------------------- ###


    ### ---------------------------- ###
    ###            SETTERS           ###
    ### ---------------------------- ###
    def setObscur(self, obscur) -> None:
        '''
        Modificateur de l'attribut obscur

            Paramètres:
                obscur (Boolean): Nouvelle valeur pour self.obscur
        '''
        self.obscur = obscur
        return None
    ### ---------------------------- ###
    ###            -------           ###
    ### ---------------------------- ###



    def __str__(self) -> str:
        '''
        Surchage de la méthode __str__ de la classe parent afin d'afficher un Personnage de type Mechant

            Retourne: 
                res (str): Personnage de type Mechant sous chaîne de caractères
        '''
        res = "\n***************************************************************"
        res += "\n*                            MECHANT                          *\n"

        # On fait appel à la __str__ de la classe parent (Personnage)
        res += super().__str__()

        return res