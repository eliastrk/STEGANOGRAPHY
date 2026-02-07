from __future__ import annotations

from typing import Optional

import cv2
import numpy as np

import random


def lsb_basic_encodeur(image_path: str, message: str, header_len: int, canal: int) -> Optional[np.ndarray]:
    """
    Encode un message texte avec lsb dans un canal de l'image.
    La longueur du message (en bits) est d'abord écrite dans un en-tête de header_len bits, 
    puis le contenu est inséré bit par bit dans les pixels suivants.

    Args:
        image_path (str): path vers l'image
        message (str): message à cacher
        header_len (int): taille de l'entête en bits qui contiendra la taille du message
        canal (int): dans quel canal on va appliquer lsb (0=Bleu, 1=Vert, 2=Rouge)

    Returns:
        np.ndarray: L'image modifiée avec le message caché dedans, None si erreur
    """
    #On charge l'_path sous la forme d'une matrice à 3 dimensions 
    img = cv2.imread(image_path)
    
    #Si on arrive pas à charger l'image
    if img is None:
        print("Erreur : Impossible de charger l'image")
        return
    
    #Si il y a pas assez de pixels pour cacher le message
    len_message = len(message)*8
    h, w = img.shape[:2]
    
    if h*w < len_message + header_len:
        print("Erreur : Pas assez de pixels pour cacher le message")
        return
    
    #On met la taille du message en binaire
    len_message_binary = format(len_message, '0' + str(header_len) + 'b')
    
    #Initialisations des variables pour le parcours des pixels
    index = 0
    l = 0
    m = 0
    stop = False
    
    #On regarde la valeur de chaque pixel dans le canal choisi en argument
    for i in img:
        for j in i:
            
            #Choisir si +1 ou -1
            delta = random.choice([-1, 1])
            
            if j[canal] == 0: delta = 1
            elif j[canal] == 255: delta = -1
            
            #Taille du message dans le header
            if index < header_len:
                
                if len_message_binary[index] == '0':
                    if j[canal]%2 != 0:
                        j[canal] = int(j[canal]) + delta      
                else:
                    if j[canal]%2 == 0:
                        j[canal] = int(j[canal]) + delta 
                          
            #On écrit le message après le header
            else:     
                binary = format(ord(message[l]), '08b')
                
                if binary[m] == '0':
                    if j[canal]%2 != 0:
                        j[canal] = int(j[canal]) + delta      
                else:
                    if j[canal]%2 == 0:
                        j[canal] = int(j[canal]) + delta 
                
                m += 1
                
                if m == 8:
                    m = 0
                    l+=1
            
            index += 1
            
            #On sort complètement de la boucle quand on a parcourut le nombre de pixels necessaires
            if index >= len_message + header_len :
                stop = True
                break
        
        if stop : break
        

    return img


def lsb_basic_decodeur(image_path: str, header_len: int, canal: int) -> Optional[str]:
    """
    Décode un message texte avec lsb dans un canal de l'image.
    La longueur du message (en bits) se situe dans un en-tête de header_len bits, 
    puis on récupère le contenu bit par bit dans les pixels suivants afin d'obtenir le message caché.

    Args:
        image_path (str): path vers l'image
        header_len (int): taille de l'entête en bits qui contiendra la taille du message
        canal (int): dans quel canal on va decoder lsb (0=Bleu, 1=Vert, 2=Rouge)

    Returns:
        str: Le message caché dans l'image avec lsb, None si erreur
    """
    #On charge l'image sous la forme d'une matrice à 3 dimensions 
    img = cv2.imread(image_path)
    
    #Si on arrive pas à charger l'image
    if img is None:
        print("Erreur : Impossible de charger l'image")
        return
    
    #Initialisations des variables pour le parcours des pixels
    index = 0
    buffer = 0
    len_message = 0
    count = 0
    stop = False
    message = ""
    
    #On regarde la valeur de chaque pixel dans le canal choisi en argument
    for i in img:
        for j in i:
            
            #On récupère la taille du message dans le header
            if index < header_len:
                if j[canal]%2 == 0: len_message = (len_message << 1) | 0
                else : len_message = (len_message << 1) | 1
            
            #On récupère le message après avoir lu le header
            else:
                if j[canal]%2 == 0: buffer = (buffer << 1) | 0
                else : buffer = (buffer << 1) | 1

                count += 1
                
                if count == 8:
                    message += chr(buffer)
                    buffer = 0
                    count = 0
            
            index += 1
            
            #On sort complètement de la boucle quand on a parcourut le nombre de pixels necessaires
            if index >= len_message + header_len :
                stop = True
                break
            
        
        if stop : break
    
    return message