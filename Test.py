from Robot import * # Permet d'utiliser la classe Robot se trouvant dans le meme repertoire
from Roue import * # Permet d'utiliser la classe Roue se trouvant dans le meme repertoire

# instanciation de deux roues
r_gauche = Roue(3,10)
r_droite = Roue(3,10)

# affichage de chaque roue
print(r_gauche) # affichage --> Roue de taille 3 cm est à l'arret
print(r_droite) # affichage --> Roue de taille 3 cm est à l'arret


# instanciation d'un robot, prenant en parametre les deux roue créer précédemment
robot = Robot(r_gauche,r_droite)

# affichage du robot
print(robot) # affichage --> Le robot en position (0,0) est à l'arret

# avancer le robot par le modification la vitesse des roues d'un robot 
robot.avancer(1)

robot.avancer(1)

robot.reculer(2)
print(robot)
