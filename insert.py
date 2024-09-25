from PIL import Image

# Ouvrir les images du conteneur et celle à cacher
container_image = Image.open("Paysage.jpg")
hidden_image = Image.open("Robot.jpg")

# Créer une nouvelle image pour stocker le résultat
result_image = Image.new("RGB", container_image.size)

# Boucle pour insérer chaque pixel de l'image cachée dans l'image conteneur
for x in range(container_image.width):
    for y in range(container_image.height):
        # Récupérer le pixel du conteneur et celui à cacher
        c_pixel = container_image.getpixel((x, y))
        h_pixel = hidden_image.getpixel((x, y))
        
        # Combiner les 4 bits de poids forts du conteneur avec les 4 bits de poids faibles de l'image cachée
        new_pixel = tuple((c & 0xF0) | (h >> 4) for c, h in zip(c_pixel, h_pixel))
        
        # Insérer le nouveau pixel dans l'image résultante
        result_image.putpixel((x, y), new_pixel)

# Sauvegarder l'image résultat
result_image.save("result.bmp", "BMP")

# Fermer les fichiers image
container_image.close()
hidden_image.close()
result_image.close()