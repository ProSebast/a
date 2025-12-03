import ttkbootstrap as tb
from tkinter import Canvas

class VentanaLlamado(tb.Toplevel):

    def __init__(self, parent, numero="__", nombre="", hora="", profesional=""):
        super().__init__(parent)

        self.title("Pantalla de Llamado")
        self.attributes("-fullscreen", True)
        self.configure(bg="#e6f2fa")

        # --- COLA INFINITA ---
        self.cola = []  # una lista dinámica con todos los pacientes

        # Si viene un primer paciente desde la ventana principal, lo cargamos
        if numero != "__":
            self.cola.append({
                "numero": numero,
                "nombre": nombre,
                "hora": hora,
                "profesional": profesional
            })

        # Canvas general
        canvas = Canvas(self, bg="#e6f2fa", highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        self.canvas = canvas

        # Recuadro
        canvas.create_rectangle(200, 100, 1720, 880, outline="black", width=8)

        # Título
        canvas.create_text(
            960, 150,
            text="🔊 Llamando",
            font=("Helvetica", 48, "bold"),
            fill="#333333"
        )

        # ZONA PRINCIPAL
        self.numero_main = canvas.create_text(960, 300, text="__", font=("Helvetica", 140, "bold"), fill="#333")
        self.nombre_main = canvas.create_text(960, 450, text="", font=("Helvetica", 60, "bold"), fill="#007BFF")
        self.hora_main   = canvas.create_text(960, 550, text="", font=("Helvetica", 36, "bold"), fill="#333")
        self.pro_main    = canvas.create_text(960, 630, text="", font=("Helvetica", 36, "bold"), fill="#28a745")

        # LISTA DE ESPERA VISUAL (N2 y N3)
        y_base = 760
        self.siguientes = []

        for i in range(2):  # solo se muestran 2 pero pueden haber 100 en cola
            item = {
                "numero": canvas.create_text(350, y_base + i*80, text="__", font=("Helvetica", 32, "bold"), fill="#444"),
                "nombre": canvas.create_text(650, y_base + i*80, text="", font=("Helvetica", 24), fill="#007BFF"),
                "hora":   canvas.create_text(1000, y_base + i*80, text="", font=("Helvetica", 20), fill="#333"),
                "prof":   canvas.create_text(1350, y_base + i*80, text="", font=("Helvetica", 20), fill="#28a745"),
            }
            self.siguientes.append(item)

        # Botón siguiente
        tb.Button(
            self,
            text="👉 Llamar Siguiente",
            bootstyle="success",
            command=self.llamar_siguiente
        ).place(x=50, y=50)

        # Refrescar pantalla inicial
        self.actualizar_pantalla()

    # ======================================================
    # AGREGAR A COLA (infinita)
    # ======================================================
    def agregar_a_cola(self, numero, nombre, hora, profesional):
        self.cola.append({
            "numero": numero,
            "nombre": nombre,
            "hora": hora,
            "profesional": profesional
        })
        self.actualizar_pantalla()

    # ======================================================
    # MOVER LA COLA
    # ======================================================
    def llamar_siguiente(self):
        if len(self.cola) > 0:
            self.cola.pop(0)  # elimina el primero
        self.actualizar_pantalla()

    # ======================================================
    # ACTUALIZAR TODO
    # ======================================================
    def actualizar_pantalla(self):
        # Principal
        if len(self.cola) > 0:
            p = self.cola[0]
            self.canvas.itemconfig(self.numero_main, text=p["numero"])
            self.canvas.itemconfig(self.nombre_main, text=p["nombre"])
            self.canvas.itemconfig(self.hora_main,   text=f"Asignado: {p['hora']}")
            self.canvas.itemconfig(self.pro_main,    text=f"Profesional: {p['profesional']}")
        else:
            self.canvas.itemconfig(self.numero_main, text="__")
            self.canvas.itemconfig(self.nombre_main, text="")
            self.canvas.itemconfig(self.hora_main,   text="")
            self.canvas.itemconfig(self.pro_main,    text="")

        # Mostrar n°2 y n°3
        for i in range(2):
            if len(self.cola) > i+1:
                item = self.cola[i+1]
                self.canvas.itemconfig(self.siguientes[i]["numero"], text=item["numero"])
                self.canvas.itemconfig(self.siguientes[i]["nombre"], text=item["nombre"])
                self.canvas.itemconfig(self.siguientes[i]["hora"],   text=item["hora"])
                self.canvas.itemconfig(self.siguientes[i]["prof"],   text=item["profesional"])
            else:
                self.canvas.itemconfig(self.siguientes[i]["numero"], text="__")
                self.canvas.itemconfig(self.siguientes[i]["nombre"], text="")
                self.canvas.itemconfig(self.siguientes[i]["hora"],   text="")
                self.canvas.itemconfig(self.siguientes[i]["prof"],   text="")

    # ======================================================
    # COMPATIBILIDAD panel_ingreso.py
    # ======================================================
    def actualizar(self, numero, nombre, hora, profesional):
        self.agregar_a_cola(numero, nombre, hora, profesional)
