# <span style="color:white; background-color:#6b6b6bff; padding:190px; padding-top:25px; padding-bottom:25px;font-size:35px">le fichier exterieur.py</span>

## <u><span style="color:#d51515">le fichier en petites etapes</span></u><br>
Le fichier exterieur.py est responsable de touts les dessins qui touchent les objets extérieurs aux batiments et qui ne bouge pas.


### <u><span style="color:#d51515">1) la fonction</span></u> `dessin_base`<br>

```python
# les dessins de base
def dessin_base(x:int):
    formes.rectangle(x-100, -100, x+20000, 250, "#13721e", True, "#13721e")
    formes.rectangle(x-100, 35, x+20000, 100, "#323232", True, "#323232")
    for i in range(1000):
        formes.ligne(i*20, 85, i*20+10, 85, "#adadad")
```

Cette fonction prend en charge un argument:<br>
- `x` : la position x du debut ou l'on va créer le parterre et la route<br>

### <u><span style="color:#d51515">1) la fonction</span></u> `soleil_obj` <u><span style="color:#d51515">et la fonction</span></u> `fonction_soleil_lune`<br>
```python
# le soleil et la lune
def soleil_obj(i:int, soleil:Turtle, screen, type:str, temps:float) -> None:
    """ fait bouger le soleil et la lune """
    temps_reste = time.time() - temps
    if temps_reste <= 5:
        # effacer l'ancien soleil
        soleil.clear()
        soleil_x = (i)*1400 + temps_reste*1400 / 5
        

        # afficher le nouveau
        if type == "soleil":
            formes.cercle(soleil_x, fonction_soleil_lune(soleil_x), 25, "#e2d257", True, "#ffe312", soleil)
        elif type == "lune":
            formes.cercle(soleil_x, fonction_soleil_lune(soleil_x), 25, "#555555", True, "#c1c1c1", soleil)


        screen.ontimer(lambda:soleil_obj(i, soleil, screen, type, temps), 20)


def fonction_soleil_lune(x:int) -> int:
    """ calcule l'arc de cercle du soleil """
    return 400 + abs(250 * math.sin(math.pi * x / 1400 ))
```

La première fonction est récursive grâce a ontimer de screen<br>
Elle prend en charge des arguments:<br>
- `i` : le nombre de boucles déjà effectuées qui permet de calculer le decalage pour les nombreuses fonctions<br>
- `soleil` : la turtle qui permet de dessiner le soleil et la lune<br>
- `screen` : screen pour permettre de ne pas relancer un grand nombre d'instances de cette classe qui permet de touches a des fonctions de l'ecran<br>
- `type` : une chaîne de caractères soit "soleil" soit "lune"<br>
- `temps` : la seconde a laquelle a debuté la première itération afin de calculer le decalage<br>

### <u><span style="color:#d51515">1) la fonction</span></u> `lampadaires` <u><span style="color:#d51515">et la fonction</span></u> `dessin_lampadaire`<br>
```python
# les lampadaires
def lampadaire(i:int) -> None:
    """ dessine les lampadaires """
    for k in range(6):
        dessin_lampadaire(i*1400+100+k*240)


def dessin_lampadaire(x:int) -> None:
    """ dessine un lampadaire a x """
    formes.ligne(x, 230, x, 150, "#606060")
    formes.triangle(x-3, 230, x+3, 230, x, 235, "#606060", True, "#606060")
```

Ces fonctions prennent en charge les argument:<br>
- `i` : le nombre de boucles déjà effectuées qui permet de calculer le decalage pour les nombreuses fonctions<br>
Pour la première et <br>
- `x` : la position a laquelle dessiner le lampadaire<br>
Pour la deuxième<br>

Ces fonctions permettent de dessiner les lampadaires.