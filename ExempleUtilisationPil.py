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