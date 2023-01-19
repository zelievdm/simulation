from Roue import * # Permet d'utiliser la classe Roue se trouvant dans le meme repertoire

class Robot :
	def __init__ (self, roue_gauche, roue_droite, pos_x = 0, pos_y = 0, estEnTrainDeRouler = False) :
		self.roue_gauche = roue_gauche
		self.roue_droite = roue_droite
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.estEnTrainDeRouler = estEnTrainDeRouler # Permet de savoir si le robot est en train de rouler


	def __str__ (self) :
		"""
		Equivalent methode toString(Java)
		Permet de redéfinir la methode print(monInstance)
		""" 
		res = "Le robot en position (" + str(self.pos_x) +","+ str(self.pos_y) + ")"
		# Le test suivant permet de faire un affichage du robot selon s'il roule ou pas
		if self.estEnTrainDeRouler :
			res += "est en train de rouler"
		else :
			res += " est à l'arret"
		return res


