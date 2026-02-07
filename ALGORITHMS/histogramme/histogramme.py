from __future__ import annotations

from pathlib import Path

import cv2
from matplotlib import pyplot as plt


def save_histogram_rgb(image, output_path: Path, title: str) -> None:
    colors = ("b", "g", "r")
    
    plt.figure(figsize=(10, 5))
    
    for i, col in enumerate(colors):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
        
    plt.title(title)
    plt.xlabel("Intensite (0-255)")
    plt.ylabel("Nombre de pixels")
    plt.tight_layout()
    plt.savefig(str(output_path))
    plt.close()


def save_histogram_grayscale(image, output_path: Path, title: str) -> None:
    plt.figure(figsize=(10, 5))
    
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    
    plt.plot(hist, color="black")
    plt.title(title)
    plt.xlabel("Intensite (0-255)")
    plt.ylabel("Nombre de pixels")
    plt.tight_layout()
    plt.savefig(str(output_path))
    plt.close()


def calculer_histogrammes_rgb(image):
    hists = []
    
    for i in range(3):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        hist = cv2.normalize(hist, hist).flatten()
        hists.append(hist)
        
    return hists


def calculer_histogramme_grayscale(image):
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    return cv2.normalize(hist, hist).flatten()


def corr_histogrammes(hists_a, hists_b):
    corrs = []
    
    for ha, hb in zip(hists_a, hists_b):
        corrs.append(cv2.compareHist(ha, hb, cv2.HISTCMP_CORREL))
        
    return corrs
