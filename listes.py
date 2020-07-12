"""Liste des classes de bases
"""

if __name__ == "__main__":
    print(__file__)
    print("Ce module ne doit pas être chargé seul")
    input()
    exit(1)
    
import colors

class FONCTIONS:
    
    @classmethod
    def get_items(cls, val_defaut = None):
        liste = {}

        for lib in cls.libelle:
            liste[lib] = val_defaut

        return liste

    @classmethod
    def get_id(cls, valeur):
        return cls.libelle.index(valeur)


    @classmethod
    def order(cls, valeur):
        idx = cls.libelle.index(valeur)
        if hasattr(cls, "ordre"):
            return cls.ordre[idx]
        else:
            return idx

    @classmethod
    def get_valof_from(cls, valeur, referentiel):
        if valeur.__class__.__name__ == "str":
            idx = cls.libelle.index(valeur)
        else:
            idx = valeur
        return getattr(cls, referentiel)[idx]

    
    @classmethod
    def get_liste_by_index(cls):
        liste = {}
        
        if hasattr(cls, "ordre"):
            for idx, lib in enumerate(cls.libelle):
                liste[cls.ordre[idx]] = lib
            
        else:
            for idx, lib in enumerate(cls.libelle):
                liste[idx] = lib

        return liste


    @classmethod
    def get_liste_by_libelle(cls):
        liste = {}
        
        if hasattr(cls, "ordre"):
            for idx, lib in enumerate(cls.libelle):
                liste[lib] = cls.ordre[idx]
            
        else:
            for idx, lib in enumerate(cls.libelle):
                liste[lib] = idx

        return liste
    

class RARETE(FONCTIONS):
    COMMUN      = 0
    NONCOMMUN   = 1
    RARE        = 2
    EPIQUE      = 3
    LEGENDAIRE  = 4
    UNIQUE      = 5
    
    libelle = (
        "Commun",
        "Non Commun",
        "Rare",
        "Epique",
        "Légendaire",
        "Unique"
    )
    
    couleur = (
        colors.fcolors.BLANC,     # COMMUN
        colors.fcolors.VERT,      # NON COMMUN
        colors.fcolors.GCYAN,     # RARE
        colors.fcolors.GJAUNE,    # EPIQUE
        colors.fcolors.GROUGE,    # LEGENDAIRE
        colors.fcolors.GMAGENTA   # UNIQUE
    )


class ATTRIBUTS(FONCTIONS):
    FORCE         = 0
    DEXTERITE     = 1
    CONSTITUTION  = 2
    INTELLIGENCE  = 3
    SAGESSE       = 4
    CHARISME      = 5
    
    libelle = (
        "Force"         ,
        "Dexterité"     ,
        "Constitution"  ,
        "Intelligence"  ,
        "Sagesse"       ,
        "Charisme"
        )

    ordre = (0,2,3,1,4,5)


class ELEMENTS(FONCTIONS):
    PHYSIQUE    = 0
    FEU         = 1
    FOUDRE      = 2
    GLACE       = 3
    TERRE       = 4
    VENT        = 5
    POISON      = 6
    LUMIERE     = 7
    TENEBRE     = 8
    
    libelle = (
        "Physique",
        "Feu"     ,
        "Foudre"  ,
        "Glace"   ,
        "Terre"   ,
        "Vent"    ,
        "Poison"  ,
        "Lumiere" ,
        "Ténèbre" 
        )


class EMPLACEMENTS(FONCTIONS) :
    TETE            = 0
    COU             = 1
    TORSE           = 2
    POIGNETS        = 3
    GANTS           = 4
    CEINTURE        = 5
    PANTALON        = 6
    CHAUSSURES      = 7
    MAINGAUCHE      = 8
    MAINDROITE      = 9
    
    libelle = (
        "Tête"       ,
        "Cou"        ,
        "Torse"      ,
        "Poignets"   ,
        "Gants"      ,
        "Ceinture"   ,
        "Pantalon"   ,
        "Chaussures" ,
        "MainGauche" ,
        "MainDroite" 
        )


