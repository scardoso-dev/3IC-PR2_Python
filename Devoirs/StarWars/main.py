from classes.Film import Film
from classes.Personnage import Personnage
from classes.Mechant import Mechant
from classes.Gentil import Gentil
from classes.Acteur import Acteur

# ***************************************************************************************************** #
# 2. Donnez le code pour créer 3 films sachant les informations suivantes trouvées sur Wikipédia        #
# (Vous inventerez le montant de la recette et du cout). Deux des films auront leur attribut écrit en   #
# dur, l’autre film aura ses attributs qui seront demandés interactivement à l’utilisateur.             #
# ***************************************************************************************************** #
def addFilm() -> Film:
    '''
    Fonction pour ajouter un film à l'aide d'une demande de saisie de l'utilsateur

        Retourne:
            Film (Film): Retourne le Film créé
    '''
    titre = input("Quel est le titre du film ?")
    annee = int(input("Quelle est l'année de sortie du film ?"))
    num = int(input("Quel est le numéro d'épisode ?"))
    cout = float(input("Combien à coûté le film ?"))
    recette = float(input("À combien s'élève les bénéfices du film ?"))
    return Film(titre, annee, num, cout, recette)

# ----------------------------- #
#       Trilogie originale      #
# ----------------------------- #
film1 = Film("Un nouvel espoir", 1977, 4, 11000000, 1236396014)
film2 = Film("L'Empire contre-attaque", 1980, 5, 18000000, 828850134)
print(film1,"\n\n")
print(film2,"\n\n")
# titre : Le retour du Jedi
# annee : 1983
# numero episode : 6
# cout : 32500000
# recette : 784412354
#film3 = addFilm()
#print(film3)

# ------------------------------ #
#            Prélogie            #
# ------------------------------ #
film4 = Film("La Menace fantôme", 1999, 1, 115000000, 1501589354)
film5 = Film("L'Attaque des clones", 2002, 2, 115000000, 960075068)
film6 = Film("La Revanche des Sith", 2005, 3, 113000000, 1229025345)

# ------------------------------ #
#       Troisième trilogie       #
# ------------------------------ #
film4 = Film("Le Réveil de la Force", 2015, 7, 200000000, 3004840450)
film5 = Film("Les Derniers Jedi", 2017, 8, 200000000, 1951918395)
film6 = Film("L'Ascension de Skywalker", 2019, 9, 275000000, 1589346790)



# ***************************************************************************************************** #
# 3 . Donnez le code de la création d'un personnage après avoir créé la classe Personnage. Pour ceux    #
# qui ont vécu dans une grotte depuis la sortie en 1977 du premier épisode, vous pouvez inventer        #
# des noms si vous n'en connaissez aucun.                                                               #
# ***************************************************************************************************** #


# ------------ #
#   MECHANTS   #
# ------------ #
personnage1 = Mechant("PALPATINE", 'Sheev')

print(personnage1,"\n\n")

# ------------- #
#    GENTILS    #
# ------------- #
personnage2 = Gentil("skywalker", "luke")
print(personnage2,"\n\n")

# Pour répondre à la problématique d'un acteur possède deux personnages, puisque Luke Skywalker devient
# Dark Vador au fil du temps, alors on va considérer que l'acteur de Luke à intéprété DV.
# Acteur David POWSE 
personnage3 = Mechant("skywalker", "anakin") # alias Dark Vador
print(personnage3)



# ***************************************************************************************************** #
# 4 . Créez une collection de votre choix et insérez les 3 objets Films.                                #
# ***************************************************************************************************** #
trilogie_originale = { Film("Star Wars, Un nouvel espoir", 1977, 4, 11000000, 1236396014),
                       Film("Star Wars, L'Empire contre-attaque", 1980, 5, 18000000, 828850134),
                       Film("Star Wars, Le retour du Jedi", 1983, 6, 32500000,784412354)
}



# ****************************************************************************** #
# 5. Créez une fonction qui parcourt la collection du type                       #
# précédent afin d'afficher le résultat de la str() pour chacun des objets       #
# ****************************************************************************** #
def afficheFilms(films) -> None:
    '''
    Fonction qui permet de parcourir la collection 'films' passée en paramêtre afin d'afficher
    les films à l'aide de la méthode '__str__' de la classe Film.
    
        Paramètres : 
            films (collection) : Collection de films 
    '''
    for film in films:
        print(film)
    return None



