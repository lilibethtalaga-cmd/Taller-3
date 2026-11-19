# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 12:58:40 2026

@author: Lily
"""
from pathlib import Path
from datetime import datetime
import json
import csv

def inicializar_carpetas():
    for subcarpeta in ["txt", "csv", "json"]:
        Path(f"data/{subcarpeta}").mkdir(parents=True, exist_ok=True)
    registrar_log("Estructura de carpetas verificada/creada.")

def registrar_log(mensaje):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"[{fecha}] {mensaje}\n")

def exportar_todo(registros):
    try:
        inicializar_carpetas()

        with open("data/txt/datos.txt", "w", encoding="utf-8") as f:
            for r in registros:
                f.write(f"{r['id']} | {r['fr']} | {r['fc']} | {r['spo2']}\n")

        with open("data/csv/datos.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "fr", "fc", "spo2"])
            writer.writeheader()
            writer.writerows(registros)

        with open("data/json/datos.json", "w", encoding="utf-8") as f:
            json.dump(registros, f, indent=4, ensure_ascii=False)

        registrar_log(f"Se exportaron {len(registros)} registros a TXT, CSV y JSON.")
        print("Archivos guardados correctamente.")
    except Exception as e:
        registrar_log(f"ERROR al exportar archivos: {e}")
        print(f"Ocurrió un error: {e}")

def importar_json():
    ruta = Path("data/json/datos.json")
    try:
        if not ruta.exists():
            print("El archivo JSON aún no existe.")
            return []
        with open(ruta, "r", encoding="utf-8") as f:
            datos = json.load(f)
        registrar_log("Datos importados desde datos.json.")
        return datos
    except Exception as e:
        registrar_log(f"ERROR al importar JSON: {e}")
        return []