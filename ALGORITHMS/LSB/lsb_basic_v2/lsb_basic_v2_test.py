from __future__ import annotations

import sys
from pathlib import Path

import cv2
script_dir = Path(__file__).resolve().parent
project_root = script_dir.parents[2]
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from ALGORITHMS.LSB.lsb_basic_v2.lsb_basic_v2 import lsb_basic_encodeur_v2, lsb_basic_decodeur_v2
from ALGORITHMS.histogramme.histogramme import calculer_histogramme_grayscale, calculer_histogrammes_rgb, corr_histogrammes, save_histogram_grayscale, save_histogram_rgb


if __name__ == "__main__":
    
    #DATA
    
    header_len8 = 8
    header_len16 = 16
    header_len24 = 24
    header_len32 = 32
    
    canalBleu, canalVert, canalRouge = 0, 1, 2
    

    #IMAGE 1 RGB
    
    #Path de l'image 1
    image1_path = project_root / "DB_STEGANOGRAPHIE" / "RGB-BMP Steganalysis Dataset" / "CALTECH-BMP-1500" / "C0002.bmp"
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
    image1_stego = lsb_basic_encodeur_v2(str(image1_originale_path), message1_original, header_len16, canalBleu)
    
    #On sauvegarde l'image stego
    cv2.imwrite(str(resultats_dir / "image1_stego.bmp"), image1_stego)
    
    
    #DECODE
    
    #Path de l'image stego
    image1_stego_path = resultats_dir / "image1_stego.bmp"
    
    #On decode le message de l'image
    message1_stego = lsb_basic_decodeur_v2(str(image1_stego_path), header_len16, canalBleu)
    
    if image1_stego is None:
        print("Erreur : Le décodage a échoué")
    
    
    #VERIFICATION
    
    print("IMAGE 1")
    print(f"Message encodé : {message1_original}")
    print()
    print(f"Message décodé : {message1_stego}")
    print()

    #HISTOGRAMME IMAGE 1
    save_histogram_rgb(image1, resultats_dir / "histogramme_image1_originale.png", "Histogramme RGB - Image 1 Originale")
    save_histogram_rgb(image1_stego, resultats_dir / "histogramme_image1_stego.png", "Histogramme RGB - Image 1 Stego")

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
    
    print()
    print()
    
    
    
    #IMAGE 2 Grayscale
    
    #Path de l'image 2
    image2_path = project_root / "DB_STEGANOGRAPHIE" / "BOSSbase_1.01" / "1.pgm"
    resultats_dir = script_dir / "resultats"
    resultats_dir.mkdir(parents=True, exist_ok=True)
    
    #On lit l'image 2
    image2 = cv2.imread(str(image2_path), cv2.IMREAD_UNCHANGED)
    
    if image2 is None:
        print("Erreur : Impossible de charger l'image2")
    
    #On sauvegarde l'image 2
    cv2.imwrite(str(resultats_dir / "image2_originale.bmp"), image2)
    
    
    #ENCODE 
    
    #Path de l'image 2 originale
    image2_originale_path = resultats_dir / "image2_originale.bmp"
    
    #Message
    message2_original = ("Bonsoir comment allez vous, je vais tres bien zfeiejznfkjejjeeeeeeeeeennnnjeznfkjenfkzejfnzejfnkzjenfkjzenfjzenfkzjenfkzejnfkzejnfzkejfnennnezjfnekzjfnzkejfnkzejfnkzjfnejzkfnkzjenfkzejfnkzejfnkezjnfzjkenfekzjnfzkejfnzkejfnjefnzknfzekjnfzkejnekjfznfejzefjzekfjnzejkfnzekjfnzkejfnkzjefnkzejfnkzejfnkzejfnzkejfnkzejfnkezjnBonsoir comment allez vous, je vais tres bien zfeiejznfkjejjeeeeeeeeeennnnjeznfkjenfkzejfnzejfnkzjenfkjzenfjzenfkzjenfkzejnfkzejnfzkejfnennnezjfnekzjfnzkejfnkzejfnkzjfnejzkfnkzjenfkzejfnkzejfnkezjnfzjkenfekzjnfzkejfnzkejfnjefnzknfzekjnfzkejnekjfznfejzefjzekfjnzejkfnzekjfnzkejfnkzjefnkzejfnkzejfnkzejfnzkejfnkzejfnkezjnBonsoir comment allez vous, je vais tres bien zfeiejznfkjejjeeeeeeeeeennnnjeznfkjenfkzejfnzejfnkzjenfkjzenfjzenfkzjenfkzejnfkzejnfzkejfnennnezjfnekzjfnzkejfnkzejfnkzjfnejzkfnkzjenfkzejfnkzejfnkezjnfzjkenfekzjnfzkejfnzkejfnjefnzknfzekjnfzkejnekjfznfejzefjzekfjnzejkfnzekjfnzkejfnkzjefnkzejfnkzejfnkzejfnzkejfnkzejfnkezjnBonsoir comment allez vous, je vais tres bien zfeiejznfkjejjeeeeeeeeeennnnjeznfkjenfkzejfnzejfnkzjenfkjzenfjzenfkzjenfkzejnfkzejnfzkejfnennnezjfnekzjfnzkejfnkzejfnkzjfnejzkfnkzjenfkzejfnkzejfnkezjnfzjkenfekzjnfzkejfnzkejfnjefnzknfzekjnfzkejnekjfznfejzefjzekfjnzejkfnzekjfnzkejfnkzjefnkzejfnkzejfnkzejfnzkejfnkzejfnkezjnBonsoir comment allez vous, je vais tres bien zfeiejznfkjejjeeeeeeeeeennnnjeznfkjenfkzejfnzejfnkzjenfkjzenfjzenfkzjenfkzejnfkzejnfzkejfnennnezjfnekzjfnzkejfnkzejfnkzjfnejzkfnkzjenfkzejfnkzejfnkezjnfzjkenfekzjnfzkejfnzkejfnjefnzknfzekjnfzkejnekjfznfejzefjzekfjnzejkfnzekjfnzkejfnkzjefnkzejfnkzejfnkzejfnzkejfnkzejfnkezjnBonsoir comment allez vous, je vais tres bien zfeiejznfkjejjeeeeeeeeeennnnjeznfkjenfkzejfnzejfnkzjenfkjzenfjzenfkzjenfkzejnfkzejnfzkejfnennnezjfnekzjfnzkejfnkzejfnkzjfnejzkfnkzjenfkzejfnkzejfnkezjnfzjkenfekzjnfzkejfnzkejfnjefnzknfzekjnfzkejnekjfznfejzefjzekfjnzejkfnzekjfnzkejfnkzjefnkzejfnkzejfnkzejfnzkejfnkzejfnkezjnBonsoir comment allez vous, je vais tres bien zfeiejznfkjejjeeeeeeeeeennnnjeznfkjenfkzejfnzejfnkzjenfkjzenfjzenfkzjenfkzejnfkzejnfzkejfnennnezjfnekzjfnzkejfnkzejfnkzjfnejzkfnkzjenfkzejfnkzejfnkezjnfzjkenfekzjnfzkejfnzkejfnjefnzknfzekjnfzkejnekjfznfejzefjzekfjnzejkfnzekjfnzkejfnkzjefnkzejfnkzejfnkzejfnzkejfnkzejfnkezjnBonsoir comment allez vous, je vais tres bien zfeiejznfkjejjeeeeeeeeeennnnjeznfkjenfkzejfnzejfnkzjenfkjzenfjzenfkzjenfkzejnfkzejnfzkejfnennnezjfnekzjfnzkejfnkzejfnkzjfnejzkfnkzjenfkzejfnkzejfnkezjnfzjkenfekzjnfzkejfnzkejfnjefnzknfzekjnfzkejnekjfznfejzefjzekfjnzejkfnzekjfnzkejfnkzjefnkzejfnkzejfnkzejfnzkejfnkzejfnkezjnBonsoir comment allez vous, je vais tres bien zfeiejznfkjejjeeeeeeeeeennnnjeznfkjenfkzejfnzejfnkzjenfkjzenfjzenfkzjenfkzejnfkzejnfzkejfnennnezjfnekzjfnzkejfnkzejfnkzjfnejzkfnkzjenfkzejfnkzejfnkezjnfzjkenfekzjnfzkejfnzkejfnjefnzknfzekjnfzkejnekjfznfejzefjzekfjnzejkfnzekjfnzkejfnkzjefnkzejfnkzejfnkzejfnzkejfnkzejfnkezjnBonsoir comment allez vous, je vais tres bien zfeiejznfkjejjeeeeeeeeeennnnjeznfkjenfkzejfnzejfnkzjenfkjzenfjzenfkzjenfkzejnfkzejnfzkejfnennnezjfnekzjfnzkejfnkzejfnkzjfnejzkfnkzjenfkzejfnkzejfnkezjnfzjkenfekzjnfzkejfnzkejfnjefnzknfzekjnfzkejnekjfznfejzefjzekfjnzejkfnzekjfnzkejfnkzjefnkzejfnkzejfnkzejfnzkejfnkzejfnkezjnBonsoir comment allez vous, je vais tres bien zfeiejznfkjejjeeeeeeeeeennnnjeznfkjenfkzejfnzejfnkzjenfkjzenfjzenfkzjenfkzejnfkzejnfzkejfnennnezjfnekzjfnzkejfnkzejfnkzjfnejzkfnkzjenfkzejfnkzejfnkezjnfzjkenfekzjnfzkejfnzkejfnjefnzknfzekjnfzkejnekjfznfejzefjzekfjnzejkfnzekjfnzkejfnkzjefnkzejfnkzejfnkzejfnzkejfnkzejfnkezjnBonsoir comment allez vous, je vais tres bien zfeiejznfkjejjeeeeeeeeeennnnjeznfkjenfkzejfnzejfnkzjenfkjzenfjzenfkzjenfkzejnfkzejnfzkejfnennnezjfnekzjfnzkejfnkzejfnkzjfnejzkfnkzjenfkzejfnkzejfnkezjnfzjkenfekzjnfzkejfnzkejfnjefnzknfzekjnfzkejnekjfznfejzefjzekfjnzejkfnzekjfnzkejfnkzjefnkzejfnkzejfnkzejfnzkejfnkzejfnkezjn")
    
    #On encode le message dans l'image
    image2_stego = lsb_basic_encodeur_v2(str(image2_originale_path), message2_original, header_len24, canalBleu)
    
    #On sauvegarde l'image stego
    cv2.imwrite(str(resultats_dir / "image2_stego.bmp"), image2_stego)
    
    
    #DECODE
    
    #Path de l'image stego
    image2_stego_path = resultats_dir / "image2_stego.bmp"
    
    #On decode le message de l'image
    message2_stego = lsb_basic_decodeur_v2(str(image2_stego_path), header_len24, canalBleu)
    if image2_stego is None:
        print("Erreur : Le décodage a échoué")
    
    
    #VERIFICATION
    
    print("IMAGE 2")
    print(f"Message encodé : {message2_original}")
    print()
    print(f"Message décodé : {message2_stego}")
    print()

    #HISTOGRAMME IMAGE 2
    save_histogram_grayscale(image2, resultats_dir / "histogramme_image2_originale.png", "Histogramme Grayscale - Image 2 Originale")
    save_histogram_grayscale(image2_stego, resultats_dir / "histogramme_image2_stego.png", "Histogramme Grayscale - Image 2 Stego")

    h2_origine = calculer_histogramme_grayscale(image2)
    h2_stego = calculer_histogramme_grayscale(image2_stego)
    
    print("Correlation histogramme IMAGE 2 (meme image, doit etre 1.0):")
    corr_same = corr_histogrammes([h2_origine], [h2_origine])[0]
    print(f"Grayscale: {corr_same}")
    
    print()
    
    print("Correlation histogramme IMAGE 2 (original vs stego):")
    corr_diff = corr_histogrammes([h2_origine], [h2_stego])[0]
    print(f"Grayscale: {corr_diff}")
    
    print()
    print()
    
    #PSNR
    psnr = cv2.PSNR(image2, image2_stego)
    print("PSNR:", psnr, "dB")
    
    print()
    print()
    
    #SSIM
    ssim, ssim_map = cv2.quality.QualitySSIM_compute(image2, image2_stego)
    print("SSIM:", ssim[0])
    
    
    
