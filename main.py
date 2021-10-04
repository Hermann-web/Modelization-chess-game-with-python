
class Echiquier:
    def __init__(self):
        self.Liste_cases = 8*[8*[None]]

        #parcours et remplissage de la liste
        Couleur = 1 #1 pour la couleur blanche et 0 pour la couleur noir
        for ligne in range (8): 
            for colonne in range (8):
                (self.Liste_cases)[ligne][colonne] = Case(Couleur,ligne,colonne)
                Couleur = 1 - Couleur #passe de 0(noire) à 1(blanche) ou de 1(blanche) à 0(noire)

            Couleur = 1 - Couleur # la couleur d'une fin de ligne et la même qu'en début de la ligne suivante

    

class Case:
    def __init__(self,couleur,ligne,colonne): #couleur est de type booleen : 0 pour noire et 1 pour blanche
        self.Couleur  = couleur #la couleur des pieces du joueur
        self.Ligne    = ligne
        self.Colonne  = colonne
        self.Si_occupe = False
        self.Piece   = None
    
class Joueur:
    def __init__(self,couleur,echiquier = Echiquier()): #un joueur est défini dans le cadre d'un echiquier ou non
        self.Echiquier = echiquier
        self.Couleur = couleur     # couleur est une chaine de caractères: "blanche" ou "noire"
        self.Liste_pieces = [0]*16 #j'initialise la liste des pièces; 16 est le nombre initial de pièces
        self.Liste_type_pieces = ['']*16

        if self.Couleur == "noire": # les pieces noires sont au debut du jeu, dans les deux premieres lignes de l'echiquier
            liste_lignes = [0,1]
        else :                      # les pieces blanches sont au debut du jeu, dans les deux dernieres lignes
            liste_lignes = [7,6]
        
        # je parcoure la liste des pieces du joueur
        for i in range (16) : 
            if 0 <= i <= 7 : # je met les pions dans les 8 premiers elements de la liste
                self.Liste_pieces[i] = Pion() #j'instancie un objet de la classe pion
                (self.Liste_pieces[i]).Placer(echiquier,liste_lignes[1],i)
                (self.Liste_type_pieces).append("Pion")

            elif  i == 8 :
                self.Liste_pieces[i] = Roi() 
                (self.Liste_pieces[i]).Placer(echiquier,liste_lignes[0],4)
                (self.Liste_type_pieces).append("Roi")

            elif  i == 9 :
                self.Liste_pieces[i] = Dame()
                (self.Liste_pieces[i]).Placer(echiquier,liste_lignes[0],3)
                (self.Liste_type_pieces).append("Dame")

            elif 10 <= i <= 11 :
                self.Liste_pieces[i] = Tour()
                (self.Liste_type_pieces).append("Tour")

                if i ==10:
                    (self.Liste_pieces[i]).Placer(echiquier,liste_lignes[0],0)
                else:
                    (self.Liste_pieces[i]).Placer(echiquier,liste_lignes[0],7)
                

            elif 12 <= i <= 13 :
                self.Liste_pieces[i] = Cavalier()
                (self.Liste_type_pieces).append("Cavalier")
                
                if i ==12 :
                    (self.Liste_pieces[i]).Placer(echiquier,liste_lignes[0],1)
                else:
                    (self.Liste_pieces[i]).Placer(echiquier,liste_lignes[0],6)

            else :
                self.Liste_pieces[i] = Fou()
                (self.Liste_type_pieces).append("Fou")
                
                if i ==14 :
                    (self.Liste_pieces[i]).Placer(echiquier,liste_lignes[0],2)
                else:
                    (self.Liste_pieces[i]).Placer(echiquier,liste_lignes[0],5)
        

class Piece :
    def __init__(self):
        self.Case      = None #la piece n'est dans aucune case d'aucun echiquier
        self.Echiquier = None #la piece n'est utilisée dans aucun echiquier

    # cette méthode permet de mettre une piece dans une case d'un echiquier donné 
    def Placer(self,echiquier,ligne,colonne):
        case = (echiquier.Liste_cases)[ligne][colonne] #la case de l'echiquier à cette ligne et à cette colonne
        self.Case = case                               #j'associe cette case à la pièce self
        self.Echiquier = echiquier 
        case.Si_occupe = True #la case est donc occupée
        case.Piece = self     #elle est occupée par la piece self

    #cette méthode permet de deplacer une pièce d'un pas sur la diagonale
    def SeDeplacer(self,echiquier):
        #si la piece est dans l'echiquier
        
        if self.Echiquier == echiquier :
            new_colonne == (self.Case).colonne
            
            # si la prochaine position est à un pas vers le haut au vers le bas
            new_ligne = 1 + (self.Case).Ligne
            new_case  = (echiquier.Liste_cases)[new_ligne][new_colonne]

            if 0 <= new_ligne_1 < 7 and new_case.Si_occupe == False:
                new_ligne == 1 + (self.Case).Ligne
                #changer de position: monter
                Placer(self,echiquier,new_ligne,new_colonne)
                


class Pion (Piece):
    Type = "Pion"
         
    #la methode SeDeplacer est déja importée
    # Je crois que toutes les methodes publiques sont importées
    def Promotion (self,echiquier):
        ligne_piece = (self.Case).Ligne
        colonne_piece = (self.Case).Colonne
        cdt1 = self.Couleur == 1 and ligne_piece ==0
        if  cdt1 or cdt2:
            ligne   = ligne_piece
            colonne = colonne_piece
            self = Dame()
            self.Placer(echiquier,ligne,colonne)
            

    def Capturer(self,echiquier,piece):
        liste_cases = echiquier.Liste_cases

        ligne   = (self.Case).Ligne
        colonne = (self.Case).Colonne

        new_ligne   = (piece.Case).Ligne
        new_colonne = (piece.Case).Colonne

        cdt1 = (new_ligne == 1 + ligne) and (new_colonne == 1 + colonne)
        cdt1 = (new_ligne == -1 + ligne) and (new_colonne == -1 + colonne)
        if cdt1 or cdt2:
            #l'ancienne case du pion qui capture est désormais sans piece et donc n'est plus occupé
            (self.Case).Si_occupe = False
            (self.Case).Piece = None

            # actualiser la position du pillon
            self.Case = piece.Case

            
                
            
class Roi(Piece):
    Type = "Roi"
class Dame(Piece):
    Type = "Dame"
class Tour(Piece):
    Type = "Tour"
class Cavalier(Piece):
    Type = "Cavalier"
class Fou(Piece):
    Type = "Fou"


# fonction test
def Modelisation_Vulgaire():
    echiquier = Echiquier()
    joueur_1  = Joueur("blanche" , echiquier)
    joueur_2  = Joueur("noire" , echiquier)
