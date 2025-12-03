import ttkbootstrap as tb
from tkinter import Canvas
import screeninfo

class VentanaLlamado(tb.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.overrideredirect(True)
        self.configure(bg="#e6f2fa")

        self.canvas = Canvas(self, bg="#e6f2fa", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Detectar segundo monitor
        monitores = screeninfo.get_monitors()
        self.monitor = monitores[1] if len(monitores) > 1 else monitores[0]
        self.geometry(f"{self.monitor.width}x{self.monitor.height}+{self.monitor.x}+{self.monitor.y}")

        # Textos
        self.numero_main = self.canvas.create_text(self.monitor.width//2, self.monitor.height//5,
                                                   text="000", font=("Helvetica", 80, "bold"), fill="#333")
        self.nombre_main = self.canvas.create_text(self.monitor.width//2, self.monitor.height//5 + 150,
                                                   text="", font=("Helvetica", 40, "bold"), fill="#007BFF")
        self.hora_main   = self.canvas.create_text(self.monitor.width//2, self.monitor.height//5 + 250,
                                                   text="", font=("Helvetica", 30), fill="#333")
        self.pro_main    = self.canvas.create_text(self.monitor.width//2, self.monitor.height//5 + 350,
                                                   text="", font=("Helvetica", 30), fill="#28a745")

    def actualizar_llamado(self, numero="", nombre="", hora="", profesional=""):
        self.canvas.itemconfig(self.numero_main, text=numero)
        self.canvas.itemconfig(self.nombre_main, text=nombre)
        self.canvas.itemconfig(self.hora_main, text=hora)
        self.canvas.itemconfig(self.pro_main, text=profesional)
