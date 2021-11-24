# Mini-projet – Tic Tac Toe
# -------------------------

# Le but de ce projet est d'écrire une version du jeu
# Tic Tac Toe dans laquelle deux joueurs humains
# s'affrontent. Une liste de listes grille donne l'état
# de la grille de jeu à tout instant.

# Par exemple, à la grille ci-dessous :
# 
# X|O|X   
#  |X|O
# O| |
# correspond la liste suivante :

grille_test = [
 ['X', 'O', 'X'], 
 [' ', 'X', 'O'], 
 ['O', ' ', ' ']
]

# Noter qu'à chaque case vide correspond la chaîne de caractères
# ' ' (et non la chaîne de caractères vide '').
# 
# Pour simplifier, à chaque tour de jeu, le joueur choisit l'endroit
# où placer son « jeton » ('X' ou 'O') en entrant un chiffre qui correspond
# à une position sur la grille :

# 0|1|2
# 3|4|5
# 6|7|8

# Question 1
# ----------

# Définir trois grilles tests :

# une grille avec une ligne gagnante:
grille_test_ligne = []

# une grille avec une colonne gagnante:
grille_test_colonne = []

# une grille avec une diagonale gagnante:
grille_test_diagonale = []

# Question 2
# ----------

def afficher_grille(grille):
    """prend en paramètre une liste de listes représentant une grille,
    et qui l'affiche comme précisé dans l'introduction du projet."""
    pass

# décommenter ces lignes pour tester votre fonction
# afficher_grille(grille_test)
# afficher_grille(grille_test_ligne)
# afficher_grille(grille_test_colonne)
# afficher_grille(grille_test_diagonale)
# recommenter les quand vous jugez que ça marche.

# Question 3
# ----------

def verifier_lignes(grille):
    """prend en paramètre une liste de listes représentant
    une grille, et vérifie si cette grille contient une ligne gagnante. La fonction renvoie 'X'
    (resp. 'O') si la grille contient une ligne gagnante avec des 'X' (resp. des 'O'), et ' '
    si aucune ligne n'est gagnante."""
    pass
            

# décommenter ces lignes pour tester votre function, laissez les décommentées
# Vous devrez peut-être les changer.

# assert(verifier_lignes(grille_test)           == ' ')
# assert(verifier_lignes(grille_test_ligne)     == 'X')
# assert(verifier_lignes(grille_test_colonne)   == ' ')
# assert(verifier_lignes(grille_test_diagonale) == ' ')

# Question 4
# ----------

def verifier_colonnes(grille):
    """prend en paramètre une liste de listes représentant
    une grille, et vérifie si cette grille contient une colonne gagnante. La fonction renvoie 'X'
    (resp. 'O') si la grille contient une ligne gagnante avec des 'X' (resp. des 'O'), et ' '
    si aucune ligne n'est gagnante."""
    pass

# décommenter ces lignes pour tester votre function, laissez les décommentées
# Vous devrez peut-être les changer.

# assert(verifier_colonnes(grille_test)           == ' ')
# assert(verifier_colonnes(grille_test_ligne)     == ' ')
# assert(verifier_colonnes(grille_test_colonne)   == 'O')
# assert(verifier_colonnes(grille_test_diagonale) == ' ')

# Question 5
# ----------

def verifier_diagonales(grille):
    """prend en paramètre une liste de listes représentant
    une grille, et vérifie si cette grille contient une diagonale gagnante. La fonction renvoie 'X'
    (resp. 'O') si la grille contient une ligne gagnante avec des 'X' (resp. des 'O'), et ' '
    si aucune ligne n'est gagnante."""
    pass

# décommenter ces lignes pour tester votre function, laissez les décommentées
# Vous devrez peut-être les changer.

# assert(verifier_diagonales(grille_test)           == ' ')
# assert(verifier_diagonales(grille_test_ligne)     == ' ')
# assert(verifier_diagonales(grille_test_colonne)   == ' ')
# assert(verifier_diagonales(grille_test_diagonale) == 'X')

# Question 6
# ----------

def verifier_alignement(grille):
    """prend en paramètre une liste de listes représentant
    une grille, et vérifie si cette grille contient une ligne,
    une colonne ou une diagonale gagnante. La fonction renvoie 'X'
    (resp. 'O') si la grille contient une ligne gagnante avec des 'X' (resp. des 'O'), et ' '
    si aucune ligne n'est gagnante."""
    pass


# décommenter ces lignes pour tester votre function, laissez les décommentées
# Vous devrez peut-être les changer.

# assert(verifier_alignement(grille_test)           == ' ')
# assert(verifier_alignement(grille_test_ligne)     == 'X')
# assert(verifier_alignement(grille_test_colonne)   == 'O')
# assert(verifier_alignement(grille_test_diagonale) == 'X')

# Question 7
# ----------

# Pour simplifier, on supposera que le coup est valide

def joue_coup(joueur,position,grille):
    """procédure qui prend en paramètre :
    - un joueur ('X' ou 'O') ;
    - une position (un chiffre de 0 à 8) ;
    - une grille (une liste de listes), et qui «joue» le coup correspondant.
      en modifiant la grille"""
    pass
    
# n'oubliez pas de tester votre fonction.
# print(grille_test)
# joue_coup('X',3,grille_test)
# print(grille_test)

# Question 8
# ----------
# Finissez le jeu en complétant ce qui suit

# Initialisation de la grille (vide)
grille = [
          [' ', ' ', ' '], 
          [' ', ' ', ' '], 
          [' ', ' ', ' ']
         ]
# Booleen fini (qui indique si la partie est terminée)
fini = False
# Chaîne de caractères joueur (qui vaut soit 'X', soit 'O')
joueur = 'X'
# Variable nb_coups qui permet de savoir quand la grille est pleine
nb_coups = 0
# Variable gagnant, passe à 'X' ou 'O' dès qu'un joueur a gagné.
gagnant = ' '

while False: # Mettez le bon test
    # On affiche la grille
    afficher_grille(grille)
    # On récupère le coup du joueur
    
    # Optionnel dans un premier temps: vérifier que le coup est valide
    # et redemendez le coup sinon dans une boucle while
    
    # On joue le coup
    
    # On vérifie s'il y a un gagnant et on sort de la boucle si c'est le cas
   
    # On incrémente la variable nb_coups
    
    # On change de joueur
        
# Ici, la partie est finie. On affiche le résultat.
# D'abord la grille...
    
# ... puis le message indiquant le vainqueur ou une partie nulle

