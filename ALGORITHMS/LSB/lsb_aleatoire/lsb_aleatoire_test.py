from __future__ import annotations

import sys
from pathlib import Path

import cv2

script_dir = Path(__file__).resolve().parent
project_root = script_dir.parents[2]
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from ALGORITHMS.LSB.lsb_aleatoire.lsb_aleatoire import (
    lsb_aleatoire_decodeur,
    lsb_aleatoire_encodeur,
)


if __name__ == "__main__":

    #DATA

    header_len8 = 8
    header_len16 = 16
    header_len24 = 24
    header_len32 = 32

    canalBleu, canalVert, canalRouge = 0, 1, 2
    cle = 12345

    #IMAGE 1 RGB

    #Path de l'image 1
    image1_path = project_root / "DB_STEGANOGRAPHIE" / "RGB-BMP Steganalysis Dataset" / "CALTECH-BMP-1500" / "C0003.bmp"
    resultats_dir = script_dir / "resultats"
    resultats_dir.mkdir(parents=True, exist_ok=True)

    #On lit l'image 1
    image1 = cv2.imread(str(image1_path), cv2.IMREAD_UNCHANGED)

    if image1 is None:
        print("Erreur : Impossible de charger l'image1")

    #On sauvegarde l'image 1
    cv2.imwrite(str(resultats_dir / "image1_originale.bmp"), image1)

    #ENCODE

    #Path de l'image 1 originale
    image1_originale_path = resultats_dir / "image1_originale.bmp"

    #Message
    message1_original = ("Bonsoir comment allez vous, je vais tres bien")
    
    #On encode le message dans l'image
    image1_stego = lsb_aleatoire_encodeur(str(image1_originale_path), message1_original, header_len16, canalBleu, cle)

    #On sauvegarde l'image stego
    cv2.imwrite(str(resultats_dir / "image1_stego.bmp"), image1_stego)


    #DECODE

    #Path de l'image stego
    image1_stego_path = resultats_dir / "image1_stego.bmp"

    #On decode le message de l'image
    message1_stego = lsb_aleatoire_decodeur(str(image1_stego_path), header_len16, canalBleu, cle)
    
    if image1_stego is None:
        print("Erreur : Le decodage a echoue")

    #VERIFICATION

    print("IMAGE 1")
    print(f"Message encode : {message1_original}")
    print()
    print(f"Message decode : {message1_stego}")
    print()