class RACE(FONCTIONS):
    HUMAINS     = 0
    DEMI_ELFES  = 1
    DEMI_ORQUES = 2
    ELFES       = 3
    GNOMES      = 4
    HALFELINS   = 5
    NAINS       = 6
    
    libelle = (
        "Humains", 
        "Demi-elfes", 
        "Demi-orques", 
        "Elfes", 
        "Gnomes", 
        "Halfelins", 
        "Nains"
    )    
    
    attributs = (
        (),
        (),
        ( (ATTRIBUTS.FORCE, 2),           (ATTRIBUTS.INTELLIGENCE, -2),    (ATTRIBUTS.CHARISME, -2)),
        ( (ATTRIBUTS.DEXTERITE, -2),      (ATTRIBUTS.CONSTITUTION, -2)),
        ( (ATTRIBUTS.FORCE, -2),          (ATTRIBUTS.CONSTITUTION, 2)),
        ( (ATTRIBUTS.FORCE, -2),          (ATTRIBUTS.DEXTERITE, 2)),
        ( (ATTRIBUTS.CONSTITUTION, 2),    (ATTRIBUTS.CHARISME, -2)),
    )

    dons = (
        1, 0, 0, 0, 0, 0, 0, 
    )
    
    competences = (
        (4, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)
    )
    
    pouvoirs_speciaux = (
        (),
        ("Vision nocturne (Ext)",),
        ("Vision dans le noir",), 
        ("Vision nocturne (Ext)",),
        ("Vision nocturne (Ext)",),
        (), 
        ("Vision dans le noir",), 
    )
    
    pouvoirs_magiques =(
        (), (), (), (),
        ("communication avec les animaux",),
        (), (),
    )
        
    

class CLASSE (FONCTIONS):
    BARBARE         = 0
    BARDE           = 1
    DRUIDE          = 2
    ENSORCELEUR     = 3
    GUERRIER        = 4
    MAGICIEN        = 5
    MOINE           = 6
    PALADIN         = 7
    PRETRE          = 8
    RODEUR          = 9
    ROUBLARD        = 10
        
    libelle = (
        "Barbare", 
        "Barde", 
        "Druide", 
        "Ensorceleur", 
        "Guerrier", 
        "Magicien", 
        "Moine", 
        "Paladin", 
        "Prêtre", 
        "Rôdeur", 
        "Roublard", 
	)
    
    PV = (
        12, 6, 8, 4, 10, 4, 8, 10, 8, 8, 6
    )

    competences = (
         4, 6, 4, 2,  2, 2, 4,  2, 2, 6, 8
    )

class POUVOIRS_SPECIAUX_VOLEUR (FONCTIONS):
    
    libelle = (
        "Attaque handicapante (Ext)",
        "Esprit fuyant (Ext)",
        "Esquive extraordinaire (Ext)",
        "Opportunisme (Ext)",
        "Roulé-boulé (Ext)",
    )


class POUVOIRS_SPECIAUX (FONCTIONS):

    libelle = (
        "Absorption d’énergie (Sur)",
        "Affaiblissement ou diminution de caractéristique (Sur)",
        "Antimagie",
        "Armes manufacturées",
        "Armes naturelles",
        "Attaque de mort",
        "Attaque sonique (Sur)",
        "Bond (Ext)",
        "Caractéristiques inexistantes",
        "Change-forme (Sur)",
        "Charme et coercition",
        "Charge en puissance (Ext)",
        "Constriction (Ext)",
        "Convocation (Mag)",
        "Esquive totale et extraordinaire",
        "Etat gazeux",
        "Engloutissement (Ext)",
        "Étreinte (Ext)",
        "Guérison accélérée (Ext)",
        "Facultés psioniques (Mag)",
        "Immunité contre le feu",
        "Immunité contre les sorts (Ext)",
        "Immunité contre le froid",
        "Intangibilité",
        "invisibilité",
        "Maladies",
        "Métamorphose",
        "Mode de déplacement",
        "Odorat (Ext)",
        "Paralysie (Ext ou Sur)",
        "Passage dans l'éther",
        "Pattes arrière (Ext)",
        "Perception des vibrations (Ext)",
        "Perte de niveau",
        "Piétinement (Ext)",
        "Poison/venin (Ext)",
        "Présence terrifiante (Ext)",
        "Rayon (Mag ou Sur)",
        "Réduction des dégâts (Ext ou Sur)",
        "Regard (Sur)",
        "Régénération (Ext)",
        "Résistance à la magie (Ext)",
        "Résistance au renvoi des morts-vivants (Ext)",
        "Résistance aux énergies destructives (Ext)",
        "Sorts",
        "Souffle (Sur)",
        "Télépathie (Sur)",
        "Terreur (Mag ou Sur)",
        "Transformation (Sur)",
        "Vision et perception aveugle (Ext)",
        "Vision dans le noir",
        "Vision nocturne (Ext)",
        "Vulnérabilité à une énergie destructive",
    )
    
    
