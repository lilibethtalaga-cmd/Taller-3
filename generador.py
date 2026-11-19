# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 12:58:01 2026

@author: Lily
"""

#id (Identificacion), de la forma ”ID-001”. ´
#fr (Edad), de la forma ”18 Anos”.
#fc (Frecuencia cardiaca), de la forma ”090ppm”.
#spo2 (Saturacion periférica de oxígeno), de la forma ”95%”
#ordenar los datos por frecuencia cardiaca.


import random

def generar_datos(cantidad=50):
    registros = []
    for i in range(1, cantidad + 1):
        id_str = f"ID-{str(i).zfill(3)}"
        fr_str = f"{random.randint(18, 90)} Años"
        fc_str = f"{str(random.randint(50, 140)).zfill(3)}ppm"
        spo2_str = f"{random.randint(88, 100)}%"

        registros.append({
            "id": id_str,
            "fr": fr_str,
            "fc": fc_str,
            "spo2": spo2_str
        })
    return registros

def ordenar_por_fc(registros):
    return sorted(registros, key=lambda x: int(x["fc"].replace("ppm", "")))