import traceback
import os, json
from colors import setColor, printXY
from msvcrt import getch;
from random import randint, choice
from listes import *


class FenetreListe:
    
    def __init__(self, titre, taille, liste):
        self.ligne_selected = 0
        self.selected = False
        
        self.titre = titre
        self.liste = liste
        
        tMax = 0
        for elt in liste:
            if len(elt) > tMax: tMax = len(elt)
                
        self.tailleElt = tMax
        self.tailleValeur = taille
    
    def add(self, element, valeur):
        self.liste[element] += valeur
    
    def get(self, element):
        return self.liste[element] 
    
    @property
    def nombre(self):
        valeur = 0
        for _ in filter(lambda x:self.liste[x], self.liste):
            valeur += 1
        
        return valeur
    
    @property
    def current_element(self):
        if not self.selected:
            return None
        else:
            for idx, elt in enumerate(self.liste):
                if idx == self.ligne_selected:
                    return self.liste[elt]
            return None
    
    @current_element.setter
    def current_element(self, val):
        if self.selected:
            for idx, elt in enumerate(self.liste):
                if idx == self.ligne_selected:
                    self.liste[elt] = val
    
    def printScreen(self, posX, posY):
        self.posX = posX
        self.posY = posY
        
        # │┤ ╣║ ╗╝ ┐└ ┴ ┬├ ─ ┼ ╚ ╔╩ ╦ ╠ ═ ╬ ┘┌ █ ▄ 
        tailleMax = self.tailleElt + 5 + self.tailleValeur
        tailleG = (tailleMax -2 - len(self.titre)) // 2
        tailleD = tailleMax - len(self.titre) - tailleG - 2
        if self.selected:
            couleur_fond = colors.bcolors.GBLEU
        else:
            couleur_fond = colors.bcolors.BLEU
            
        if self.selected:
            selectedColor = colors.fcolors.GVERT
        else:
            selectedColor = colors.fcolors.ENDC
            
        setColor(selectedColor + couleur_fond)
        printXY(posX-2, posY, "┌", end="")
        print( "═"*tailleG, self.titre, "═" *tailleD, end="┐") 
        setColor(colors.fcolors.ENDC + couleur_fond)
    
        posY += 1
        objet_color_libelle = ""
        objet_color_code = None
        
        for idx, rez in enumerate(sorted(self.liste, key=self.liste_classe.order)):
            rezstr = self.liste[rez]
            
            objet = rezstr
            
            if rezstr == None: 
                rezstr = "Aucun"
                
            if self.selected and idx == self.ligne_selected:
                # ligne selectionnee                    
                if objet.__class__.__name__ == "Objet":
                    objet_color_code = RARETE.get_valof_from(objet.rarete, "couleur") # RARETE.couleur[objet.rarete]
                    objet_color_libelle = RARETE.get_valof_from(objet.rarete, "libelle") # RARETE.libelle[objet.rarete]
                    rezstr = objet.nom[:self.tailleValeur]
                    setColor(objet_color_code + couleur_fond)
                else:
                    setColor(colors.fcolors.GJAUNE + couleur_fond)
                    
                printXY(posX-2, posY, ">" )
                
            else:
                # ligne non selectionnee                    
                if objet.__class__.__name__ == "Objet":
                    rezstr = objet.nom[:self.tailleValeur]
                    # setColor(RARETE.couleur[objet.rarete] + couleur_fond)
                    setColor(RARETE.get_valof_from(objet.rarete, "couleur") + couleur_fond)
                else:
                    setColor(colors.fcolors.ENDC + couleur_fond)
                    
            if objet.__class__.__name__ == "Objet" or objet is None:
                printXY(posX, posY, ("{:" + str(self.tailleElt) + "} : {:" + str(self.tailleValeur) + "} ").format(rez, rezstr)) 
            else:
                resequip = self.depuis_equipement[rez]
                
                tailleVal1 = self.tailleValeur // 2
                tailleVal2 = self.tailleValeur - tailleVal1
                printXY(posX, posY, ("{:" + str(self.tailleElt) + "} : {:" + str(tailleVal1) + "}{:" + str(tailleVal2) + "} ").format(rez, rezstr, resequip)) 
                
            if self.selected and idx == self.ligne_selected:
                printXY(posX + self.tailleElt + self.tailleValeur + 4, posY, "<" )
    
            posY += 1
            
        setColor(selectedColor + couleur_fond)
        printXY(posX-2, posY, "└", end="")
        print("─"*tailleMax, end="┘")
        
        if hasattr(self, "points"):
            if self.points_max > 0:
                posY += 1
                setColor(colors.fcolors.ENDC)
                printXY(posX, posY, ("{:" + str(self.tailleElt) + "} :").format("Points dispo"[:self.tailleElt])) 
                setColor(colors.fcolors.GVERT)
                printXY(posX+self.tailleElt+3, posY, ("{:" + str(self.tailleValeur) + "}").format(self.points)) 
                
        elif objet_color_libelle != "":
                posY += 1
                setColor(colors.fcolors.ENDC)
                printXY(posX, posY, ("{:" + str(self.tailleElt) + "} :").format("Rareté"[:self.tailleElt])) 
                setColor(objet_color_code)
                printXY(posX+self.tailleElt+3, posY, ("{:" + str(self.tailleValeur) + "}").format(objet_color_libelle)) 
            
        setColor(colors.fcolors.ENDC )
    
    
