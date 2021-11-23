from copy import copy

# La position dans le jeu est une liste croissante comme
# [1,2,3,4]
# [5,8,8,8]
# [0,0,0,0]
# l est croissante si l[i] <= l[i+1] pour tout i entre 0 et len(l) - 2

# Un coup consiste à choisir un des entiers de la liste et à le diminuer
# de un ou plus, mais la liste doit rester croissante.

# Par exemple si on part de [5,8,8,8] on peut atteindre
# les positions suivantes:
# [4,8,8,8]
# [3,8,8,8]
# [2,8,8,8]
# [1,8,8,8]
# [0,8,8,8]
# [5,7,8,8]
# [5,6,8,8]
# [5,5,8,8]

# Le premier joueur qui ne peut plus jouer à perdu.

# Question 1: quelle est la seule position qui est perdante si on joue
# avec une liste de taille 4 ?
position_perdante_4 = []

# Lisez la fonction suivante
def coups_possibles(position):
    """prend une position en entrée et retourne la liste des coups
    possibles. Chaque coups est un couple (i,d) avec i l'indice
    modifié et d la diminution qu'on lui applique"""
    coups = []
    for i in range(0,len(position)):
        # On regarde les coups possibles diminuant l'indice [i]
        # on cherche l'élément précédent dans la liste, ou 0 si i = 0
        precedent = 0 if i == 0 else position[i-1]
        # et l'élément courant
        courant = position[i]
        # les diminutions possibles sont entre 1 et
        # courant - précédent (inclus)
        for d in range(1,courant - precedent + 1):
            coups.append((i,d))
    return(coups)

# Quelques remarques:
# - les couples en python, sont comme des listes
#   (1,2) est presque pareil que [1,2]
# Mais on ne peut pas modifier un couple.

l = [1,2] # mettez un couple, ça ne marchera plus!
l[1] = 5
l.append(3)

# - l.append permet d'ajouter un élément à la fin d'une liste.
# - python possible un if pour les "expressions" sur la ligne
#       precedent = 0 if i == 0 else position[i-1]

# Question 2: Explique la différence entre les deux if de python
# ...
# ...

# Question 3: complète la fonction suivante.
def joue(position,coup):
    """joue le coup indiqué à partir de la position donnée et renvoie
    la nouvelle position"""
    (i,d) = coup
    position = copy(position)
    position[i] = position[i] - d # à modifier
    assert(position[i] >= 0)
    if i > 0:
        assert(position[i] >= position[i-1])
    return(position)

# Question 4: à quoi sert les deux lignes avec assert dans la fonction
# joue

# Question 5: la fonction suivante demande un coup à un joueur humain.
# modifie la pour qu'elle redemande un coup si la réponse du joueur
# est invalide.

def coups_humain(position,coups):
    """demande à un joueur humain de choisir un des coups possibles
    la position est utilisée pour un affichage sympathique"""
    print(position)
    for i in range(0,len(coups)):
        print("coup", i, ":", coups[i], "=>", joue(position,coups[i]))
    i = int(input("votre coup : "))
    while(i<0 or i >= len(coups)):
        print("coup invalide")
        i = int(input("votre coup : "))
    coup = coups[i]
    position = joue(position,coup)
    return(position)

# Question 6: la fonction suivante joue une partie entre deux joueurs
# humain jusqu'à la fin. Complète la.
def joue_partie(position):
    """joue une partie complète avec deux joueurs humain"""
    coups = coups_possibles(position)
    while(coups != []):
        position = coups_humain(position,coups)
        coups = coups_possibles(position)
    print("vous avez perdu")

# lance une partie
joue_partie([1,3,5,7])

# Question 7: modifie joue_partie et coup_humain pour afficher le nom
# du joueur qui doit jouer maintenant. On utilisera
# joue_parie([1,3,5,7],"Tamatoa","Simon") pour jouer une partie
# entre Simon et Tamatoa, si Tamatoa commence.

    
