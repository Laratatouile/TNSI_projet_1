# <span style="color:white; background-color:#6b6b6bff; padding:190px; padding-top:25px; padding-bottom:25px;font-size:35px">le fichier voitures.py</span>

## <u><span style="color:#d51515">le fichier en petites etapes</span></u><br>

Ce fichier ne possède qu'une seule fonction : la fonction `voiture`<br>
C'est pourquoi nous allons le decouper en parties de la fonction.<br>

```python
def voitures(heure_depart:float, t_voiture:Turtle, screen, liste_voitures:list=[[], []]) -> None:
    """ affiche les voitures """
    # variables
    proba_voiture = [5, 100]
    v_voiture = 5


    # definition des points ecrates le plus proche possible de la camera pour eviter le lag
    x_instant = round((time.time() - heure_depart) //8 * 1400)
    x_min = x_instant - 20
    x_max = x_min + 2800


    # verifier et generer les voitures sur la ligne du dessus
    if liste_voitures[0] != []:
        if not x_max - liste_voitures[0][-1] < 175:
            # generer aleatoirement une voiture
            if random.choice(range(proba_voiture[1])) < proba_voiture[0]:
                liste_voitures[0].append(x_max-5)
    else:
        if random.choice(range(proba_voiture[1])) < proba_voiture[0]:
            liste_voitures[0].append(x_max-5)
    # la ligne du dessous
    if liste_voitures[1] != []:
        if not x_min - liste_voitures[1][-1] < 175:
            # generer aleatoirement une voiture
            if random.choice(range(proba_voiture[1])) < proba_voiture[0]:
                liste_voitures[1].append(x_min+5)
    else:
        if random.choice(range(proba_voiture[0])) < proba_voiture[0]:
            liste_voitures[1].append(x_min+5)

            

    # supprimer les voitures si il y a des voitures
    if liste_voitures[0] != []:
        for i in reversed(range(len(liste_voitures[0]))):
            if not x_min < liste_voitures[0][i] < x_max:
                liste_voitures[0].pop(i)
    if liste_voitures[1] != []:
        for i in reversed(range(len(liste_voitures[1]))):
            if not x_min < liste_voitures[1][i] < x_max:
                liste_voitures[1].pop(i)

    # tout clear
    t_voiture.clear()


    # dessiner les voitures
    for i in range(len(liste_voitures[0])):
        liste_voitures[0][i] -= v_voiture
        t_voiture.shape("./turtle/images/voiture.gif")
        t_voiture.goto(liste_voitures[0][i], 120)
        t_voiture.stamp()
    for i in range(len(liste_voitures[1])):
        liste_voitures[1][i] += v_voiture
        t_voiture.shape("./turtle/images/voiture.gif")
        t_voiture.goto(liste_voitures[1][i], 85)
        t_voiture.stamp()


    screen.ontimer(lambda:voitures(heure_depart, t_voiture, screen, liste_voitures), 1)
```


### <u><span style="color:#d51515">1) de la ligne 1 a 10</span></u><br>
C'est la partie du calcul des variables.<br>
La fonction va calculer différentes variables utiles.<br>

### <u><span style="color:#d51515">2) de la ligne 14 a 31</span></u><br>
Cette partie sert a gérérer les voitures sur la route.<br>
Les voitures ne doivent pas etre trop collées les unes aux autres.<br>
Elle vérifie et génère les voitures pour les deux routes.<br>
La liste `liste_voitures` possède deux listes pour les deux sens de circulation de la route elle est initialisée dans l'en tête vide pour éviter les erreurs.<br>

### <u><span style="color:#d51515">3) de la ligne 35 a 46</span></u><br>
La fonction regarde si des voitures sont sorties de l'ecran au quel cas elle les supprimes des listes.<br>

Et elle clear toutes les voitures qu'elle va redessiner ensuite.<br>

### <u><span style="color:#d51515">3) de la ligne 49 a 62</span></u><br>
La fonction redessine toutes les voiutres présentes sur les deux routes.<br>

Elle se réitère ensuite avec la fonction ontimer de screen.<br>

