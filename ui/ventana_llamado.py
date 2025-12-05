import ttkbootstrap as tb
from tkinter import Canvas
import csv
from pathlib import Path
import screeninfo

class VentanaLlamado(tb.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(bg="#e6f2fa")
        
        # Carpeta para guardar CSV
        self.datos_path = Path(__file__).parent / "Datos_llamdo"
        self.datos_path.mkdir(exist_ok=True)
        self.csv_file = self.datos_path / "llamados.csv"

        # Crear archivo con encabezados si no existe
        if not self.csv_file.exists():
            with open(self.csv_file, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["numero","nombre","hora","profesional"])
                writer.writeheader()

        # Cola de pacientes
        self.cola = []

        # Canvas
        self.canvas = Canvas(self, bg="#e6f2fa", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Detectar segundo monitor
        monitores = screeninfo.get_monitors()
        self.monitor = monitores[1] if len(monitores) > 1 else monitores[0]
        self.geometry(f"{self.monitor.width}x{self.monitor.height}+{self.monitor.x}+{self.monitor.y}")

        # Textos
        self.numero_main = self.canvas.create_text(self.monitor.width//2, self.monitor.height//5,
                                                   text="__", font=("Helvetica", 80, "bold"), fill="#333")
        self.nombre_main = self.canvas.create_text(self.monitor.width//2, self.monitor.height//5 + 150,
                                                   text="", font=("Helvetica", 40, "bold"), fill="#007BFF")
        self.hora_main   = self.canvas.create_text(self.monitor.width//2, self.monitor.height//5 + 250,
                                                   text="", font=("Helvetica", 30), fill="#333")
        self.pro_main    = self.canvas.create_text(self.monitor.width//2, self.monitor.height//5 + 350,
                                                   text="", font=("Helvetica", 30), fill="#28a745")

    # ================================
    # Agregar paciente a la cola
    # ================================
    def agregar_a_cola(self, numero, nombre, hora, profesional):
        self.cola.append({
            "numero": numero,
            "nombre": nombre,
            "hora": hora,
            "profesional": profesional
        })
        self.actualizar_llamado()

    # ================================
    # Mostrar paciente actual
    # ================================
    def actualizar_llamado(self):
        if self.cola:
            p = self.cola[0]
            self.canvas.itemconfig(self.numero_main, text=p["numero"])
            self.canvas.itemconfig(self.nombre_main, text=p["nombre"])
            self.canvas.itemconfig(self.hora_main, text=p["hora"])
            self.canvas.itemconfig(self.pro_main, text=p["profesional"])
        else:
            self.canvas.itemconfig(self.numero_main, text="__")
            self.canvas.itemconfig(self.nombre_main, text="")
            self.canvas.itemconfig(self.hora_main, text="")
            self.canvas.itemconfig(self.pro_main, text="")

    # ================================
    # Llamar siguiente paciente y guardar
    # ================================
    def llamar_siguiente(self):
        if self.cola:
            paciente = self.cola.pop(0)
            self.guardar_paciente(paciente)
        self.actualizar_llamado()

    # ================================
    # Guardar en CSV
    # ================================
    def guardar_paciente(self, paciente):
        with open(self.csv_file, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["numero","nombre","hora","profesional"])
            writer.writerow(paciente)
        print(f"✅ Paciente guardado: {paciente}")
