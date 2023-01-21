from Roue import * # Permet d'utiliser la classe Roue se trouvant dans le meme repertoire
import math

class Robot :
    def __init__ (self, roue_gauche, roue_droite, pos_x = 0, pos_y = 0, estEnTrainDeRouler = False) :
        self.roue_gauche = roue_gauche
        self.roue_droite = roue_droite
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.estEnTrainDeRouler = estEnTrainDeRouler # Permet de savoir si le robot est en train de rouler
    
    def avancer(self,vitesseVoulue_kmh,tmp_enSec) :
        """
        Fonction permet le robot à avancer avec la vitesse passée en paramètre
        """
        assert(vitesseVoulue_kmh != 0)
        assert(self.roue_droite.vMaxTourParSec == self.roue_gauche.vMaxTourParSec) # Permet de vérifier si les deux roues ont la même vitesse maximale
        
        vMaxTpS = self.roue_droite.vMaxTourParSec
        tmp_enH = tmp_enSec/3600 
        vitesse = 0 
        if(self.roue_droite.setVitesse(vitesseVoulue_kmh) >vMaxTpS): # si la vitesse voulue est plus grande que la vitesse maximale possible 
            self.roue_droite.setVitesse(vMaxTpS)
            self.roue_gauche.setVitesse(vMaxTpS)
            vitesse = vMaxTpS
        else:  # si la vitesse voulue est possible pour la roue
            self.roue_droite.setVitesse(vitesseVoulue_kmh) 
            self.roue_gauche.setVitesse(vitesseVoulue_kmh)
            vitesse = vitesseVoulue_kmh
        self.estEnTrainDeRouler = True
        distance = (int)((vitesse*1000) * tmp_enH) # calcul la distance 
        self.pos_x += distance
        print("le robot avance à la vitesse ",(vitesseVoulue_kmh),"km/h")

    
    def reculer(self,vitesseVoulue_kmh,tmp_enSec) :

        """
        Fonction permet le robot à reculer avec la vitesse passée en paramètre
        """
        assert(vitesseVoulue_kmh != 0)
        assert(self.roue_droite.vMaxTourParSec == self.roue_gauche.vMaxTourParSec) # Permet de vérifier si les deux roues ont la même vitesse maximale
        
        vMaxTpS = self.roue_droite.vMaxTourParSec
        tmp_enH = tmp_enSec/3600 
        vitesse = 0 
        if(self.roue_droite.setVitesse(vitesseVoulue_kmh) >vMaxTpS): # si la vitesse voulue est plus grande que la vitesse maximale possible 
            self.roue_droite.setVitesse(vMaxTpS)
            self.roue_gauche.setVitesse(vMaxTpS)
            vitesse = vMaxTpS
        else:  # si la vitesse voulue est possible pour la roue
            self.roue_droite.setVitesse(vitesseVoulue_kmh) 
            self.roue_gauche.setVitesse(vitesseVoulue_kmh)
            vitesse = vitesseVoulue_kmh
        self.estEnTrainDeRouler = True
        distance = (int)((vitesse*1000) * tmp_enH) # calcul la distance 
        self.pos_x -= distance
        print("le robot recule à la vitesse ",(vitesseVoulue_kmh),"km/h")
                
    def arreter_urgence(self):
        """
        Arrete les roues en urgence
        """
        self.roue_gauche.setVitesse(0)
        self.roue_droite.setVitesse(0)
        self.estEnTrainDeRouler = False
        print("Le robot est à l'arret")

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