class Caracteristique(FenetreListe):
    
    def __init__(self, forPlayer = True):
        if forPlayer:
            self.points = 20
            self.points_max = 20
            titre = "Caractéristiques"
            taille = 10
            val_defaut = 10
            
        else:
            titre = ""
            taille = 0
            val_defaut = 0
            
        self.liste_classe = ATTRIBUTS
        FenetreListe.__init__(self, titre, taille, ATTRIBUTS.get_items(val_defaut))

    
class Resistance(FenetreListe):
    
    def __init__(self, forPlayer = True):
        if forPlayer:
            titre = "Résistances"
            taille = 10
        else:
            titre = ""
            taille = 0
        
        self.liste_classe = ELEMENTS
        FenetreListe.__init__(self, titre, taille, ELEMENTS.get_items(0))

    
class Attaque(FenetreListe):
    
    def __init__(self):
        
        self.toucher = [5]
    
    
    
class Objet:
    
    def __init__(self, nom, emplacement):
        self.nom = nom
        self.emplacement = emplacement
        self.rarete = choice([RARETE.COMMUN, RARETE.NONCOMMUN, RARETE.RARE, RARETE.EPIQUE, RARETE.LEGENDAIRE, RARETE.UNIQUE])
        
        self.attaque = 0
        self.touche  = 0
        
        self.caracteristiques = Caracteristique(False)
        self.resistances = Resistance(False)
        
        # Caracteristiques
        valeur_max = 0
        nom_max = ""
        for a in range(self.rarete+1):
            valeur = randint(1,1)
            nom_attribut = choice(list(self.caracteristiques.liste))
            # ------------------------------------------
            self.caracteristiques.add(nom_attribut, valeur)
            valeur = self.caracteristiques.get(nom_attribut)
            if valeur > valeur_max:
                valeur_max = valeur
                nom_max = nom_attribut
        
        if nom_max[0].upper() in "AEIOUY":
            self.nom += " d'" + nom_max.lower()
        else:
            self.nom += " de " + nom_max.lower()
        
        # Resistances
        valeur_max = 0
        nom_max = ""
        for a in range(self.rarete): 
            valeur = randint(1,1)
            nom_resistance = choice(list(self.resistances.liste))
            # ------------------------------------------
            self.resistances.add(nom_resistance, valeur)
            valeur = self.resistances.get(nom_resistance)
            if valeur > valeur_max:
                valeur_max = valeur
                nom_max = nom_resistance
        
        if nom_max:
            if nom_max[0].upper() in "AEIOUY":
                self.nom += " d'" + nom_max.lower()
            else:
                self.nom += " de " + nom_max.lower()
    
    
class Buff_Debuff:
    
    def __init__(self, nom, duree):
        
        self.nom = nom
        self.duree = 0
        self.caracteristiques = FenetreListe.__init__(self, "Buff", 4, ATTRIBUTS.get_items())
        self.resistances = FenetreListe.__init__(self, "Buff", 4, ELEMENTS.get_items())
    
    
    
