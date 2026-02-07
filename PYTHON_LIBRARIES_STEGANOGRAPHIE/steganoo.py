from __future__ import annotations

# STEGANO
from stegano import lsb
import cv2

'''
À quoi sert Stegano / en quoi ça aide pour la stéganographie

Stegano est une librairie Python qui implémente plusieurs techniques classiques de stéganographie, en particulier sur les images : 

LSB sur les pixels : cache un message dans les bits de poids faible des pixels.

LSB avec ensembles de positions (generators) : cache le message dans des pixels choisis selon des suites mathématiques (Eratosthène, Fibonacci, etc.) → message mieux “dispersé” dans l’image.

Canal rouge (red) : encode dans la composante rouge d un pixel.

Champ de description EXIF (exifHeader) : cache le message dans les métadonnées JPEG/TIFF.

Steganalysis : quelques fonctions pour analyser statistiquement si une image semble contenir de la LSB (parity, statistics). 
stegano.readthedocs.io
+1

Pour ton projet, ça te sert à :

Générer rapidement des jeux de données (images propres + images stego) avec différentes variantes LSB.
Tester la détection : histogrammes OpenCV + steganalysis de Stegano.
Comparer les approches : LSB simple vs LSB avec générateurs vs EXIF, etc.
'''



# 1. LSB

# 1.1 Premier exemple : cacher / révéler un texte

# Cacher un message

# secret_img = lsb.hide("../DB_STEGANOGRAPHIE/RGB-BMP Steganalysis Dataset/CALTECH-BMP-1500/C0001.bmp", "Hello Elias")
# secret_img.save("stego.png")

# # Révéler
# msg = lsb.reveal("stego.png")
# print(msg)  # -> "Hello Elias"



# 2. LSB + ENSEMBLE (GENERATORS)

''' 
Là on passe à quelque chose de plus “crypto-friendly” : tu ne caches plus ton message linéairement pixel 0,1,2,3… 
mais dans des positions définies par une suite (primes, Fibonacci, etc.).
'''

from stegano.lsb import generators

# secret_msg = "Am I hidden?"
# secret_img = lsb.hide(
#     "../DB_STEGANOGRAPHIE/RGB-BMP Steganalysis Dataset/CALTECH-BMP-1500/C0001.bmp",
#     secret_msg,
#     generators.eratosthenes()   # positions = nombres premiers
# )
# secret_img.save("stego_primes.png")

# msg = lsb.reveal("stego_primes.png", generators.eratosthenes())
# print(msg)



# 3. CACHER DANS LES METADONNEES

from stegano import exifHeader

''' 
Visuellement, l image est strictement identique (pixels inchangés).

Le message vit dans les métadonnées (EXIF), donc :

Avantage : pas de trace dans l histogramme/LSB.
Inconvénient : les métadonnées peuvent être effacées par certains logiciels / compressions.

Super intéressant pour ton projet : tu peux comparer :

Stéganographie “dans le signal” (LSB) vs
Stéganographie “dans la structure/metadata” (EXIF).
'''

# Cache le message dans le champ de description d'un JPEG
# exifHeader.hide(
#     "../DB_STEGANOGRAPHIE/RGB-BMP Steganalysis Dataset/stegos/845162.JPG",           # image de départ
#     "stego_exif.jpg",      # image résultat
#     secret_message="Hello from EXIF"
# )

# msg = exifHeader.reveal("stego_exif.jpg")
# print(msg)



# 4. CACHER DANS LA COMPOSANTE ROUGE

from stegano import red

''' 
Autre technique fournie : utiliser la composante rouge (R) d un pixel. 

En CLI tu as stegano-red hide/reveal ; en Python tu peux importer le module correspondant (suivant la version, il peut être exposé comme from stegano import red).

Principe :

La valeur R (0-255) est utilisée pour stocker l info (souvent via LSB du rouge).
Intérêt : tu peux faire des expériences comparant :
LSB classique (probablement sur tous les canaux),
LSB uniquement sur R,
effets visuels/statistiques différents.
'''



# 5. STEGANALYSIS

from stegano.steganalysis import statistics, parity
from stegano import lsb
from PIL import Image

# 1) cacher un message
secret_img = lsb.hide("../DB_STEGANOGRAPHIE/RGB-BMP Steganalysis Dataset/stegos/845162.JPG", "HELLO WORLD")
secret_img.save("stegoAnalysis.png")

# 2) ouvrir pour l'analyse
img = Image.open("stegoAnalysis.png")

# 3) analyse statistique
stat = statistics.steganalyse(img)
par = parity.steganalyse(img)
print(stat)
print(par)

