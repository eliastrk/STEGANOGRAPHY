from __future__ import annotations

from pathlib import Path

import cv2
from matplotlib import pyplot as plt


def save_histogram(image_path: Path, output_path: Path, title: str) -> None:
    img = cv2.imread(str(image_path))
    if img is None:
        print(f"Erreur : Impossible de charger l'image: {image_path}")
        return

    colors = ("b", "g", "r")
    plt.figure(figsize=(10, 5))
    for i, col in enumerate(colors):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)

    plt.title(title)
    plt.xlabel("Intensité (0-255)")
    plt.ylabel("Nombre de pixels")
    plt.tight_layout()
    plt.savefig(str(output_path))
    plt.close()


def calculer_histogrammes_rgb(image_path: Path):
    img = cv2.imread(str(image_path))
    if img is None:
        print("Erreur : Impossible de charger l'image")
        return None

    hists = []
    for i in range(3):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        hist = cv2.normalize(hist, hist).flatten()
        hists.append(hist)
    return hists


if __name__ == "__main__":
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parents[1]

    dataset_dir = project_root / "DB_STEGANOGRAPHIE" / "RGB-BMP Steganalysis Dataset"
    original_path = dataset_dir / "originals" / "845153.JPG"
    stego_path = dataset_dir / "stegos" / "845162.JPG"

    resultats_dir = script_dir / "resultats"
    resultats_dir.mkdir(parents=True, exist_ok=True)

    save_histogram(
        original_path,
        resultats_dir / "histogramme_845153_original.png",
        "Histogramme RGB - Original 845153.JPG",
    )
    save_histogram(
        stego_path,
        resultats_dir / "histogramme_845162_stego.png",
        "Histogramme RGB - Stego 845162.JPG",
    )

    h_orig = calculer_histogrammes_rgb(original_path)
    h_stego = calculer_histogrammes_rgb(stego_path)

    if h_orig is not None and h_stego is not None:
        print("Correlation (meme image, doit etre 1.0):")
        for i, canal in enumerate(("B", "G", "R")):
            corr = cv2.compareHist(h_orig[i], h_orig[i], cv2.HISTCMP_CORREL)
            print(f"{canal}: {corr}")

        print("Correlation (original vs stego):")
        for i, canal in enumerate(("B", "G", "R")):
            corr = cv2.compareHist(h_orig[i], h_stego[i], cv2.HISTCMP_CORREL)
            print(f"{canal}: {corr}")
