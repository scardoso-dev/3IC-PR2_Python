import collections
from xmlrpc.client import Boolean
class Film:
    def __init__(self, titre, annee, num, cout, recette, acteurs = {}, films = {}):
        '''
        Constructeur de classe Film

            Paramètres:
                titre (str): Titre du film
                annee (int): Année de sortie du film
                num (int): Numéro d'épisode
                cout (int): Budget demandé pour faire le film
                recette (int): Recette du film
                acteurs (collection): Collection des acteurs présents dans le film
        '''

        self.titre = titre
        self.annee = annee
        self.num = num
        self.cout = cout
        self.recette = recette
        self.acteurs = acteurs
        # Ajout d'une collection de films (question 10)
        self.films = films



    ### ---------------------------- ###
    ###            GETTERS           ###
    ### ---------------------------- ###

    def getTitre(self) -> str: 
        '''
        Accesseur de l'attribut titre

            Retourne:
                self.titre (str): Titre du film 
        '''
        return self.titre

    def getAnnee(self) -> int: 
        '''
        Accesseur de l'attribut Annee

            Retourne:
                self.annee (int): Année de sortie du film 
        '''
        return self.annee

    def getNum(self) -> int: 
        '''
        Accesseur de l'attribut num

            Retourne:
                self.num (int): Numéro d'épisode  
        '''
        return self.num

        
    def getCout(self) -> int: 
        '''
        Accesseur de l'attribut cout

            Retourne:
                self.cout (int): Coût demandé pour effectuer le film  
        '''
        return self.cout

    def getRecette(self) -> int: 
        '''
        Accesseur de l'attribut recette
            
            Returne:
                self.recette (int): Recette du film  
        '''
        return self.recette

    def getActeurs(self) -> collections:
        '''
        Accesseur de l'attribut acteurs (collections)

            Retourne:
                self.acteurs (collections): Collections d'acteurs
        '''
        return self.acteurs

    def getFilms(self) -> collections:
        '''
        Accesseur de l'attribut films (collections)

            Retourne:
                self.films (collections): Collections de filmss
        '''
        return self.acteurs
    ### ---------------------------- ###
    ###            -------           ###
    ### ---------------------------- ###



    ### ---------------------------- ###
    ###            SETTERS           ###
    ### ---------------------------- ###

    def setTitre(self, titre) -> None: 
        '''
        Modificateur de l'attribut titre
            
            Paramètres :
                titre (str): Nouveau titre
        '''
        self.titre = titre


    def setAnnee(self, annee) -> None: 
        '''
        Modificateur de l'attribut annee
            
            Paramètres :
                annee (int): Nouvelle année de sortie de film
        '''
        self.annee = annee


    def setNum(self, num) -> None: 
        '''
        Modificateur de l'attribut annee
            
            Paramètres :
                num (int): Nouveau numéro d'épisode du film
        '''
        self.num = num

    def setCout(self, cout) -> None: 
        '''
        Modificateur de l'attribut cout
            
            Paramètres :
                cout (float): Nouveau coût demandé pour effectuer le film 
        '''
        self.cout = cout

    def setRecette(self, recette) -> None: 
        '''
        Modificateur de l'attribut recette
            
            Paramètres :
                recette (float): Nouvelle recette du film
        '''
        self.recette = recette

    def setActeurs(self, acteurs) -> None:
        '''
        Modificateur de l'attribut acteurs

            Paramètres: 
                acteurs (collections): Nouvelle colection d'acteurs
        '''
        self.acteurs = acteurs

    def setFilms(self, acteurs) -> None:
        '''
        Modificateur de l'attribut films

            Paramètres: 
                films (collections): Nouvelle colection de films
        '''
        self.acteurs = acteurs
    ### ---------------------------- ###
    ###            -------           ###
    ### ---------------------------- ###



    
    def nbActeurs(self) -> int:
        '''
        Méthode qui permet de savoir le nombre d'acteurs présents dans le film
            
            Retourne:
                (int) Le nombre d'acteurs présents dans le film
        '''
        return len(self.acteurs)



    def nbPersonnages(self)->int:
        '''
        Méthode qui permet de retourner le nombre total de personnages dans le film

            Retourne: 
                res (int): Nombre total de personnages dans le film
        '''
        res = 0
        # On parcours chaque acteur de la collection d'acteurs, et on appelle la méthode 
        # nbPersonnages() de la classe Acteur (On effectue la somme des personnages de chaque acteur)
        for acteur in self.acteurs:
            res += acteur.nbPersonnages()
        return res



    def calculBenefice(self) -> tuple():
        '''
        Méthode qui permet de savoir si le film à réalisé du bénéfice et retourne True ainsi que le nombre total de bénéfices.
        Dans le cas contraire, ça retourne False et le montant de déficit du film.

            Retourne:
                res (tuple): True avec le montant des bénéfices ou False avec le montant de bénéfices en négatif (déficit).
        '''
        isBenefice = False
        if self.recette > self.cout:
            isBenefice = True
        
        if isBenefice == True:
            res = (True, self.recette - self.cout)
        else:
            res = (False, self.recette - self.cout) 
        return res



    def isBefore(self, annee) -> Boolean:
        '''
        Méthode permettant de savoir si un film est sortie avant une année passé en paramètre

            Paramètres: 
                annee (int): Année à comparer avec l'annee de sortie du film

            Retourne:
                res (Boolean): Retourne true si le film est sortie avant l'année passé en paramètre, False sinon.
        '''
        res = False
        if self.annee < annee:
            res = True
        return res



    def trieActeurs(self) -> None:
        '''
        Méthode qui permet de trier les acteurs par ordre alphabétique sur le nom et le prénom
        '''
        self.acteurs = sorted(self.acteurs, key=lambda acteur: (acteur.getNom(), acteur.getPrenom()))
        return None



    def __str__(self) -> str:
        '''
        Surchage de la méthode __str__ pour regarder une instance de la classe Film sous chaîne de caractères.
        La chaine de caractères est returnée lors de l'utilisation de cette fonction sur un objet
        ou lors de l'utilisation de la fonction print.
            
            Retourne
                Un film sous forme de chaîne de caractères
        '''
        res = "***************************************************************"
        res += "\n*                           FILM                              *"
        res += "\n***************************************************************"
        res += "\nTitre : %s" %(self.titre)
        res += "\nAnnee : %i" %(self.annee)
        res += "\nNumero d'episode : %i" %(self.num)
        res += "\nCout : "+format(round(self.cout), "0,d").replace(',', ' ')+" $"
        res += "\nRecette : "+format(round(self.recette), "0,d").replace(',', ' ')+" $"
        res += "\n***************************************************************"
        return res