# ***************************************** #
# 6 . Testez la sur votre collection        #
# ***************************************** #
afficheFilms(trilogie_originale)
# Essai d'un ajout de Film à la collection à l'aide de la méthode add()
trilogie_originale.add(Film("Star Wars, La Menace fantôme", 1999, 1, 115000000, 1501589354))
afficheFilms(trilogie_originale)


# ***************************************************************************************************** #
# 7. Ajoutez un attribut qui sera une collection d’acteurs dans votre classe Films et un attribut tuple #
# de personnages pour un acteur. Un tuple est une collection permettant de stocker deux éléments        #
# ou plus....                                                                                           #
# ***************************************************************************************************** #
# ------------- #
# -- DONE :) -- #
# ------------- #

# ****************************************************************************************************** #
# 8 . Donnez le code pour créer un acteur incarnant deux personnages. Dans cette étude de cas, un        #
# acteur possède deux personnages parce que ce sont les personnages avec qui on l'identifie le plus.     #
# Par exemple pour Harrisson Ford, il est le plus souvent Han Solo ou Indiana Jones. (NDLR : tant pis si #
# les personnages ne sont pas dans le même film)                                                         #
# ****************************************************************************************************** #
acteur = Acteur("Ford", "Harrison", {Personnage("Han", "Solo"),Personnage("Indiana","Jones")})

# Avec un acteur et deux personnages existants dans Star Wars :)
autreActeur = Acteur("Powse", "david", {Gentil("skywalker", "luke"), Mechant("skywalker", "anakin")})

print(acteur,"\n")
print(autreActeur, "\n")



# ***************************************************************************************************** #
# 9. Ajoutez une méthode dans la classe Acteur de nom nbPersonnages() qui retourne le nombre            #
# de personnages incarnés par cet acteur.                                                               #
# ***************************************************************************************************** #
print("Nombre de personnages : "+str(autreActeur.nbPersonnages())+"\n")



# ***************************************************************************************************** #
# 10. Dans un de vos films déjà créés, ajoutez votre collection crée à la question 4 comme attribut de  #
# la classe de votre film.                                                                              #
# ***************************************************************************************************** #

# ----------------------------------------------------------------------------------------------------- #
# Définition de la fonction printFilmsOnlyTitle() pour vérifier (visuellement) les changements de Q10 - #
# ----------------------------------------------------------------------------------------------------- #
def printFilmsOnlyTitle(films) -> None:
    '''
    Fonction qui permet de parcourir la collection 'films' passée en paramêtre afin d'afficher
    le titre des films films à l'aide de la méthode 'getTitre()' de la classe Film.
    
        Paramètres : 
            films (collection) : Collection de films 
    '''
    for film in films:
        print(film.getTitre())
    return None


# ------------------------------------------------ #
# - Affichage de la collecion avant modification - #
# ------------------------------------------------ #
print("\n\n------------------- Question 10 -----------------------")
print("\nAffichage avant modification de la collection")
printFilmsOnlyTitle(film1.getFilms())

# ------------------------------------------------ #
# - Affichage de la collecion avant modification - #
# ------------------------------------------------ #
print("\nAffichage après modification de la collection")
film1.setFilms(trilogie_originale)
printFilmsOnlyTitle(film1.getFilms())
print("\n\n\n\n")




# ********************************************************************************************************** #
# 11. Ajoutez des méthodes à la classe Film :                                                                #                                                          #
#   nbActeurs() qui vous retourne le nombre d’acteurs du film                                                #
#                                                                                                            #
#   nbPersonnages() le nombre de personnages de ce film. Vous ajouterez ensuite                              #
#                                                                                                            #
#   calculBénéfice() qui retourne le montant du bénéfice et un booléen dans un duet pour savoir si le        #
#   film est bénéficiaire et si oui, de combien. Même raisonnement pour le déficit.                          #
#                                                                                                            #
#   isBefore(annee) qui retourne si True ou False le film est sortie avant une année passée en paramètre.    #
# ********************************************************************************************************** #

# -------------------- #
# - TEST nbActeurs() - #
# -------------------- #
print("\n\nFilm : %s \nNombre d'acteurs : %i" %(film1.getTitre(), film1.nbActeurs()))