class Equipement(FenetreListe):
    
    def __init__(self, aleatoire=True):
        
        self.caracteristiques = ATTRIBUTS.get_items(0)
        self.resistances = ELEMENTS.get_items(0)
        
        liste_emplacements = EMPLACEMENTS.get_items()
        if aleatoire:
            for emplacement in liste_emplacements:
                liste_emplacements[emplacement] = Objet(emplacement, emplacement)
                
                for attribut in liste_emplacements[emplacement].caracteristiques.liste:
                    self.caracteristiques[attribut] += liste_emplacements[emplacement].caracteristiques.liste[attribut]
                
                for element in liste_emplacements[emplacement].resistances.liste:
                    self.resistances[element] += liste_emplacements[emplacement].resistances.liste[element]
                
        self.liste_classe = EMPLACEMENTS
        FenetreListe.__init__(self, "Equipement", 40, liste_emplacements)

    
    def print_caracteristiques(self):
        if self.selected:
            objet = self.current_element
            
            if objet != None:
                posY = self.posY + len(self.liste) + 5
                couleur_fond = colors.bcolors.BLEU
                
                printXY(self.posX, posY-2, objet.nom)
                
                coinHD = "┐"
                coinBD = "┘"
                # Resistances
                if objet.resistances.nombre:
                    decalX = 29
                    setColor(colors.fcolors.GVERT + couleur_fond)
                    
                    printXY(self.posX-2+decalX, posY-1, "┌", end="")
                    titre = "{} {} {}".format("═"*6, "Résistances", "═"*6)
                    print( titre, end="┐") 
                    
                    setColor(colors.fcolors.ENDC + couleur_fond)
                    nombre = 0
                    for idx, res in enumerate(objet.resistances.liste):
                        valeur = objet.resistances.liste[res]
                        if valeur > 0:
                            printXY(self.posX+decalX, posY+nombre, "{:12} : {:4}     ".format(res, valeur))
                            nombre += 1
    
                    setColor(colors.fcolors.GVERT + couleur_fond)
                    printXY(self.posX-2+decalX, posY+nombre, "└", end="")
                    print("─"*len(titre), end="┘")
                
                # Caracteristiques
                if objet.caracteristiques.nombre:
                    if objet.resistances.nombre:
                        coinHD = "┬"
                    
                    if objet.caracteristiques.nombre == objet.resistances.nombre:
                        coinBD = "┴"
                        
                    setColor(colors.fcolors.GVERT + couleur_fond)
                    printXY(self.posX-2, posY-1, "┌", end="")
                    titre = "{} {} {}".format("═"*5, "Caracteristiques", "═"*5)
                    print( titre, end=coinHD) 
                    
                    setColor(colors.fcolors.ENDC + couleur_fond)
                    nombre = 0
                    for idx, a in enumerate(objet.caracteristiques.liste):
                        valeur = objet.caracteristiques.liste[a]
                        if valeur > 0:
                            printXY(self.posX, posY+nombre, "{:12} : {:4}        ".format(a, valeur))
                            nombre += 1
    
                    setColor(colors.fcolors.GVERT + couleur_fond)
                    printXY(self.posX-2, posY+nombre, "└", end="")
                    print("─"*len(titre), end=coinBD)
                
        setColor(colors.fcolors.ENDC)
    
    
