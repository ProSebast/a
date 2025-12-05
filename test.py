import os
import csv

# Carpeta de datos
carpeta = os.path.join(os.path.dirname(__file__), "Datos_llamdo")
os.makedirs(carpeta, exist_ok=True)

archivo = os.path.join(carpeta, "llamados.csv")

# Crear archivo con encabezados si no existe
if not os.path.exists(archivo):
    with open(archivo, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["numero", "nombre", "hora", "profesional"])
        writer.writeheader()

# Datos de prueba
pacientes = [
    {"numero": "1", "nombre": "Juan Pérez", "hora": "10:00", "profesional": "Dr. López"},
    {"numero": "2", "nombre": "Ana Gómez", "hora": "10:15", "profesional": "Dra. Martínez"}
]

# Guardar pacientes
with open(archivo, "a", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["numero", "nombre", "hora", "profesional"])
    for p in pacientes:
        writer.writerow(p)

print("✅ Pacientes guardados correctamente en:", archivo)
