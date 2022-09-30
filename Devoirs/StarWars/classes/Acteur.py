class Acteur:
    def __init__(self, nom, prenom, personnages = ()):
        '''
        Constructeur de la classe Acteur

            Paramètres:
                nom (str): Nom de l'acteur
                prenom (str): Prénom de l'acteur
                personnages (tuple): Tuple de personnages pour un acteur

        '''
        self.nom = nom.upper()
        self.prenom = prenom.capitalize()
        self.personnages = tuple(personnages)



    ### ---------------------------- ###
    ###            GETTERS           ###
    ### ---------------------------- ###
    
    def getNom(self) -> str: 
        '''
        Accesseur de l'attribut nom
            
            Retourne:
                self.nom (str): Nom de l'acteur 
        '''
        return self.nom


    def getPrenom(self) -> str: 
        '''
        Accesseur de l'attribut prenom
            
            Returne:
                self.prenom (str): Prénom de l'acteur  
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
                nom (str): Nouveau nom d'acteur
        '''
        self.nom = nom.upper()


    def setPrenom(self, prenom) -> None: 
        '''
        Modificateur de l'attribut prenom
            
            Paramètres :
                prenom (str): Nouveau prénom d'acteur
        '''
        self.prenom = prenom.capitalize()

    ### ---------------------------- ###
    ###            -------           ###
    ### ---------------------------- ###


    def nbPersonnages(self) -> int:
        '''
        Méthode qui retourne le nombre de personnages joués par un acteur

            Retourne:
                res (int): Nombre de personnages joués par l'acteur 
        '''
        res = len(self.personnages)
        return res

        
    def __str__(self) -> str:
        '''
        Surchage de la méthode __str__ pour convertir une instance de la classe Acteur sous chaîne de caractères.
        La chaine de caractères est returnée lors de l'utilisation de cette fonction sur un objet
        ou lors de l'utilisation de la fonction print.
            
            Retourne
                res (str) : Un Acteur sous forme de chaîne de caractères
        '''
        res = "***************************************************************"
        res += "\n*                           ACTEUR                        *"
        res += "\n***************************************************************"
        res += "\nNom : %s" %(self.nom)
        res += "\nPrenom : %s" %(self.prenom)
        res += "\n***************************************************************\n"
        for personnage in self.personnages: 
            res += personnage.__str__()
        return res