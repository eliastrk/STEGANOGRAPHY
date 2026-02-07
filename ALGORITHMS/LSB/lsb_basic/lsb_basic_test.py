from __future__ import annotations

import cv2
from pathlib import Path

from lsb_basic import lsb_basic_encodeur, lsb_basic_decodeur


if __name__ == "__main__":
    
    #DATA
    
    header_len8 = 8
    header_len16 = 16
    header_len24 = 24
    header_len32 = 32
    
    canalBleu, canalVert, canalRouge = 0, 1, 2
    
    
    
    #IMAGE 1
    
    #Path de l'image 1
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parents[2]
    image1_path = project_root / "DB_STEGANOGRAPHIE" / "RGB-BMP Steganalysis Dataset" / "CALTECH-BMP-1500" / "C0002.bmp"
    resultats_dir = script_dir / "resultats"
    resultats_dir.mkdir(parents=True, exist_ok=True)
    
    #On lit l'image 1
    image1 = cv2.imread(str(image1_path))
    
    if image1 is None:
        print("Erreur : Impossible de charger l'image1")
    
    #On sauvegarde l'image 1
    cv2.imwrite(str(resultats_dir / "image1_originale.bmp"), image1)
    
    
    #ENCODE 
    
    #Path de l'image 1 originale
    image1_originale_path = resultats_dir / "image1_originale.bmp"
    
    #Message
    message1_original = "Le vent glissait entre les immeubles comme une rumeur ancienne, une lumière pâle clignotait en hésitant entre la nuit et l aube, des pas résonnaient au loin sans que personne ne semble arriver, et quelque part une idée naissait, discrète mais impossible à ignorer."
    
    #On encode le message dans l'image
    image1_stego = lsb_basic_encodeur(str(image1_originale_path), message1_original, header_len16, canalBleu)
    
    #On sauvegarde l'image stego
    cv2.imwrite(str(resultats_dir / "image1_stego.bmp"), image1_stego)
    
    
    #DECODE
    
    #Path de l'image stego
    image1_stego_path = resultats_dir / "image1_stego.bmp"
    
    #On decode le message de l'image
    message1_stego = lsb_basic_decodeur(str(image1_stego_path), header_len16, canalBleu)
    if image1_stego is None:
        print("Erreur : Le décodage a échoué")
    
    
    #VERIFICATION
    
    print("IMAGE 1")
    print(f"Message encodé : {message1_original}")
    print(f"Message décodé : {message1_stego}")
