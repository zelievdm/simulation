class Roue :
	def __init__ (self, taille_cm, vMaxTourParSec) :
		self.taille_cm = taille_cm
		self.vMaxTourParSec = vMaxTourParSec
		self.vTourParSec = 0

	def __str__ (self) :
		"""
		Equivalent methode toString(Java)
		Permet de redéfinir la methode print(monInstance)
		""" 
		res = "Roue de taille " + str(self.taille_cm) + " cm"
		
		if self.vTourParSec == 0: # Si la roue est à l'arret
			res += " est à l'arret" 

		else : # Si la roue tourne
			res += " roule à " + str(self.vTourParSec) + "tour/seconde"
		return res