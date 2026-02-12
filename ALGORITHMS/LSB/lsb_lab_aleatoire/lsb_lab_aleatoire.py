from __future__ import annotations

from typing import Optional

import random

import cv2
import numpy as np

from ALGORITHMS.LSB.functions_lsb import choix_delta, modif_bit, build_binary_lsb


def lsb_lab_aleatoire_encodeur(image_path: str, message: str, header_len: int, cle_pixels: int, cle_canal: int) -> Optional[np.ndarray]:
    """
    Encode un message texte avec lsb dans un canal de l'image.
    La longueur du message (en bits) est d'abord écrite dans un en-tête de header_len bits,
    puis le contenu est inséré bit par bit dans des pixels (LAB) choisis aléatoirement selon une clé pour les pixels et les canaux.

    Args:
        image_path (str): path vers l'image
        message (str): message à cacher
        header_len (int): taille de l'entête en bits qui contiendra la taille du message
        cle_pixels (int): clé pour générer l'ordre aléatoire des pixels
        cle_canal (int): clé pour générer l'ordre aléatoire des canals

    Returns:
        np.ndarray: L'image modifiée avec le message caché dedans, None si erreur
    """

    #On charge l'_path sous la forme d'une matrice à 3 dimensions
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)

    #Si on arrive pas à charger l'image
    if img is None:
        print("Erreur : Impossible de charger l'image")
        return None
    
    #On charge LAB
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)

    #Si il y a pas assez de pixels pour cacher le message
    len_message = len(message) * 8
    total_len = len_message + header_len
    h, w = lab.shape[:2]
    total_pixels = h*w

    if total_pixels < total_len:
        print("Erreur : Pas assez de pixels pour cacher le message")
        return None

    #On met la taille du message en binaire
    len_message_binary = format(len_message, "0" + str(header_len) + "b")

    #Initialisations des variables pour le parcours des pixels
    index_pixel = 0
    index_message = 0
    index_bit = 0

    #Ordre aléatoire des pixels selon la clé
    liste_pixels = list(range(total_pixels))
    random.Random(cle_pixels).shuffle(liste_pixels)
    
    #Ordre aléatoire des canaux LAB selon la clé
    rCanal = random.Random(cle_canal)
    liste_canals = [rCanal.randint(1, 2) for _ in range(total_pixels)]

    #On regarde la valeur de chaque pixel dans le canal choisi en argument
    for pixel in liste_pixels:
        i = pixel // w
        j = pixel % w

        val_int = int(lab[i, j, liste_canals[index_pixel]])

        #Choix de delta
        delta = choix_delta(val_int)

        #Taille du message dans le header
        if index_pixel < header_len:
            val_int = modif_bit(val_int, len_message_binary[index_pixel], delta)

        #On écrit le message après le header
        else:
            binary = format(ord(message[index_message]), "08b")
            val_int = modif_bit(val_int, binary[index_bit], delta)

            index_bit += 1
            if index_bit == 8:
                index_bit = 0
                index_message += 1

        #print(lab[i, j, liste_canals[index_pixel]])
        lab[i, j, liste_canals[index_pixel]] = val_int

        index_pixel += 1

        #On sort complètement de la boucle quand on a parcourut le nombre de pixels necessaires
        if index_pixel >= total_len:
            rgb = cv2.cvtColor(lab, cv2.COLOR_Lab2BGR)
            return rgb

    return cv2.cvtColor(lab, cv2.COLOR_Lab2BGR)


def lsb_lab_aleatoire_decodeur(image_path: str, header_len: int, cle_pixels: int, cle_canal: int) -> Optional[str]:
    """
    Décode un message texte avec lsb dans un canal de l'image.
    La longueur du message (en bits) se situe dans un en-tête de header_len bits,
    puis on récupère le contenu bit par bit dans des pixels (LAB) choisis aléatoirement selon une clé pour les pixels et les canaux.

    Args:
        image_path (str): path vers l'image
        header_len (int): taille de l'entête en bits qui contiendra la taille du message
        cle_pixels (int): clé pour générer l'ordre aléatoire des pixels
        cle_canal (int): clé pour générer l'ordre aléatoire des canals

    Returns:
        str: Le message caché dans l'image avec lsb, None si erreur
    """

    #On charge l'_path sous la forme d'une matrice à 3 dimensions
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)

    #Si on arrive pas à charger l'image
    if img is None:
        print("Erreur : Impossible de charger l'image")
        return None
    
    #On charge LAB
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)

    #Initialisations des variables pour le parcours des pixels
    index_pixel = 0
    buffer = 0
    len_message = 0
    count_bit = 0
    message = ""

    h, w = lab.shape[:2]
    total_pixels = h * w

    #Ordre aléatoire des pixels selon la clé
    liste_pixels = list(range(total_pixels))
    random.Random(cle_pixels).shuffle(liste_pixels)

    #Ordre aléatoire des canaux LAB selon la clé
    rCanal = random.Random(cle_canal)
    liste_canals = [rCanal.randint(1, 2) for _ in range(total_pixels)]
        
    #On regarde la valeur de chaque pixel dans le canal choisi en argument
    for pixel in liste_pixels:
        i = pixel // w
        j = pixel % w

        val = lab[i, j, liste_canals[index_pixel]]

        #On récupère la taille du message dans le header
        if index_pixel < header_len:
            len_message = build_binary_lsb(len_message, int(val))

        #On récupère le message après avoir lu le header
        else:
            buffer = build_binary_lsb(buffer, int(val))

            count_bit += 1
            if count_bit == 8:
                message += chr(buffer)
                buffer = 0
                count_bit = 0

        index_pixel += 1

        #On sort complètement de la boucle quand on a parcourut le nombre de pixels necessaires
        if index_pixel >= len_message + header_len:
            return message

    return message