class Player:
    
    def __init__(self, nom, classe, race):
        self.nom = nom 
        self.classes = ()
        self.race = race 
        self.niveau = 0
        # Points de Vie  [en cours, maximum]
        self.PV = [0, 0]
        # Points de Mana [en cours, maximum]
        self.PM = [0, 0]
        
        self.attaque = Attaque()
        
        self.caracteristiques = Caracteristique()
        self.resistances = Resistance()
        
        self.equipement = Equipement()
        
        self.caracteristiques.depuis_equipement = self.equipement.caracteristiques
        
        # Ajout des attributs de Race
        for attribut, valeur in RACE.attributs[self.race]:
            attr_lib = ATTRIBUTS.libelle[attribut]
            self.caracteristiques.depuis_equipement[attr_lib] += valeur

        self.resistances.depuis_equipement = self.equipement.resistances
        
        self.nombre_dons = 0
        self.dons = {}
        self.nombre_competences = 0
        self.competences = {}
        
        
        self.buff = []
        self.debuff = []
    
        self.add_level(classe)
        
    
    def add_level(self, classe):
        self.niveau += 1
        self.classes += (classe,)
        self.caracteristiques.points += 1
        
        # Ajoute les PV de la nouvelle classe au max de PV
        self.PV[1] += randint(1, CLASSE.get_valof_from(classe, "PV")) # CLASSE.PV[classe])
        # Remet les PVs au max
        self.PV[0] = self.PV[1]
        
        # ajout du nombre de Dons dus à la race
        # self.nombre_dons += RACE.dons[self.race]
        self.nombre_dons += RACE.get_valof_from(self.race,"dons")
        if self.niveau == 1:
            # self.nombre_competences = RACE.competences[self.race][0]
            self.nombre_competences += RACE.get_valof_from(self.race,"competences")[0]
        else:
            # self.nombre_competences = RACE.competences[self.race][1]
            self.nombre_competences += RACE.get_valof_from(self.race,"competences")[1]
            
        # self.nombre_competences = CLASSE.competences[classe]
        self.nombre_competences += CLASSE.get_valof_from(classe,"competences")
    
    
    @property
    def current_fenetre(self):
        for fenetre in (self.caracteristiques, self.resistances, self.equipement):
            if fenetre.selected:
                return fenetre
        return None
    
    def imprime(self):
        setColor(colors.bcolors.NOIR)
        print(" ")
        os.system("cls")
        printXY(2, 2, "Nom    :", self.nom)
        printXY(3, 3, "Niveau :", self.niveau)
        
        classes = {}
        for classe in self.classes:
            classes[classe] = 1 + classes.get(classe, 0)
            
        classe_str = ""    
        for classe in classes:
            classe_str += f"{CLASSE.libelle[classe]} ({classes[classe]}), "
            
        printXY(3, 4, "Classe :", classe_str[:-2])
        
        printXY(33, 3, "Race :", RACE.get_valof_from(self.race, "libelle") ) # RACE.libelle[self.race])
        
        printXY(60, 3, "Vie  :", "{:4} / {:4}".format(*self.PV))
        printXY(90, 3, "Mana :", "{:4} / {:4}".format(*self.PM))
        
        printXY(3, 19, "Nombre de dons :", self.nombre_dons)
        printXY(3, 20, "Nombre de compétences :", self.nombre_competences)
        
        self.caracteristiques.printScreen(5, 6)
        self.resistances.printScreen(38, 6)
        self.equipement.printScreen(67, 6)
        self.equipement.print_caracteristiques()


