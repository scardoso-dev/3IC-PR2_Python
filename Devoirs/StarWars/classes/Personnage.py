class Personnage:
    def __init__(self, nom, prenom):
        '''
        Constructeur de la classe Personnage

            Paramètres:
                nom (str): Nom du Personnage
                prenom (str): Prénom du Personnage

        '''
        self.nom = nom.upper()
        self.prenom = prenom.capitalize()



    ### ---------------------------- ###
    ###            GETTERS           ###
    ### ---------------------------- ###

    def getNom(self) -> str: 
        '''
        Accesseur de l'attribut nom

            Retourne:
                self.nom (str): Nom du personnage 
        '''
        return self.nom


    def getPrenom(self) -> str: 
        '''
        Accesseur de l'attribut prenom
            
            Returne:
                self.prenom (str): Prénom du personnage  
        '''
        return self.prenom

    ### ---------------------------- ###
    ###            -------           ###
    ### ---------------------------- ###



    ### ---------------------------- ###
    ###            SETTERS           ###
    ### ---------------------------- ###
    
    def setNom(self, nom) -> None: 
        '''
        Modificateur de l'attribut nom
            
            Paramètres :
                nom (str): Nouveau nom du personnage
        '''
        self.nom = nom.upper()


    def setPrenom(self, prenom) -> None: 
        '''
        Modificateur de l'attribut prenom
            
            Paramètres :
                prenom (str): Nouveau prénom du personnage
        '''
        self.prenom = prenom.capitalize()
    
    ### ---------------------------- ###
    ###            -------           ###
    ### ---------------------------- ###




    def __str__(self) -> str:
        '''
        Surchage de la méthode __str__ pour convertir une instance de la classe Personnage sous chaîne de caractères.
        La chaine de caractères est returnée lors de l'utilisation de cette fonction sur un objet
        ou lors de l'utilisation de la fonction print.
            
            Retourne
                res (str) : Un Personnage sous forme de chaîne de caractères
        '''
        res = "***************************************************************"
        res += "\n*                           PERSONNAGE                        *"
        res += "\n***************************************************************"
        res += "\nNom : %s" %(self.nom)
        res += "\nPrenom : %s" %(self.prenom)
        res += "\n***************************************************************\n"
        return res