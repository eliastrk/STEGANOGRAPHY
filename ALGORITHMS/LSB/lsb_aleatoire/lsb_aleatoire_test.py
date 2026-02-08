from __future__ import annotations

import sys
from pathlib import Path

import cv2

script_dir = Path(__file__).resolve().parent
project_root = script_dir.parents[2]
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from ALGORITHMS.LSB.lsb_aleatoire.lsb_aleatoire import lsb_aleatoire_decodeur, lsb_aleatoire_encodeur
from ALGORITHMS.histogramme.histogramme import calculer_histogrammes_rgb, corr_histogrammes, save_histogram_rgb


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
    message1_original = ("Bonsoir comment allez vous, je vais tres bien zfeiejznfkjejjeeeeeeeeeennnnjeznfkjenfkzejfnzejfnkzjenfkjzenfjzenfkzjenfkzejnfkzejnfzkejfnennnezjfnekzjfnzkejfnkzejfnkzjfnejzkfnkzjenfkzejfnkzejfnkezjnfzjkenfekzjnfzkejfnzkejfnjefnzknfzekjnfzkejnekjfznfejzefjzekfjnzejkfnzekjfnzkejfnkzjefnkzejfnkzejfnkzejfnzkejfnkzejfnkezjnBonsoir comment allez vous, je vais tres bien zfeiejznfkjejjeeeeeeeeeennnnjeznfkjenfkzejfnzejfnkzjenfkjzenfjzenfkzjenfkzejnfkzejnfzkejfnennnezjfnekzjfnzkejfnkzejfnkzjfnejzkfnkzjenfkzejfnkzejfnkezjnfzjkenfekzjnfzkejfnzkejfnjefnzknfzekjnfzkejnekjfznfejzefjzekfjnzejkfnzekjfnzkejfnkzjefnkzejfnkzejfnkzejfnzkejfnkzejfnkezjnBonsoir comment allez vous, je vais tres bien zfeiejznfkjejjeeeeeeeeeennnnjeznfkjenfkzejfnzejfnkzjenfkjzenfjzenfkzjenfkzejnfkzejnfzkejfnennnezjfnekzjfnzkejfnkzejfnkzjfnejzkfnkzjenfkzejfnkzejfnkezjnfzjkenfekzjnfzkejfnzkejfnjefnzknfzekjnfzkejnekjfznfejzefjzekfjnzejkfnzekjfnzkejfnkzjefnkzejfnkzejfnkzejfnzkejfnkzejfnkezjnBonsoir comment allez vous, je vais tres bien zfeiejznfkjejjeeeeeeeeeennnnjeznfkjenfkzejfnzejfnkzjenfkjzenfjzenfkzjenfkzejnfkzejnfzkejfnennnezjfnekzjfnzkejfnkzejfnkzjfnejzkfnkzjenfkzejfnkzejfnkezjnfzjkenfekzjnfzkejfnzkejfnjefnzknfzekjnfzkejnekjfznfejzefjzekfjnzejkfnzekjfnzkejfnkzjefnkzejfnkzejfnkzejfnzkejfnkzejfnkezjnBonsoir comment allez vous, je vais tres bien zfeiejznfkjejjeeeeeeeeeennnnjeznfkjenfkzejfnzejfnkzjenfkjzenfjzenfkzjenfkzejnfkzejnfzkejfnennnezjfnekzjfnzkejfnkzejfnkzjfnejzkfnkzjenfkzejfnkzejfnkezjnfzjkenfekzjnfzkejfnzkejfnjefnzknfzekjnfzkejnekjfznfejzefjzekfjnzejkfnzekjfnzkejfnkzjefnkzejfnkzejfnkzejfnzkejfnkzejfnkezjnBonsoir comment allez vous, je vais tres bien zfeiejznfkjejjeeeeeeeeeennnnjeznfkjenfkzejfnzejfnkzjenfkjzenfjzenfkzjenfkzejnfkzejnfzkejfnennnezjfnekzjfnzkejfnkzejfnkzjfnejzkfnkzjenfkzejfnkzejfnkezjnfzjkenfekzjnfzkejfnzkejfnjefnzknfzekjnfzkejnekjfznfejzefjzekfjnzejkfnzekjfnzkejfnkzjefnkzejfnkzejfnkzejfnzkejfnkzejfnkezjnBonsoir comment allez vous, je vais tres bien zfeiejznfkjejjeeeeeeeeeennnnjeznfkjenfkzejfnzejfnkzjenfkjzenfjzenfkzjenfkzejnfkzejnfzkejfnennnezjfnekzjfnzkejfnkzejfnkzjfnejzkfnkzjenfkzejfnkzejfnkezjnfzjkenfekzjnfzkejfnzkejfnjefnzknfzekjnfzkejnekjfznfejzefjzekfjnzejkfnzekjfnzkejfnkzjefnkzejfnkzejfnkzejfnzkejfnkzejfnkezjnBonsoir comment allez vous, je vais tres bien zfeiejznfkjejjeeeeeeeeeennnnjeznfkjenfkzejfnzejfnkzjenfkjzenfjzenfkzjenfkzejnfkzejnfzkejfnennnezjfnekzjfnzkejfnkzejfnkzjfnejzkfnkzjenfkzejfnkzejfnkezjnfzjkenfekzjnfzkejfnzkejfnjefnzknfzekjnfzkejnekjfznfejzefjzekfjnzejkfnzekjfnzkejfnkzjefnkzejfnkzejfnkzejfnzkejfnkzejfnkezjnBonsoir comment allez vous, je vais tres bien zfeiejznfkjejjeeeeeeeeeennnnjeznfkjenfkzejfnzejfnkzjenfkjzenfjzenfkzjenfkzejnfkzejnfzkejfnennnezjfnekzjfnzkejfnkzejfnkzjfnejzkfnkzjenfkzejfnkzejfnkezjnfzjkenfekzjnfzkejfnzkejfnjefnzknfzekjnfzkejnekjfznfejzefjzekfjnzejkfnzekjfnzkejfnkzjefnkzejfnkzejfnkzejfnzkejfnkzejfnkezjnBonsoir comment allez vous, je vais tres bien zfeiejznfkjejjeeeeeeeeeennnnjeznfkjenfkzejfnzejfnkzjenfkjzenfjzenfkzjenfkzejnfkzejnfzkejfnennnezjfnekzjfnzkejfnkzejfnkzjfnejzkfnkzjenfkzejfnkzejfnkezjnfzjkenfekzjnfzkejfnzkejfnjefnzknfzekjnfzkejnekjfznfejzefjzekfjnzejkfnzekjfnzkejfnkzjefnkzejfnkzejfnkzejfnzkejfnkzejfnkezjnBonsoir comment allez vous, je vais tres bien zfeiejznfkjejjeeeeeeeeeennnnjeznfkjenfkzejfnzejfnkzjenfkjzenfjzenfkzjenfkzejnfkzejnfzkejfnennnezjfnekzjfnzkejfnkzejfnkzjfnejzkfnkzjenfkzejfnkzejfnkezjnfzjkenfekzjnfzkejfnzkejfnjefnzknfzekjnfzkejnekjfznfejzefjzekfjnzejkfnzekjfnzkejfnkzjefnkzejfnkzejfnkzejfnzkejfnkzejfnkezjnBonsoir comment allez vous, je vais tres bien zfeiejznfkjejjeeeeeeeeeennnnjeznfkjenfkzejfnzejfnkzjenfkjzenfjzenfkzjenfkzejnfkzejnfzkejfnennnezjfnekzjfnzkejfnkzejfnkzjfnejzkfnkzjenfkzejfnkzejfnkezjnfzjkenfekzjnfzkejfnzkejfnjefnzknfzekjnfzkejnekjfznfejzefjzekfjnzejkfnzekjfnzkejfnkzjefnkzejfnkzejfnkzejfnzkejfnkzejfnkezjn")
    
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

    #HISTOGRAMME IMAGE 1
    save_histogram_rgb(image1, resultats_dir / "histogramme_image1_originale.png", "Histogramme RGB - Image 1 Originale",)
    save_histogram_rgb(image1_stego, resultats_dir / "histogramme_image1_stego.png", "Histogramme RGB - Image 1 Stego",)

    h1_origine = calculer_histogrammes_rgb(image1)
    h1_stego = calculer_histogrammes_rgb(image1_stego)
    
    print("Correlation histogramme IMAGE 1 (meme image, doit etre 1.0):")
    for i, canal in enumerate(("B", "G", "R")):
        corr = corr_histogrammes([h1_origine[i]], [h1_origine[i]])[0]
        print(f"{canal}: {corr}")
        
    print()
        
    print("Correlation histogramme IMAGE 1 (original vs stego):")
    for i, canal in enumerate(("B", "G", "R")):
        corr = corr_histogrammes([h1_origine[i]], [h1_stego[i]])[0]
        print(f"{canal}: {corr}")
    
    print()
    print()
    
    
    #PSNR
    psnr = cv2.PSNR(image1, image1_stego)
    print("PSNR:", psnr, "dB")
    
    print()
    print()
    
    #SSIM
    ssim, ssim_map = cv2.quality.QualitySSIM_compute(image1, image1_stego)
    print("SSIM:", ssim[0])
