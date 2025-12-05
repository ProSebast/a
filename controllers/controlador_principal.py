from pathlib import Path
from services.csv_service import CSVService
from models.registro import RegistroPaciente


class ControladorPrincipal:
    """Controlador principal para la gestión de registros"""
    
    def __init__(self):
        # Ruta del CSV de registros
        self.csv_service = CSVService(
            Path(__file__).parent.parent / "data" / "registros.csv"
        )
        self.encabezados = ["numero", "nombre", "hora", "profesional"]
        self.csv_service.crear_archivo(self.encabezados)
        self.registros = []
    
    def agregar_registro(self, numero, nombre, hora, profesional):
        """Agrega un nuevo registro"""
        registro = {
            "numero": numero,
            "nombre": nombre,
            "hora": hora,
            "profesional": profesional
        }
        self.csv_service.agregar_fila(registro)
        self.registros.append(registro)
        return True
    
    def obtener_registros(self):
        """Obtiene todos los registros"""
        return self.csv_service.leer_todos()
    
    def limpiar_registros(self):
        """Limpia todos los registros"""
        self.csv_service.limpiar_archivo()
        self.registros = []
