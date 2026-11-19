# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 12:58:18 2026

@author: Lily
"""

import re

def validar_registro(registro):
    patron_id = r"^ID-\d{3}$"          # Ej: ID-001
    patron_fr = r"^\d{1,3} Años$"     # Ej: 18 Años
    patron_fc = r"^\d{3}ppm$"         # Ej: 090ppm
    patron_spo2 = r"^\d{2,3}%$"       # Ej: 95%

    if not re.match(patron_id, registro.get("id", "")):
        return False
    if not re.match(patron_fr, registro.get("fr", "")):
        return False
    if not re.match(patron_fc, registro.get("fc", "")):
        return False
    if not re.match(patron_spo2, registro.get("spo2", "")):
        return False
    
    return True