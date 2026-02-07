from __future__ import annotations

import random

MAX_PIXEL_VAL = 255
MIN_PIXEL_VAL = 0

def choix_delta(val: int) -> int:
    """
    Choisir aléatoirement si on va faire +1 ou -1 pour éviter la redondance,
    tout en restant dans l'intervalle [0,255]

    Args:
        val (int): valeur de l'octet

    Returns:
        int: +1 ou -1 aléatoirement ou selon la valeur de l'octet
    """
    
    delta = random.choice([-1, 1])
    
    if val == 0: 
        return 1
    elif val == 255: 
        return -1
    
    return delta

def modif_bit(val:int, bit:str, delta:int) -> int:
    """
    Modifit la valeur du bit selon sa parité, sa valeur et delta.

    Args:
        val (int): valeur de l'octet
        bit (str): le bit qu'on doit avoir
        delta (int): +1 ou -1 aléatoirement ou selon la valeur de l'octet
    Returns:
        int: la valeur après modification
    """
    
    if bit == "0" and (val % 2 != 0): 
        return val + delta
    elif bit == "1" and (val % 2 == 0): 
        return val + delta
    
    return val

def build_binary_lsb(acc_bit: int, val:int) -> int:
    """
    Construit une valeur binaire bit par bit à partir des bits récupérés avec lsb

    Args:
        acc_bit (int): accumulateur de bits
        val (int): valeur de l'octet

    Returns:
        int: renvoie l'accumulateur avec l'ajout du bit de poids faible de val
    """
    return (acc_bit << 1) | (val & 1)
