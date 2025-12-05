import csv
from pathlib import Path


class CSVService:
    """Servicio para gestionar archivos CSV"""
    
    def __init__(self, ruta_csv):
        self.ruta_csv = Path(ruta_csv)
        self.ruta_csv.parent.mkdir(parents=True, exist_ok=True)
    
    def crear_archivo(self, encabezados):
        """Crea el archivo CSV con encabezados si no existe"""
        if not self.ruta_csv.exists():
            with open(self.ruta_csv, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=encabezados)
                writer.writeheader()
    
    def agregar_fila(self, datos):
        """Agrega una fila al CSV"""
        with open(self.ruta_csv, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=datos.keys())
            writer.writerow(datos)
    
    def leer_todos(self):
        """Lee todos los registros del CSV"""
        registros = []
        try:
            with open(self.ruta_csv, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                registros = list(reader)
        except FileNotFoundError:
            pass
        return registros
    
    def limpiar_archivo(self):
        """Limpia el contenido del CSV manteniendo encabezados"""
        if self.ruta_csv.exists():
            with open(self.ruta_csv, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                encabezados = next(reader, None)
            
            if encabezados:
                with open(self.ruta_csv, "w", newline="", encoding="utf-8") as f:
                    writer = csv.DictWriter(f, fieldnames=encabezados)
                    writer.writeheader()
