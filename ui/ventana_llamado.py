import ttkbootstrap as tb
from tkinter import Canvas

class VentanaLlamado(tb.Toplevel):
    def __init__(self, parent, nombre="", hora="", profesional="", numero="__"):
        super().__init__(parent)

        self.title("Pantalla de Llamado")
        self.attributes("-fullscreen", True)
        self.configure(bg="#e6f2fa")  # Fondo azul claro

        # Canvas para control absoluto
        canvas = Canvas(self, bg="#e6f2fa", highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        # Recuadro negro
        self.recuadro = canvas.create_rectangle(
            200, 100, 1720, 880,  # coordenadas (x1,y1,x2,y2)
            outline="black", width=8
        )

        # Título
        self.titulo = canvas.create_text(
            960, 150,  # centrado horizontal
            text="🔊 Llamando",
            font=("Helvetica", 48, "bold"),
            fill="#333333"
        )

        # Número grande
        self.numero = canvas.create_text(
            960, 300,
            text=f"{numero}",
            font=("Helvetica", 140, "bold"),
            fill="#333333"
        )

        # Nombre
        self.nombre = canvas.create_text(
            960, 450,
            text=f"{nombre}",
            font=("Helvetica", 60, "bold"),
            fill="#007BFF"  # azul
        )

        # Hora
        self.hora = canvas.create_text(
            960, 550,
            text=f"Asignado: {hora}",
            font=("Helvetica", 36, "bold"),
            fill="#333333"
        )

        # Profesional
        self.profesional = canvas.create_text(
            960, 630,
            text=f"Profesional: {profesional}",
            font=("Helvetica", 36, "bold"),
            fill="#28a745"  # verde
        )

        self.canvas = canvas

    def actualizar(self, numero, nombre, hora, profesional):
        self.canvas.itemconfig(self.numero, text=f"{numero}")
        self.canvas.itemconfig(self.nombre, text=f"{nombre}")
        self.canvas.itemconfig(self.hora, text=f"Asignado: {hora}")
        self.canvas.itemconfig(self.profesional, text=f"Profesional: {profesional}")

