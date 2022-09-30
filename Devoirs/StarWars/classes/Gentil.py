from xmlrpc.client import Boolean
from classes.Personnage import Personnage

class Gentil(Personnage):

    def __init__(self, nom, prenom, force = True):
        '''
        Constructeur de la classe Gentil qui hérite de la classe Personnage
    
            Paramètres:
                nom (str): Nom du Personnage gentil
                prenom (str): Prénom du Personnage gentil
        
        '''

        # On appel le constructeur de la classe parent (Personnage)
        super().__init__(nom, prenom)

        self.force = True



    ### ---------------------------- ###
    ###            GETTERS           ###
    ### ---------------------------- ###
    def getForce(self) -> Boolean:
        '''
        Accesseur de l'attribut force

            Retourne:
                self.force (Boolean): Retourne True ou False
        '''
        return self.force
    ### ---------------------------- ###
    ###            -------           ###
    ### ---------------------------- ###


    ### ---------------------------- ###
    ###            SETTERS           ###
    ### ---------------------------- ###
    def setForce(self, force) -> None:
        '''
        Modificateur de l'attribut force

            Paramètres:
                force (Boolean): Nouvelle valeur pour self.force
        '''
        self.force = force
        return None
    ### ---------------------------- ###
    ###            -------           ###
    ### ---------------------------- ###



    def __str__(self) -> str:
        '''
        Surchage de la méthode __str__ de la classe parent afin d'afficher un Personnage de type Gentil

            Retourne: 
                res (str): Personnage de type Gentil sous chaîne de caractères
        '''
        res = "\n***************************************************************"
        res += "\n*                             GENTIL                          *\n"
        
        # On fait appel à la __str__ de la classe parent (Personnage)
        res += super().__str__()

        return res