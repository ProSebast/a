import pandas as pd
from pathlib import Path


class ExcelService:
    """Servicio para exportar datos a Excel"""
    
    def __init__(self, ruta_excel="reportes"):
        self.ruta_reportes = Path(__file__).parent.parent / ruta_excel
        self.ruta_reportes.mkdir(exist_ok=True)
    
    def exportar_a_excel(self, datos, nombre_archivo="reporte_llamados.xlsx"):
        """
        Exporta los datos a un archivo Excel
        
        Args:
            datos: Lista de diccionarios con los datos
            nombre_archivo: Nombre del archivo Excel
        """
        try:
            df = pd.DataFrame(datos)
            ruta_completa = self.ruta_reportes / nombre_archivo
            df.to_excel(ruta_completa, index=False, sheet_name="Llamados")
            return True, f"Archivo guardado en: {ruta_completa}"
        except Exception as e:
            return False, f"Error al exportar: {str(e)}"
    
    def leer_excel(self, ruta_archivo):
        """
        Lee datos de un archivo Excel
        
        Args:
            ruta_archivo: Ruta del archivo Excel
            
        Returns:
            Lista de diccionarios con los datos
        """
        try:
            df = pd.read_excel(ruta_archivo)
            return df.to_dict('records')
        except Exception as e:
            print(f"Error al leer Excel: {str(e)}")
            return []
