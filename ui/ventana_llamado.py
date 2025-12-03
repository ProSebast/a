import ttkbootstrap as tb
from tkinter import Canvas
import screeninfo

class VentanaLlamado(tb.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        # --- Ventana sin bordes ---
        self.overrideredirect(True)
        self.configure(bg="#e6f2fa")

        # --- Cola de llamados ---
        self.cola = []

        # --- Canvas ---
        self.canvas = Canvas(self, bg="#e6f2fa", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # --- Detectar segundo monitor ---
        self.monitor = self.obtener_segundo_monitor()
        self.geometry(f"{self.monitor.width}x{self.monitor.height}+{self.monitor.x}+{self.monitor.y}")
        self.update_idletasks()

        # --- Textos centrados ---
        self.numero_main = self.canvas.create_text(self.monitor.width//2, self.monitor.height//5,
                                                   text="000", font=("Helvetica", 80, "bold"), fill="#333")
        self.nombre_main = self.canvas.create_text(self.monitor.width//2, self.monitor.height//5 + 150,
                                                   text="", font=("Helvetica", 40, "bold"), fill="#007BFF")
        self.hora_main   = self.canvas.create_text(self.monitor.width//2, self.monitor.height//5 + 250,
                                                   text="", font=("Helvetica", 30), fill="#333")
        self.pro_main    = self.canvas.create_text(self.monitor.width//2, self.monitor.height//5 + 350,
                                                   text="", font=("Helvetica", 30), fill="#28a745")

    def obtener_segundo_monitor(self):
        monitores = screeninfo.get_monitors()
        if len(monitores) < 2:
            print("Solo se detecta un monitor. Usando el principal.")
            return monitores[0]
        else:
            return monitores[1]

    def agregar_llamado(self, nombre="", hora="", profesional=""):
        # Generar número automático: el primero será 001
        numero = f"{len(self.cola) + 1:03d}"
        self.cola.append({
            "numero": numero,
            "nombre": nombre,
            "hora": hora,
            "profesional": profesional
        })
        self.actualizar_pantalla()


    def actualizar_pantalla(self):
        if len(self.cola) > 0:
            p = self.cola[-1]  # mostrar siempre el último agregado
            self.canvas.itemconfig(self.numero_main, text=p["numero"])
            self.canvas.itemconfig(self.nombre_main, text=p["nombre"])
            self.canvas.itemconfig(self.hora_main,   text=f"Asignado: {p['hora']}")
            self.canvas.itemconfig(self.pro_main,    text=f"Profesional: {p['profesional']}")
        else:
            self.canvas.itemconfig(self.numero_main, text="000")
            self.canvas.itemconfig(self.nombre_main, text="")
            self.canvas.itemconfig(self.hora_main,   text="")
            self.canvas.itemconfig(self.pro_main,    text="")