class Partie:
    
    def __init__(self):
        self.players = []
        self.player_id = 0
        self.max_players = 0
        
        tryon = Player("Tryon", CLASSE.BARBARE, RACE.GNOMES)
        tryon.add_level(CLASSE.ROUBLARD)
        tryon.add_level(CLASSE.ROUBLARD)
        
        self.players.append(tryon)
        self.players.append(Player("Ammy" , CLASSE.ENSORCELEUR, RACE.ELFES))
        self.players.append(Player("Elsa" , CLASSE.PRETRE     , RACE.HUMAINS))
        self.players.append(Player("Yisa" , CLASSE.ROUBLARD   , RACE.DEMI_ORQUES))
        self.max_players += len(self.players)
        
        self.current_player = self.players[self.player_id]
        

    def menu (self):
        
        k = None
        special = False
        while k != b'\x1b':
            setColor(colors.fcolors.ENDC)
            setColor(colors.bcolors.NOIR)

            os.system("cls")
            
            couleur_fond = colors.bcolors.BLEU
            posX, posY = 30, 10
            
            # │┤ ╣║ ╗╝ ┐└ ┴ ┬├ ─ ┼ ╚ ╔╩ ╦ ╠ ═ ╬ ┘┌ █ ▄ 
            setColor(couleur_fond)
            
            printXY(posX+40, posY, "┐" )
            printXY(posX, posY, "─"*16, " Menu ", "─"*16 )
            printXY(posX-1, posY, "┌" )
            posY += 1
            for ligne in range(10):
                printXY(posX-1, posY+ligne, "│" + " "*40 + "│")
                
            posY += 1
            printXY(posX+5, posY, "F1  ", "Gestion des joueurs" )
            
            posY += 7
            printXY(posX+5, posY, "Esc ", "Sortie" )
            posY += 2
            printXY(posX+40, posY, "┘" )
            printXY(posX, posY, "─"*40 )
            printXY(posX-1, posY, "└" )
            
            if k:
                printXY(5, 40, "Key:", k)
                if special:
                    printXY(5, 41, "Special")
                
            print(end="", flush=True)
            k = getch()
            if k == b'\x00': 
                k = getch()
                special = True
            
                if k == b';':  # Touche F1
                    self.gestion_joueurs()
                    
                elif  k == b'<': # Touche F2
                    pass

                elif  k == b'=': # Touche F3
                    pass

                elif  k == b'>': # Touche F4
                    pass
                    
            else:
                printXY(5, 42, "Key:", k)
                special = False
        
        
    def gestion_joueurs(self):
        
        k = None
        special = False
        while k != b'\x1b':
            self.current_player.imprime()
            if k:
                printXY(5, 40, "Key:", k)
                if special:
                    printXY(5, 41, "Special")
                
            print(end="", flush=True)
            k = getch()
            if k == b'\xe0': 
                k = getch()
                special = True
                if k == b'K': # Fleche Gauche
                    liste_fenetres = ((self.current_player.caracteristiques, self.current_player.equipement), 
                                      (self.current_player.resistances, self.current_player.caracteristiques), 
                                      (self.current_player.equipement, self.current_player.resistances))
                    
                    for (fen_src, fen_dest) in liste_fenetres:
                        if fen_src.selected: 
                            fen_src.selected = False
                            fen_dest.selected  = True
                            break
                    else:
                        liste_fenetres[-1][0].selected = True
                    
                elif k == b'M': # Fleche Droite
                    liste_fenetres = ((self.current_player.caracteristiques, self.current_player.resistances), 
                                      (self.current_player.resistances, self.current_player.equipement), 
                                      (self.current_player.equipement, self.current_player.caracteristiques))
                                      
                    for (fen_src, fen_dest) in liste_fenetres:
                        if fen_src.selected: 
                            fen_src.selected = False
                            fen_dest.selected  = True
                            break
                    else:
                        liste_fenetres[0][0].selected = True
                            
                elif k == b'H': # Fleche Haut
                    if self.current_player.current_fenetre:
                        temp_selected = self.current_player.current_fenetre.ligne_selected - 1
                        if temp_selected < 0:
                            self.current_player.current_fenetre.ligne_selected = len(self.current_player.current_fenetre.liste)-1
                        else:
                            self.current_player.current_fenetre.ligne_selected = temp_selected
                    
                elif k == b'P': # Fleche Bas
                    if self.current_player.current_fenetre:
                        self.current_player.current_fenetre.ligne_selected += 1
                        if self.current_player.current_fenetre.ligne_selected >= len(self.current_player.current_fenetre.liste):
                            self.current_player.current_fenetre.ligne_selected = 0
                            
                elif k == b'I': # Fleche Page Up
                    self.player_id -= 1
                    if self.player_id < 0: self.player_id = self.max_players - 1
                    self.current_player = self.players[self.player_id]
                        
                elif k == b'Q': # Fleche Page Down
                    self.player_id += 1
                    if self.player_id > self.max_players - 1: self.player_id = 0
                    self.current_player = self.players[self.player_id]
                        
            else:
                special = False
                if k == b'\x1b': # Touche Echap
                    if self.current_player.caracteristiques.selected: 
                        self.current_player.caracteristiques.selected = False
                        k = None
                    if self.current_player.resistances.selected: 
                        self.current_player.resistances.selected = False
                        k = None
                    if self.current_player.equipement.selected: 
                        self.current_player.equipement.selected = False
                        k = None
                        
                elif k == b'+': # Touche '+'
                    if self.current_player.current_fenetre:
                        if hasattr(self.current_player.current_fenetre, "points"):
                            if self.current_player.current_fenetre.points > 0:
                                self.current_player.current_fenetre.points -= 1
                                self.current_player.current_fenetre.current_element += 1
                    
                elif k == b'-': # Touche '-'
                    if self.current_player.current_fenetre:
                        if hasattr(self.current_player.current_fenetre, "points"):
                            if self.current_player.current_fenetre.current_element > 1:
                                self.current_player.current_fenetre.points += 1
                                self.current_player.current_fenetre.current_element -= 1


    def run (self):
        # self.gestion_joueurs()
        self.menu()

        
try:
    partie = Partie()
    partie.run()
    
    
except Exception as e:
    print(colors.fcolors.GROUGE)
    print("Erreur:",e)
    print(traceback.print_exc(), colors.fcolors.ENDC)
    getch()
        
print("\nappuyez sur une touche", end="", flush=True)
