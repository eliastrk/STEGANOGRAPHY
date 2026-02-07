from __future__ import annotations

import sys
from pathlib import Path

import cv2

script_dir = Path(__file__).resolve().parent
project_root = script_dir.parents[1]
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from ALGORITHMS.histogramme.histogramme import calculer_histogrammes_rgb, corr_histogrammes, save_histogram_rgb


if __name__ == "__main__":
    dataset_dir = project_root / "DB_STEGANOGRAPHIE" / "RGB-BMP Steganalysis Dataset"
    original_path = dataset_dir / "originals" / "845153.JPG"
    stego_path = dataset_dir / "stegos" / "845162.JPG"

    resultats_dir = script_dir / "resultats"
    resultats_dir.mkdir(parents=True, exist_ok=True)

    original = cv2.imread(str(original_path))
    stego = cv2.imread(str(stego_path))
    
    if original is None or stego is None:
        print("Erreur : Impossible de charger les images")
    
    save_histogram_rgb(original, resultats_dir / "histogramme_845153_original.png", "Histogramme RGB - Original 845153.JPG")
    save_histogram_rgb(stego, resultats_dir / "histogramme_845162_stego.png","Histogramme RGB - Stego 845162.JPG") 

    h_origine = calculer_histogrammes_rgb(original)
    h_stego = calculer_histogrammes_rgb(stego)

    print("Correlation (meme image, doit etre 1.0):")
    corrs_same = corr_histogrammes(h_origine, h_origine)
    for canal, corr in zip(("B", "G", "R"), corrs_same):
        print(f"{canal}: {corr}")

    print()
    
    print("Correlation (original vs stego):")
    corrs = corr_histogrammes(h_origine, h_stego)
    for canal, corr in zip(("B", "G", "R"), corrs):
        print(f"{canal}: {corr}")
