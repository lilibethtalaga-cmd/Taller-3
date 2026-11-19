# Sistema de Gestión y Monitoreo de Datos Biomédicos

Taller desarrollado en Python para la generación, validación mediante expresiones regulares, almacenamiento en formatos txt, csv y json e integración con bases de datos NoSQL en la nube (MongoDB Atlas) con el fin de almacenar registros biomédicos.

## Estructura del Proyecto

* `main.py`: Menú interactivo que integra todos los módulos del sistema.
* `generador.py`: Generación aleatoria de registros biomédicos (ID, frecuencia respiratoria, frecuencia cardíaca y saturación de oxígeno) y ordenamiento por frecuencia cardíaca.
* `validador.py`: Validación de los formatos de signos vitales utilizando expresiones regulares.
* `gestor_archivos.py`: Creación automática de directorios, exportación e importación en formatos `.txt`, `.csv` y `.json`, y registro en `log.txt`.
* `base_datos.py`: Conexión a MongoDB Atlas, carga de registros validados y ejecución de consultas (promedio de FC, filtrado de pacientes con $SpO_2 < 94\%$ y búsqueda por ID).

## Requisitos e Instalación

1. Clonar el repositorio:
   `git clone https://github.com/lilibethtalaga-cmd/Taller-3.git`
2. Crear y activar el entorno virtual:
   `py -m venv env`
   `env\Scripts\activate`
3. Instalar MongoDB:
   `pip install pymongo`

## Ejecución

1. Configurar la cadena de conexión (`URI_MONGO`) con las credenciales en `base_datos.py`.
2. Ejecutar el programa principal:
   `python main.py`

## Autora

* **Lilibeth Tálaga**