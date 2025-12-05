import os
import csv

class ControladorLlamado:
    def __init__(self):
        # Carpeta dentro de app
        self.carpeta = os.path.join(os.path.dirname(__file__), "..", "Datos_llamdo")
        os.makedirs(self.carpeta, exist_ok=True)

        # Archivo CSV
        self.archivo = os.path.join(self.carpeta, "llamados.csv")

        # Si no existe, crear con encabezados
        if not os.path.exists(self.archivo):
            with open(self.archivo, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["numero", "nombre", "hora", "profesional"])
                writer.writeheader()

    def guardar_paciente(self, paciente):
        # 🔥 Guardar paciente al CSV
        with open(self.archivo, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["numero", "nombre", "hora", "profesional"])
            writer.writerow(paciente)
