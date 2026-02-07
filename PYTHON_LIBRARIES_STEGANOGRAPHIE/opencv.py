from __future__ import annotations

# OpenCV
import cv2
import numpy as np
from matplotlib import pyplot as plt


'''
OpenCV (Open Computer Vision) = une grosse bibliothèque C++ avec des bindings Python pour :

Charger / sauver des images et des vidéos
Faire des opérations de base : redimensionner, recadrer, flouter, gérer les couleurs
Faire de la vision par ordinateur avancée : détection de contours, features, visages, suivi d objets, etc.

En stéganographie, elle t aide surtout à :

Lire et écrire des images facilement, dans plein de formats.
Accéder aux pixels sous forme de matrices (souvent numpy.ndarray).
Manipuler les canaux de couleur (R, G, B) pour modifier les bits LSB là où tu veux.

Faire de la stéganalyse basique :

Regarder les histogrammes des images.
Appliquer des filtres (flou, bords) pour voir des artefacts.
Comparer image originale vs image stego.

Donc : OpenCV est ton couteau suisse image/vidéo, et NumPy est ton tournevis à bits. Les deux ensemble = parfait pour stéganographie classique.
'''

# 1. LIRE ET AFFICHER UNE IMAGE

# 1.1 Lire une image

img = cv2.imread("../DB_STEGANOGRAPHIE/RGB-BMP Steganalysis Dataset/CALTECH-BMP-1500/C0001.bmp")   # ou .jpg, .bmp, etc.
print("1.1 : ")
print("Dim image :")
print(type(img))                # <class 'numpy.ndarray'>
print(img.shape)                # (hauteur, largeur, canaux)
print()
print(img)

# Attention : OpenCV travaille en BGR, pas en RGB.

h, w, c = img.shape
print("Hauteur:", h, "Largeur:", w, "Canaux:", c)
print()


# 1.2 Afficher une image

# 1.2.1 appli classique
#cv2.imshow("Mon image", img)
#cv2.waitKey(5000)   # sinon la fenêtre se ferme instantanement, 0 pour indefiniment sinon c'est en ms
#cv2.destroyAllWindows()

# 1.2.2 notebook jupyter
#img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#plt.imshow(img_rgb)
#plt.axis("off")
#plt.show()



# 2. ACCES AUX PIXELS

# Pixel en (x=10, y=20)
pixel = img[20, 10]
b, g, r = pixel
print("2 :")
print("Pixels :")
print(type(pixel))  # <class 'numpy.ndarray'>
print(pixel)        # [165 208 198]
print()

# Lire juste le canal bleu
blue_value = img[20, 10, 0]
print("Canal bleu :")
print(type(blue_value)) #<class 'numpy.uint8'>
print(blue_value)       # 165
print()

# Lire juste le canal vert
print("Canal vert :")
green_value = img[20, 10, 1]
print(green_value) # 208
print()

# Modifier un pixel (le mettre en rouge pur)
img[20, 10] = [0, 0, 255]
print("Modif pixel en rouge")
print(pixel)    #[  0   0 255]
print()

# On voit un pixel rouge apparaitre
# cv2.imshow("Mon image", img)
# cv2.waitKey(0)   # sinon la fenêtre se ferme instantanement, 0 pour indefiniment sinon c'est en ms
# cv2.destroyAllWindows()


# Exemple en Steganographie

# On récupère une valeur de pixel (0 à 255)
val = img[20, 10, 0]

# Mettre à 0 le bit de poids faible
val = val & 0b11111110  # ou val = val & 254

# Mettre le bit de poids faible à 1
val = val | 1   # val = (val & 0b11111110) | bit

# Réinjecter la valeur modifiée
img[20, 10, 0] = val
print("Changer le bit de point faible :")
print(img[20, 10])  #[  1   0 255]
print()



# 3. CANAUX DE COULEUR (B G R)

# 3.1 Separer / Fusionner les canaux 
print("3.1 :")

b, g, r = cv2.split(img)    # b, g, r sont des matrices 2D
print("separe les caneaux et on print g")
print(g)
print()

