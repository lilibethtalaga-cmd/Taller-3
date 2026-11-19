# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 12:58:58 2026

@author: Lily
"""

from pymongo import MongoClient
import json
from gestor_archivos import registrar_log

user="lilibethtalaga_db_user"
passwd="Vxu96HLOEMFguM9X"

URI_MONGO = f"mongodb+srv://lilibethtalaga_db_user:{passwd}@hxrtvy.zdlvgj3.mongodb.net/"

def conectar_db():
    cliente = MongoClient(URI_MONGO)
    db = cliente["bioing_db"]
    return db["signos_vitales"]

def subir_a_mongo(registros_validos):
    try:
        coleccion = conectar_db()
        if registros_validos:
            coleccion.insert_many(registros_validos)
            registrar_log(f"Se insertaron {len(registros_validos)} registros en MongoDB.")
            print("Datos subidos a MongoDB Atlas.")
    except Exception as e:
        registrar_log(f"ERROR MongoDB al insertar: {e}")
        print(f"Error de conexión: {e}")

def ejecutar_consultas_y_exportar(id_buscar):
    try:
        coleccion = conectar_db()
        todos = list(coleccion.find({}, {"_id": 0}))

        frecuencias = [int(doc["fc"].replace("ppm", "")) for doc in todos]
        promedio_fc = sum(frecuencias) / len(frecuencias) if frecuencias else 0

        bajo_spo2 = [doc for doc in todos if int(doc["spo2"].replace("%", "")) < 94]

        paciente_id = coleccion.find_one({"id": id_buscar}, {"_id": 0})

        resultados = {
            "promedio_frecuencia_cardiaca": round(promedio_fc, 2),
            "pacientes_spo2_menor_94": bajo_spo2,
            "busqueda_por_id": paciente_id
        }

        with open("data/json/resultados_mongo.json", "w", encoding="utf-8") as f:
            json.dump(resultados, f, indent=4, ensure_ascii=False)

        registrar_log("Consultas de MongoDB ejecutadas y exportadas a resultados_mongo.json.")
        print("Resultados guardados en data/json/resultados_mongo.json")
    except Exception as e:
        registrar_log(f"ERROR en consultas MongoDB: {e}")
        print(f"Error: {e}")
