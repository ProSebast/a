# services/data_service.py
import csv
from models.registro import RegistroPaciente

class DataService:
    def __init__(self, ruta_csv="registros.csv"):
        self.ruta_csv = ruta_csv
        self.registros = []  # lista en memoria

    def agregar_registro(self, registro: RegistroPaciente):
        self.registros.append(registro)
        self._guardar_csv(registro)

    def _guardar_csv(self, registro: RegistroPaciente):
        # Guardar en CSV agregando al final
        with open(self.ruta_csv, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([registro.numero, registro.nombre, registro.hora, registro.profesional])
