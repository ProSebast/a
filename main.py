"""
Punto de entrada del Sistema de Llamado de Citas
"""

import sys
from pathlib import Path

# Añadir el directorio de la aplicación al path
sys.path.insert(0, str(Path(__file__).parent))

from ui.ventana_principal import VentanaPrincipal

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