class COMPETENCES (FONCTIONS):
    
    libelle = (
        "Acrobaties",
        "Art de la magie",
        "Artisanat",
        "Bluff",
        "Concentration",
        "Connaissance",
        "Contrefaçon",
        "Crochetage",
        "Décryptage",
        "Déguisement",
        "Déplacement silencieux",
        "Désamorçage",
        "Détection",
        "Diplomatie",
        "Discrétion",
        "Dressage",
        "Equilibre",
        "Equitation",
        "Escalade",
        "Escamotage",
        "Estimation",
        "Evasion",
        "Fouille",
        "Intimidation",
        "Langue",
        "Maîtrise des cordes",
        "Natation",
        "Perception auditive",
        "Premiers secours",
        "Profession",
        "Psychologie",
        "Renseignements",
        "Représentation",
        "Saut",
        "Survie",
        "Utilisation d'objets magiques",
    )
    

class DONS (FONCTIONS):
    
    libelle = (
        "Affinité magique",
        "Amélioration des créatures convoquées",
        "Arme de prédilection",
        "Arme de prédilection supérieure",
        "Arme en main",
        "Athlétisme",
        "Attaque au galop",
        "Attaque éclair",
        "Attaque en finesse",
        "Attaque en puissance",
        "Attaque en rotation",
        "Attaques réflexes",
        "Autonome",
        "Charge dévastatrice",
        "Combat à deux armes",
        "Combat en aveugle",
        "Combat monté",
        "Coup étourdissant",
        "Course",
        "Défense à deux armes",
        "Discret",
        "Dispense de composants matériels",
        "Doigts de fée",
        "Dur à cuire",
        "Ecole renforcée",
        "Ecole supérieure",
        "Efficacité des sorts accrue",
        "Efficacité des sorts supérieure",
        "Emprise sur les morts vivants",
        "Enchaînement",
        "Endurance",
        "Esquive",
        "Expertise du combat",
        "Feu nourri",
        "Fin limier",
        "Fourberie",
        "Fraternité animale",
        "Funambule",
        "Incantation animale",
        "Interception de projectile",
        "Magie de guerre",
        "Maîtrise des sorts",
        "Maîtrise du combat à deux armes",
        "Maniement d'une arme de guerre",
        "Maniement d'une arme exotique",
        "Maniement des armes courantes",
        "Maniement des boucliers",
        "Maniement du pavois",
        "Méticuleux",
        "Négociation",
        "Parade de projectiles",
        "Persuasion",
        "Piétinement",
        "Pistage",
        "Port des armures intermédiaires",
        "Port des armures légères",
        "Port des armures lourdes",
        "Prestige",
        "Rechargement rapide",
        "Réflexes surhumains",
        "Robustesse",
        "Savoir faire mécanique",
        "Science de la destruction",
        "Science de l'initiative",
        "Science de la bousculade",
        "Science de la feinte",
        "Science de la lutte",
        "Science du combat à deux armes",
        "Science du combat à mains nues",
        "Science du contresort",
        "Science du coup de bouclier",
        "Science du critique",
        "Science du croc en jambe",
        "Science du désarmement",
        "Science du renversement",
        "Science du renvoi",
        "Science du tir de précision",
        "Souplesse du serpent",
        "Spécialisation martiale",
        "Spécialisation martiale supérieure",
        "Succession d'enchaînements",
        "Talent",
        "Tir à bout portant",
        "Tir de loin",
        "Tir de précision",
        "Tir en mouvement",
        "Tir monté",
        "Tir rapide",
        "Vigilance",
        "Vigueur surhumaine",
        "Volonté de fer",
        "Voltigeur",
    )
