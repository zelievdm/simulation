from Roue import * # Permet d'utiliser la classe Roue se trouvant dans le meme repertoire
import math
class Robot :
    def __init__ (self, roue_gauche, roue_droite, pos_x = 0, pos_y = 0, estEnTrainDeRouler = False) :
        self.roue_gauche = roue_gauche
        self.roue_droite = roue_droite
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.estEnTrainDeRouler = estEnTrainDeRouler # Permet de savoir si le robot est en train de rouler
    
    def avancer(self,vitesseVoulue_kmh) :
        """
        Fonction permet le robot à avancer avec la vitesse passée en paramètre
        """
        assert(vitesseVoulue_kmh != 0)
        assert(self.roue_droite.vMaxTourParSec == self.roue_gauche.vMaxTourParSec) # Permet de vérifier si les deux roues ont la même vitesse maximale
        
        vMaxTpS = self.roue_droite.vMaxTourParSec
        if(self.roue_droite.setVitesse(vitesseVoulue_kmh) >vMaxTpS): # si la vitesse voulue est plus grande que la vitesse maximale possible 
            self.roue_droite.setVitesse(vMaxTpS)
            self.roue_gauche.setVitesse(vMaxTpS)
        else:  # si la vitesse voulue est possible pour la roue
            self.roue_droite.setVitesse(vitesseVoulue_kmh) 
            self.roue_gauche.setVitesse(vitesseVoulue_kmh)
        self.estEnTrainDeRouler = True
        print("le robot avance avac la vitesse ",(vEnKmh + vitesseVoulue_kmh),"km/h")

    
    def reculer(self,vitesse) :

        """if(vitesse > self.roue_droite.vMaxTourParSec ):
            v = self.roue_droite.vMaxTourParSec
        if(self.roue_gauche.vTourParSec != 0 & self.roue_gauche.vTourParSec - vitesse >0):
            if(self.roue_droite.vTourParSec != 0 & self.roue_droite.vTourParSec - vitesse >0):
                self.roue_gauche.vTourParSec.setVitesse(self.roue_gauche.vTourParSec - vitesse)
                self.roue_droite.vTourParSec.setVitesse(self.roue_droite.vTourParSec - vitesse)
                print("le robot reculer avac la vitesse "+vitesse+"km/h")
                if(self.roue_droite.vTourParSec == 0 & self.roue_droite.vTourParSec == 0):
                    self.estEnTrainDeRouler = False """
                
            
    def __str__ (self) :
        """
		Equivalent methode toString(Java)
		Permet de redéfinir la methode print(monInstance)
		""" 
        res = "Le robot en position (" + str(self.pos_x) +","+ str(self.pos_y) + ")"
	    # Le test suivant permet de faire un affichage du robot selon s'il roule ou pas# 
        if (self.estEnTrainDeRouler) :
            res += "est en train de rouler"
        else :
            res += " est à l'arret"
        return res

    """
    vEnKmh = (3/25)*math.pi*(self.roue_droite.taille_cm*(10**-2))*(self.roue_droite.vTourParSec*60) # Permet de convertir la vitesse en tour/s de la roue en Km/h
    assert(self.roue_droite.vTourParSec == self.roue_gauche.vTourParSec) # Permet de vérifier si les deux roues ont la même vitesse
    """
