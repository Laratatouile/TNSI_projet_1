
### <u><span style="color:#d51515">1) Importation de la bibliothèque pillow</span></u><br>
```python
import PIL.Image
```

 On importe la librairie PIL (Pillow) qui permet de manipuler des images (ouvrir, redimensionner, convertir, etc.).

### <u><span style="color:#d51515">2) Demande de chemin de l'image</span></u><br>

```python
path = input("Enter the path to the image field : \n")
```

Le programme demande à l’utilisateur de saisir le chemin du fichier image (exemple : "image.png").

### <u><span style="color:#d51515">3) Ouverture de l'image</span></u><br>

```python
try:
    img = PIL.Image.open(path)
    img_flag = True
except:
    print(path, "Unable to find image ");
```

 On tente d’ouvrir l’image.

Si le chemin est valide → img contient l’image.

Sinon un message d’erreur s’affiche: "Unable to find image ".

### <u><span style="color:#d51515">4) Récuperation de la taille de l'image et redimensionnement</span></u><br>

```python
width, height = img.size
aspect_ratio = height / width
new_width = 120
new_height = aspect_ratio * new_width * 0.55
img = img.resize((new_width, int(new_height)))
```

 On adapte la taille pour que l’image ASCII soit lisible :

"aspect_ratio" garde les proportions de l’image.

"new_width = 120" fixe la largeur à 120 caractères.

"new_height" est calculée pour respecter les proportions de la page.

"img.resize(...)é redimensionne l’image.

### <u><span style="color:#d51515">5) Conversion en gris</span></u><br>

```python
img = img.convert('L')
```

 On convertit l’image en noir et blanc (luminance, valeurs de 0 à 255).
Cela permet d’associer chaque pixel à un caractère ASCII selon sa luminosité.

### <u><span style="color:#d51515">6) Définition des caractères ASCII</span></u><br>

```python
chars = ["@", "J", "D", "%", "*", "P", "+", "Y", "$", ",", "."]
```

 Cette liste contient les symboles utilisés pour représenter les pixels.

"@"  représente un pixel très sombre.

"."  représente un pixel clair.
Ainsi, plus le pixel est sombre plus le caractère choisi est dense.


### <u><span style="color:#d51515">7) Conversion des pixels en caractères</span></u><br>
```python
pixels = img.getdata()
new_pixels = [chars[pixel // 25] for pixel in pixels]
new_pixels = ''.join(new_pixels)
```
 Étapes :

img.getdata() récupère la valeur de luminosité de chaque pixel.

pixel // 25 ramène cette valeur entre 0 et 10 (car 255 ÷ 25 ≈ 10).

Chaque pixel est transformé en un caractère de la liste chars.

Tous les caractères sont assemblés en une seule grande chaîne "(join)".

### <u><span style="color:#d51515">8) Découpage ligne par ligne</span></u><br>
```python
new_pixels_count = len(new_pixels)
ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
ascii_image = "\n".join(ascii_image)
```

 On remet en forme :

On découpe la chaîne de caractères en lignes de largeur "new_width (120)".

On assemble les lignes avec des sauts de ligne "\n".


### <u><span style="color:#d51515">9) Sauvegarde dans un fichier texte</span></u><br>
```python
with open("ascii_image.txt", "w") as f:
    f.write(ascii_image)
```

 L’image ASCII est enregistrée dans un fichier texte "ascii_image.txt".
Ainsi, l’utilisateur peut l’ouvrir et voir l’image transformé avec des caractères.