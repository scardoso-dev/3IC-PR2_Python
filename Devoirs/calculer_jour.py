# Calculer le jour à partir d'une date
# https://fr.wikibooks.org/wiki/Curiosit%C3%A9s_math%C3%A9matiques/Trouver_le_jour_de_la_semaine_avec_une_date_donn%C3%A9e
# Méthode 3

def estBissextile(annee):
    '''
    Fonction qui permet de vérifier si une année est bissextile
        
        Paramètres: 
            annee (int): Année
       
        Retourne: 
            res (Boolean): Retourne True si l'année est bissextile, False sinon.
    '''
    # Initialisation de la valeur de retour
    res = False
    # Si l'année est uniformément divisible par 4 (reste de la division = 0), alors elle est bissextile
    if annee%4 == 0:
        res = True
    return res    


def calculerJour(date) -> str:
    '''
    Fonction qui permet de calculer le jour (Lundi, Mardi, ..etc) à partir d'une date
        
        Paramètres: 
            date (str): Une date au format chaîne de caractères (JJ/MM/AAAA ou JJ-MM-AAAA)

        Retourne: 
            jour (str): Retourne le jour de la semaine qui correspond à la 'date' passée en paramètre
    '''
    # Initialisation du jour retourné
    res = ''
    # Initialisation du dictionnaire des jours avec comme clé le reste de la division et comme valeur le jour de la semaine
    jours = { 0: 'Dimanche', 1: 'Lundi', 2:  'Mardi', 3: 'Mercredi', 4: 'Jeudi', 5: 'Vendredi', 6: 'Samedi' }
    # Création du dictionnaire des mois avec comme clé le mois en chaîne de caractères et comme valeur le nombre à ajouter selon le mois
    mois = { 'Janvier': 0, 'Février': 3, 'Mars': 3, 'Avril': 6, 'Mai': 1, 'Juin': 4, 'Juillet': 6, 'Août': 2, 'Septembre': 5, 'Octobre': 0, 'Novembre': 3, 'Décembre': 5 }
    # Création du dictionnaire des siecles avec comme clé le siecle et comme valeur le nombre à ajouter selon le siecle
    siecles = { 16: 6, 17: 4, 18: 2, 19: 0, 20: 6, 21: 4 }
    
    # On garde les deux derniers chiffres de l'année
    annee = int(date[-2:len(date)])

    # On divise l'annee par 4 en ignorant les restes
    annee = annee // 4

    # On ajoute la journée du mois à l'année
    annee += int(date[:2])


    # On ajoute a l'année, selon le mois, en récupérérant la valeur à ajouter dans le dictionnaire 'mois'
    valuesMois = list(mois.values())
    indexMois = int(date[3:5])-1
    annee += valuesMois[indexMois]

    # Si l'année est bissextile et le mois est janvier ou février, on ôte 1
    if estBissextile(int(date[-2:len(date)])) and ( (indexMois == 0 ) or (indexMois) == 1):
        annee -= 1

    # Selon le siècle, on ajoute à année la valeur récupéré dans le dictionnaires des siecles 
    annee += siecles[int(date[-4:-2])]
    
    # On divise la somme, (année de depart + la valeur de la variable 'annee') et on divise par 7, puis on garde le reste
    somme = annee + int(date[-2:len(date)]) 
    reste = somme % 7


    # Le reste représente le jour recherché, on récupére le jour à l'aide du dictionnaire des jours en recherchant par la clé (la clé = reste)
    res = jours[reste]
    return res

######## TESTS ########
date1 = '01/08/1947'
date2 = '14-02-2019'
date3 = '13-03-2004'
date4 = '13/04/1965'
date5 = '14/02/1964'
date6 = '11/07/1941'
date7 = '31/07/1967'
date8 = '01/01/1994'
date9 = '17/02/1948'
date10 = '12/05/1971'
date11 = '26/08/1946'
date12 = '03/12/1995'

print( "Le %s est un %s"%(date1, calculerJour(date1)) ) # Vendredi
print( "Le %s est un %s"%(date2, calculerJour(date2)) ) # Jeudi
print( "Le %s est un %s"%(date3, calculerJour(date3)) ) # Samedi
print( "Le %s est un %s"%(date4, calculerJour(date4)) ) # Mardi
print( "Le %s est un %s"%(date5, calculerJour(date5)) ) # Vendredi
print( "Le %s est un %s"%(date6, calculerJour(date6)) ) # Vendredi
print( "Le %s est un %s"%(date7, calculerJour(date7)) ) # Lundi
print( "Le %s est un %s"%(date8, calculerJour(date8)) ) # Samedi
print( "Le %s est un %s"%(date9, calculerJour(date9)) ) # Mardi
print( "Le %s est un %s"%(date10, calculerJour(date10)) ) # Mercredi
print( "Le %s est un %s"%(date11, calculerJour(date11)) ) # Lundi
print( "Le %s est un %s"%(date12, calculerJour(date12)) ) # Dimanche