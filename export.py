from PIL import Image

# Ouvrir l'image contenant le secret
container_image = Image.open("result.bmp")

# Créer une nouvelle image pour stocker l'image extraite
extracted_image = Image.new("RGB", container_image.size)

# Boucle pour extraire chaque pixel de l'image cachée
for x in range(container_image.width):
    for y in range(container_image.height):
        # Récupérer le pixel de l'image contenant le secret
        c_pixel = container_image.getpixel((x, y))
        
        # Extraire les 4 bits de poids faibles et les déplacer vers la gauche
        new_pixel = tuple((c & 0x0F) << 4 for c in c_pixel)
        
        # Insérer le nouveau pixel dans l'image extraite
        extracted_image.putpixel((x, y), new_pixel)

# Sauvegarder l'image extraite
extracted_image.save("extracted_image.bmp", "BMP")

# Fermer les fichiers image
container_image.close()
extracted_image.close()