img2 = cv2.merge([b, g, r])
print("On merge les caneaux et on print la nouvelle image")
print(img2)

# Qu'un canal donc photo en noir et blanc
# cv2.imshow("Mon image", b)
# cv2.waitKey(5000)   # sinon la fenêtre se ferme instantanement, 0 pour indefiniment sinon c'est en ms
# cv2.destroyAllWindows()



# 4. CONVERSION DE COULEUR

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print("4 :")
print("On convertit l'image en gris :")
print(gray)
print()
""" 
gray.shape → (h, w) (image 2D, niveaux de gris)

Pourquoi utile pour stéganographie / stéganalyse ?

Tu peux comparer l image stego vs originale en niveaux de gris.
Tu peux regarder les contours ou les bruits de façon plus simple.
"""
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print("Valeurs HSV :")
print(hsv)
print()
print("Shape HSV :")
print(hsv.shape)
print()
''' 
HSV représente :

H = Hue (Teinte, 0-180 dans OpenCV)
S = Saturation (0-255)
V = Value (luminosité) (0-255)

Comment les couleurs changent ?

Modifier H change la couleur (bleu → vert → orange…).
Modifier S change l intensité de la couleur (saturation).
Modifier V change la luminosité.

Pourquoi c est intéressant pour la stéganographie ?

Parce que :
toucher V de ±1 est beaucoup moins visible que toucher R, G ou B directement
on peut cacher des bits dans S ou V sans changer beaucoup la perception
Le modèle HSV est plus robuste pour cacher dans la luminance.
'''

lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
print("Valeurs LAB :")
print(lab)
print()
print("Shape LAB :")
print(lab.shape)
print()

''' 
Lab = le ROI des sciences colorimétriques.

Il contient :

L : luminosité (0-100 rééchelonné en 0-255 par OpenCV)
a : axe vert ↔ rouge (environ 0-255)
b : axe bleu ↔ jaune

Lab est conçu pour être :

Perceptuellement uniforme
→ Un changement numérique constant ≃ un changement visuel constant.
Donc une modification de 1 unité dans Lab se voit beaucoup moins qu un changement de 1 dans RGB.

Pourquoi c est très utilisé en stéganographie ?

Modifier un pixel dans l'espace Lab ≠ modifier sa couleur perçue comme en RGB.
LSB sur L est très discret.
LSB sur a ou b peut être presque invisible.

Le Lab est l un des meilleurs espaces pour dissimuler des données de façon imperceptible.
'''

# Affiche l'image en noir et blanc
# cv2.imshow("Mon image", gray)
# cv2.waitKey(5000)   # sinon la fenêtre se ferme instantanement, 0 pour indefiniment sinon c'est en ms
# cv2.destroyAllWindows()



# 5. REDIMENSIONNER, RECADRER, DESSINER

# 5.1 Redimensionner

resized = cv2.resize(img, (256, 256))
# cv2.imshow("Mon image", resized)
# cv2.waitKey(5000)   # sinon la fenêtre se ferme instantanement, 0 pour indefiniment sinon c'est en ms
# cv2.destroyAllWindows()


# 5.2 Recadrer

# Crop rectangle : y1:y2, x1:x2
crop = img[50:150, 100:200]

# On a juste le coin en haut a droite
# cv2.imshow("Mon image", crop)
# cv2.waitKey(5000)   # sinon la fenêtre se ferme instantanement, 0 pour indefiniment sinon c'est en ms
# cv2.destroyAllWindows()


# 5.3 Dessiner (texte rectangle etc)

rectangle = cv2.rectangle(img, (50, 50), (150, 150), (0, 255, 0), 2)

# Ajoute un rectangle vert en haut a droite de l image
# cv2.imshow("Mon image", rectangle)
# cv2.waitKey(5000)   # sinon la fenêtre se ferme instantanement, 0 pour indefiniment sinon c'est en ms
# cv2.destroyAllWindows()

texteRectangle = cv2.putText(
    img, "Stego", (50, 40),
    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2
)

# Ajoute Stego en vert au dessus du rectangle vert
# cv2.imshow("Mon image", texteRectangle)
# cv2.waitKey(5000)   # sinon la fenêtre se ferme instantanement, 0 pour indefiniment sinon c'est en ms
# cv2.destroyAllWindows()



