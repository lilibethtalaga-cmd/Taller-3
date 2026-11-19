# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 17:13:28 2026

@author: Lily
"""

from generador import generar_datos, ordenar_por_fc
from validador import validar_registro
from gestor_archivos import exportar_todo, importar_json, registrar_log
from base_datos import subir_a_mongo, ejecutar_consultas_y_exportar

def menu():
    datos_actuales = []
    datos_validados = []

    while True:
        print("\n--- SISTEMA DE MONITOREO BIOMÉDICO ---")
        print("1. Generar datos aleatorios (50 registros) y ordenar por FC")
        print("2. Ingresar un registro manual")
        print("3. Validar datos con Expresiones Regulares")
        print("4. Exportar datos a TXT, CSV y JSON")
        print("5. Importar datos desde JSON")
        print("6. Subir datos validados a MongoDB Atlas")
        print("7. Consultar en MongoDB (Promedio FC, SpO2 < 94% y buscar por ID)")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            raw = generar_datos(50)
            datos_actuales = ordenar_por_fc(raw)
            registrar_log("Generados y ordenados los 50 registros aleatorios.")
            print("Registros ordenados correctamente")

        elif opcion == "2":
            nuevo = {
                "id": input("ID (ej. ID-051): "),
                "fr": input("Edad (ej. 25 Años): "),
                "fc": input("Frecuencia cardiaca (ej. 085ppm): "),
                "spo2": input("SpO2 (ej. 98%): ")
            }
            datos_actuales.append(nuevo)
            datos_actuales = ordenar_por_fc(datos_actuales)
            registrar_log(f"Registro manual agregado: {nuevo['id']}")

        elif opcion == "3":
            datos_validados = [d for d in datos_actuales if validar_registro(d)]
            invalidos = len(datos_actuales) - len(datos_validados)
            registrar_log(f"Validación ejecutada: {len(datos_validados)} válidos, {invalidos} inválidos.")
            print(f"Válidos: {len(datos_validados)} | Rechazados por formato: {invalidos}")

        elif opcion == "4":
            if not datos_actuales:
                print("Primero genera o importa datos.")
            else:
                exportar_todo(datos_actuales)

        elif opcion == "5":
            datos_actuales = importar_json()
            print(f"Se cargaron {len(datos_actuales)} registros desde el JSON.")

        elif opcion == "6":
            if not datos_validados:
                print("Primero debes validar los datos (Opción 3).")
            else:
                subir_a_mongo(datos_validados)

        elif opcion == "7":
            id_buscar = input("Ingrese el ID del paciente a consultar (ej. ID-010): ")
            ejecutar_consultas_y_exportar(id_buscar)

        elif opcion == "8":
            registrar_log("Programa finalizado por el usuario.")
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()

        
        