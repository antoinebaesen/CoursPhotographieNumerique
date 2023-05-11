from PIL import Image

# Charger l'image à partir du fichier
image = Image.open('testImage.jpg')

# Passe l'image en noir et blanc 0 = noir, 255 = blanc
for x in range(image.width):
    for y in range(image.height):
        r, g, b = image.getpixel((x, y))
        moyenne = (r + g + b) // 3
        if moyenne < 128:
            image.putpixel((x, y), (0, 0, 0))
        else:
            image.putpixel((x, y), (255, 255, 255))

# Sauvegarder l'image modifiée dans un nouveau fichier
image.save('testImageNB.jpg')