# TEST nbActeurs et nbPersonnages()
acteurs = {
    Acteur("Powse", "David", {Gentil("skywalker", "luke"),Mechant("skywalker","anakin")}),
    Acteur("Ford", "Harrison", {Mechant("PALPATINE", 'Sheev')}),
    Acteur("Powse", "Allan", {Gentil("PERSONNE", "Test")})

}
film = Film("Mon film", 2006, 1, 5500, 3200, acteurs)
print("\n\nFilm : %s \nNombre d'acteurs : %i \nNombre de personnages : %i" %(film.getTitre(), film.nbActeurs(), film.nbPersonnages()))

# Test calculBenefice()
print(film.calculBenefice())

# Test isBefore()
print(film.isBefore(2022))
print(film.isBefore(2001))


# ********************************************************************************************************** #
# 12. Donnez le code d’une méthode tri() de la classe FILM qui trie les acteurs par ordre alphabétique       #
# dans la collection                                                                                         #
# ********************************************************************************************************** #

# -------------------------------------------------------------------------------------------------------------------- #
# - TEST de la méthode trieActeurs, on affichera la collection d'acteurs avant et après le trie pour la vérification - #
# -------------------------------------------------------------------------------------------------------------------- #
# Before !
acteursBeforeTrie = ""
for acteur in film.acteurs:
    acteursBeforeTrie += acteur.getNom()+" "+acteur.getPrenom()+"\n"

# After !
acteursAfterTrie = ""
film.trieActeurs()
for acteur in film.acteurs:
    acteursAfterTrie += acteur.getNom()+" "+acteur.getPrenom()+"\n"

# Affichage
print("***************************\nActeurs avant le trie :\n***************************\n%s\n\n" %(acteursBeforeTrie))
print("***************************\nActeurs après le trie :\n***************************\n%s" %(acteursAfterTrie))




# ********************************************************************************************************** #
# 13. Donnez le code d’une fonction makeBackUp qui prend en paramètre un dictionnaire de films               #
# (l’année du film étant la clé et la valeur est l’objet) et qui écrit pour chaque film la ligne suivante :  #
# l’année – le titre – le bénéfice :                                                                         #
# ********************************************************************************************************** #

def makeBackUp(films) -> None:
    '''
    Fonction qui permet d'écrire pour chaque film du dictionnaire :
    l'année - le titre - le bénéfice

        Paramètres:
            films (dict): Dictionnaire de films
        
        Ne retourne rien
    '''
    for annee in films:
        film = films[annee]
        benefice = format(round(film.calculBenefice()[1]), "0,d").replace(',', ' ')+" $"

        print("%s - %s - %s" %(annee, film.getTitre(), benefice))
    return None


# ----------------------------- #
#       Trilogie originale      #
# ----------------------------- #
trilogie_originale = { 
    '1977': Film("Star Wars, Un nouvel espoir", 1977, 4, 11000000, 1236396014), 
    '1980': Film("Star Wars, L'Empire contre-attaque", 1980, 5, 18000000, 828850134),
    '1983': Film("Star Wars, Le retour du Jedi", 1983, 6, 32500000,784412354)
}

# ------------------------------ #
#            Prélogie            #
# ------------------------------ #
prelogie = { 
    '1999': Film("Star Wars, La Menace fantôme", 1999, 1, 115000000, 1501589354), 
    '2002': Film("Star Wars, L'Attaque des clones", 2002, 2, 115000000, 960075068),
    '2005': Film("Star Wars, La Revanche des Sith", 2005, 3, 113000000, 1229025345)
}

# ------------------------------ #
#       Troisième trilogie       #
# ------------------------------ #
troisieme_trilogie = { 
    '2015': Film("Star Wars, Le Réveil de la Force", 2015, 7, 200000000, 3004840450), 
    '2017': Film("Star Wars, Les Derniers Jedi", 2017, 8, 200000000, 1951918395),
    '2019': Film("Star Wars, L'Ascension de Skywalker", 2019, 9, 275000000, 1589346790)
}

# -------------------------------------- #
# -  TEST de la fonction makeBackUp()  - #
# ---------------------------------------#
makeBackUp(trilogie_originale)
print() 
makeBackUp(prelogie)
print()
makeBackUp(troisieme_trilogie)

# ******************************************* #
# *     Fin de l'étude de cas Star Wars     * #
# ******************************************* #