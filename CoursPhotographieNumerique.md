# Imagerie numérique

## Introduction

### Un peu d'histoire

L'imagerie numérique est apparue dans les années 70. Elle a été rendue possible par l'invention du capteur CCD (Charge-Coupled Device) par Willard Boyle et George Smith. Ce capteur est capable de convertir une image en un signal électrique. Ce signal peut ensuite être numérisé et stocké dans un ordinateur.

Le premier appareil photo numérique a été inventé en 1975 par Steven Sasson. Il pesait 3,6 kg et avait une résolution de 0,01 mégapixels. Il fallait 23 secondes pour prendre une photo et 23 secondes pour l'afficher sur un téléviseur. Il fallait ensuite 23 secondes pour effacer la photo et pouvoir prendre une nouvelle photo. La photo était stockée sur une cassette audio. Il fallait 50 secondes pour transférer la photo sur un ordinateur.

Aujourd'hui, les appareils photo numériques sont beaucoup plus performants. Ils sont capables de prendre des photos de plusieurs dizaines de mégapixels en quelques millisecondes. Ils sont capables de prendre des vidéos en 4K à 60 images par seconde.

## Les images numériques

### Qu'est ce qu'un Pixel ?

Un pixel est un point de l'image. Il est défini par sa position et sa couleur. La couleur est définie par un triplet de valeurs RVB (Rouge, Vert, Bleu). Chaque valeur est comprise entre 0 et 255. 0 correspond à l'absence de couleur et 255 à la couleur la plus intense.

> Exemple : 🟥 correspondrait à un pixel de valeur (255, 0, 0)

### Composition d'une image ?

Une image numérique est une matrice de pixels. On peut imaginer une image comme un tableau à deux dimensions. Chaque case du tableau correspond à un pixel. La taille du tableau correspond à la taille de l'image. La valeur de chaque case correspond à la couleur du pixel.

```
*Exemple :*
⬛⬛⬛⬛
⬛🟥🟥⬛
🟥🟨🟨🟥
🟨🟨🟨🟨
```

*représente une petite image de 4x4 pixels.*
*Cette image correspond en fait aux valeurs suivantes :*

 | | | | |
 |:-----:|:-----:|:-----:|:-----:|
 (0, 0, 0) | (0, 0, 0) | (0, 0, 0) | (0, 0, 0) |
 (0, 0, 0) | (255, 0, 0) | (255, 0, 0) | (0, 0, 0) |
 (255, 0, 0) | (255, 255, 0) | (255, 255, 0) | (255, 0, 0) |
 (255, 255, 0) | (255, 255, 0) | (255, 255, 0) | (255, 255, 0) |

> Plus il y a de pixels, plus l'image est détaillée. La taille d'une image est exprimée en pixels. Par exemple, une image de 1920x1080 pixels contient 1920 pixels en largeur et 1080 pixels en hauteur.


### Les formats d'image

Il existe de nombreux formats d'image. Chaque format a ses avantages et ses inconvénients. Certains formats sont plus adaptés pour le stockage, d'autres pour l'affichage, d'autres pour la compression, etc.

**Les formats d'image sans perte**

Les formats d'image sans perte sont des formats qui ne modifient pas les données de l'image. Ils sont donc adaptés pour le stockage et la transmission. Ils sont cependant moins efficaces que les formats avec perte pour la compression.

Les formats d'image sans perte les plus connus sont :
- BMP
- PNG

**Les formats d'image avec perte**

Les formats d'image avec perte sont des formats qui modifient les données de l'image pour les stocker plus efficacement. Mais ils perdent de l'information. Ils sont donc moins adaptés pour le stockage et la transmission. Ils sont cependant plus efficaces que les formats sans perte pour la compression.

Les formats d'image avec perte les plus connus sont :
- JPEG
- WEBP

<br>

**Les formats d'image vectoriels**

Les formats d'image vectoriels ne stockent pas les pixels de l'image. Ils stockent des formules mathématiques qui permettent de générer l'image. On peut donc agrandir une image vectorielle sans perte de qualité. On peut imaginer une image vectorielle comme une image composée de formes géométriques.

Les formats d'image vectoriels les plus connus sont :
- SVG
- EPS
- PDF

<br>
<br>

## **Exercices :**

### Exercice 1

> Pour utiliser une image dans un programme python on peut utiliser la bibliothèque PIL (Python Imaging Library). Cette bibliothèque permet de lire et d'écrire des images dans de nombreux formats.

Pour installer la bibliothèque PIL, il faut taper la commande suivante dans un terminal :
```bash
pip install pillow
```

Voici un exemple d'utilisation de la bibliothèque PIL pour lire une image :
```python
from PIL import Image

# Charger l'image à partir du fichier
image = Image.open('Exercice1.jpg')

# Afficher les dimensions de l'image
print(image.size)

# Afficher le premier pixel de l'image
print(image.getpixel((0, 0)))

# Modifier le premier pixel de l'image
image.putpixel((0, 0), (255, 0, 0))

# Sauvegarder l'image modifiée dans un nouveau fichier
image.save('Exercice1_resultat.jpg')
```
> Ce programme est disponible dans le fichier [ExempleUtilisationPil.py](ExempleUtilisationPil.py)

Ecrire un programme pour récupérer la couleur du pixel en position (2, 2) de l'image `Exercice1.jpg`

<br>

---

<br>

### Exercice 2

<br>

    Pour convertir une image en noir et blanc, il faut remplacer la valeur de chaque pixel par la moyenne des valeurs RVB du pixel.
    
    Par exemple, le pixel (255, 0, 0) devient (85, 85, 85) car (255 + 0 + 0) / 3 = 85

Ecrire un programme pour convertir l'image `Exercice1.jpg` en noir et blanc et sauvegarder le résultat dans un nouveau fichier `Exercice2.jpg`

<br>

---

<br>
<br>

### Exercice 3

<br>

```python
# Pour créer une nouvelle image :
image2 = Image.new('RGB', (100, 100), (255, 255, 255))

image2.save('Exercice3.jpg')
```

Ecrire un programme pour créer une image de 100x100 pixels que vous remplirez avec des pixels de couleur aléatoire.

<br>

---

<br>
<br>

## Pour aller plus loin

## Meta données

Les métadonnées sont des informations sur un fichier qui permettent de préciser des informations supplémentaires sur le fichier. Par exemple, les métadonnées d'une image peuvent contenir des informations sur l'appareil photo qui a pris la photo, la date de prise de vue, la localisation, etc.

Les métadonnées sont stockées dans le fichier. Elles peuvent être lues et modifiées par des logiciels.

<br>

### **Exercice :**

Notez les métadonnées de l'image `Exercice1.jpg`

> La façon la plus simple de voir les métadonnées d'une image c'est d'ouvrir les paramètres de l'image :
> ```clic droit```
> ```paramètres```

| Données | Valeur |
|:-:|:-:|
| Dimention de l'image | ... |
| Propriétaire | ... |
| Format de fichier | ... |
| Date de création | ... |