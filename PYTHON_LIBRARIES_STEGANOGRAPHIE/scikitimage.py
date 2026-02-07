from __future__ import annotations

#ScikitImage
from skimage import io, color, filters, exposure, util, feature, transform
import numpy as np

''' 
En quoi scikit-image aide pour la stéganographie ?

Pour cacher des infos, tu peux l utiliser un peu, mais là où elle est très forte, 
c est pour la stéganoanalyse (détecter s il y a un message caché).

Typiquement :

Histogrammes & exposition
exposure.histogram, equalize_hist → repérer des anomalies dans la distribution des intensités.

Filtrage / résidus
filters.sobel, filters.laplace, filters.gaussian → extraire des résidus haute fréquence.

Beaucoup de méthodes de stéganoanalyse se basent sur ces résidus.
Statistiques locales / texture
feature.local_binary_pattern (LBP)
feature.graycomatrix, feature.graycoprops → matrices de cooccurrence (hyper classique pour les features de stégano).

Patches / blocs
util.view_as_blocks → découper une image en petits blocs, calculer des features par bloc.

Color spaces
color.rgb2ycbcr, color.rgb2lab, etc. → certaines attaques se font sur un canal précis (Y, CbCr, etc.).

En gros, tu peux :

Charger une image.
Travailler sur des versions filtrées / dérivées de cette image.
Calculer des features (histogrammes, cooccurrence, LBP…)
Donner ça à un classifieur (scikit-learn, PyTorch…) pour détecter la stéganographie.
'''



# 1. BASE : IMAGES = TABLEAUX NUMPY

from skimage import io

# Les images sont en float64 avec des valeurs dans [0, 1].
img = io.imread("../DB_STEGANOGRAPHIE/RGB-BMP Steganalysis Dataset/stegos/845162.JPG", "HELLO WORLD")   # shape (H, W, 3) pour RGB
print(img.shape, img.dtype, img)

img_float = util.img_as_float(img)      # 0–255 → 0.0–1.0
print(img_float)

img_uint8 = util.img_as_ubyte(img_float) # 0.0–1.0 → 0–255
print(img_uint8)



# 2. MODULES

from skimage import io

img = io.imread("../DB_STEGANOGRAPHIE/RGB-BMP Steganalysis Dataset/stegos/845162.JPG", "HELLO WORLD")       # charge en RGB
io.imshow(img)
io.show()

io.imsave("845162_copy.png", img)   # sauvegarde


from skimage import color

gray = color.rgb2gray(img)          # (H, W, 3) → (H, W)
hsv  = color.rgb2hsv(img)
lab  = color.rgb2lab(img)
ycbcr = color.rgb2ycbcr(img)