# 6. SAUVEGARDER UNE IMAGE

#cv2.imwrite("stego.png", img)

''' 
Attention en stéganographie :

Format :

PNG, BMP → sans perte (lossless) → mieux pour garder les bits LSB intacts.
JPG → compression destructive → détruit souvent les bits LSB → embêtant pour LSB simple.
'''



# 7. FONCTION UTILES POUR LA STEGANALYSE

# 7.1 Histogrammes

# Histogramme d'un canal (par exemple le bleu)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])  # Histogramme d'un canal (par exemple le bleu)

# plt.hist(hist)
# plt.axis("off")
# plt.show()


# Histogramme des 3 canals

# colors = ('b', 'g', 'r')
# plt.figure(figsize=(10, 5))

# for i, col in enumerate(colors):
#     hist = cv2.calcHist([img], [i], None, [256], [0, 256])
#     plt.plot(hist, color=col)

# plt.title("Histogramme des 3 canaux (B, G, R)")
# plt.xlabel("Intensité (0-255)")
# plt.ylabel("Nombre de pixels")
# plt.show()


# 7.2 Filtres et contours

blur = cv2.GaussianBlur(img, (5, 5), 0)
# cv2.imshow("Mon image", blur)
# cv2.waitKey(5000)   # sinon la fenêtre se ferme instantanement, 0 pour indefiniment sinon c'est en ms
# cv2.destroyAllWindows()
''' 
Filtre de flou gaussien

Applique un flou doux à l image.
Le noyau (5,5) correspond à la zone utilisée pour adoucir chaque pixel.
Le flou est basé sur une distribution gaussienne → le centre compte plus que les bords.

Résultat :

Réduction du bruit
Lissage des détails fins
Très utilisé avant de détecter des bords ou encoder de la stéganographie pour stabiliser les pixels

En bref : adoucir pour nettoyer l image.
'''

edges = cv2.Canny(gray, 100, 200)
# cv2.imshow("Mon image", edges)
# cv2.waitKey(5000)   # sinon la fenêtre se ferme instantanement, 0 pour indefiniment sinon c'est en ms
# cv2.destroyAllWindows()

''' 
Détection de contours (Canny Edge Detector)

Canny réalise plusieurs étapes :

Filtrage du bruit (déjà fait si tu as mis un GaussianBlur).
Calcul du gradient → repère où l image change brusquement.

Seuils 100 et 200 :

<100 = pas un bord
200 = bord sûr
Entre 100 et 200 = bord faible, accepté seulement si connecté à un bord sûr
Produit une image binaire : 0 = pas bord, 255 = bord

Résultat :

détecte les contours nets et fins
identifie les formes de l image
utile pour repérer quelles zones sont trop sensibles pour y cacher des données

En bref : extraire uniquement les contours importants.
'''




# 8. BITWISE OPERATIONS (TRES PUISSANT POUR LSB)

# OpenCV + NumPy permettent de jouer avec des masques


# 8.1 Masques 

# Créer un masque binaire
mask = np.zeros(img.shape[:2], dtype=np.uint8)
mask[50:150, 50:150] = 255  # zone blanche sur fond noir

# cv2.imshow("Mon image", mask)
# cv2.waitKey(5000)   # sinon la fenêtre se ferme instantanement, 0 pour indefiniment sinon c'est en ms
# cv2.destroyAllWindows()


# 8.2 Operations bit a bit (cv2)

''' 
Fonctions :

cv2.bitwise_and()
cv2.bitwise_or()
cv2.bitwise_xor()
cv2.bitwise_not()
'''

channel = img[:, :, 0]  # canal bleu

# enlever le LSB
channel_no_lsb = channel & 254

# insérer un bit (0 ou 1)
bit_to_hide = 1
channel_with_lsb = channel_no_lsb | bit_to_hide

# cv2.imshow("Mon image", img)
# cv2.waitKey(5000)   # sinon la fenêtre se ferme instantanement, 0 pour indefiniment sinon c'est en ms
# cv2.destroyAllWindows()


