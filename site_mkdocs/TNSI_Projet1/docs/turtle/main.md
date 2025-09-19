# le fichier main.pyw
## le fichier en petites etapes
Ce fichier est la base du projet, son extention .pyw permet de ne pas ouvrir de console a son execution.

Ce fichier possède plusieures fonctions
### la fonction `lancement`
Cette fonction ne prend pas en charge d'argument

cette fonction permet d'initialiser les différents fichiers et turtles du projet.
Elle permet egalement de lancer screen et de mettre des parametres de base.

A la fin de celle-ci elle lance la boucle principale et attend sa fermeture

### la fonction `boucle`
Cette fonction est récursive avec la fonction ontimer de screen.<br><br>
Cette fonction prend en charge 3 arguments:<br>
- soleil : la turtle qui permet de dessiner le soleil et la lune<br>
- i : le nombre de boucles déjà effectuées qui permet de calculer le decalage pour les nombreuses fonctions<br>
- screen : screen pour permettre de ne pas relancer un grand nombre d'instances de cette classe qui permet de touches a des fonctions de l'ecran<br>

Cette fonction est la boucle principale et elle lance les differentes fonctions de ce projet.

### la fonction `rue`
Cette fonction permet de dessiner les immeubles.<br><br>
Elle prend en charge un argument:<br>
- i : qui est le nombre de boucles déjà réalisées<br>

Elle va calculer a partir de ses variables le decalage et lancer la fonction de dessin d'un immeuble 5 fois


### la fonction `deplacement_camera`
Cette fonction est récursive grace a la fonction ontimer de screen
Elle prend en charge 2 arguments: <br>
 - i : le deplacement de base avant le decalage <br>
 - temps_depart : l'heure a laquelle la fonction a été lancée pour la 1ere fois

Cette fonction calcule le decalage a appliquer sur la camera en fonction du temps passé.
