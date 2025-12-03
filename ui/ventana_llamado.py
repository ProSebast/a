import ttkbootstrap as tb
from tkinter import Canvas
import screeninfo

class VentanaLlamado(tb.Toplevel):
    def __init__(self, parent, numero="__", nombre="", hora="", profesional=""):
        super().__init__(parent)

        # --- Ventana sin bordes ---
        self.overrideredirect(True)
        self.configure(bg="#e6f2fa")

        # --- Información inicial ---
        self.numero = numero
        self.nombre = nombre
        self.hora = hora
        self.profesional = profesional

        self.canvas = Canvas(self, bg="#e6f2fa", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # --- Detectar segundo monitor ---
        self.monitor = self.obtener_segundo_monitor()
        self.geometry(f"{self.monitor.width}x{self.monitor.height}+{self.monitor.x}+{self.monitor.y}")
        self.update_idletasks()

        # --- Textos centrados ---
        self.numero_main = self.canvas.create_text(self.monitor.width//2, self.monitor.height//5,
                                                   text=self.numero, font=("Helvetica", 80, "bold"), fill="#333")
        self.nombre_main = self.canvas.create_text(self.monitor.width//2, self.monitor.height//5 + 150,
                                                   text=self.nombre, font=("Helvetica", 40, "bold"), fill="#007BFF")
        self.hora_main   = self.canvas.create_text(self.monitor.width//2, self.monitor.height//5 + 250,
                                                   text=self.hora, font=("Helvetica", 30), fill="#333")
        self.pro_main    = self.canvas.create_text(self.monitor.width//2, self.monitor.height//5 + 350,
                                                   text=self.profesional, font=("Helvetica", 30), fill="#28a745")

    def obtener_segundo_monitor(self):
        monitores = screeninfo.get_monitors()
        if len(monitores) < 2:
            print("Solo se detecta un monitor. Usando el principal.")
            return monitores[0]
        else:
            return monitores[1]

    def actualizar_llamado(self, numero="", nombre="", hora="", profesional=""):
        if numero: self.numero = numero
        if nombre: self.nombre = nombre
        if hora: self.hora = hora
        if profesional: self.profesional = profesional

        self.canvas.itemconfig(self.numero_main, text=self.numero)
        self.canvas.itemconfig(self.nombre_main, text=self.nombre)
        self.canvas.itemconfig(self.hora_main, text=self.hora)
        self.canvas.itemconfig(self.pro_main, text=self.profesional)
