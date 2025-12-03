import ttkbootstrap as tb
from tkinter import Label

class VentanaLlamado(tb.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Sistema de Llamado")
        self.geometry("600x400")  # tamaño fijo, no fullscreen

        # Labels para mostrar datos
        self.label_numero = Label(self, text="Número: __", font=("Arial", 24))
        self.label_numero.pack(pady=20)

        self.label_nombre = Label(self, text="Nombre: __", font=("Arial", 20))
        self.label_nombre.pack(pady=10)

        self.label_hora = Label(self, text="Hora: __", font=("Arial", 20))
        self.label_hora.pack(pady=10)

        self.label_prof = Label(self, text="Profesional: __", font=("Arial", 20))
        self.label_prof.pack(pady=10)

    def actualizar(self, numero, nombre, hora, profesional):
        self.label_numero.config(text=f"Número: {numero}")
        self.label_nombre.config(text=f"Nombre: {nombre}")
        self.label_hora.config(text=f"Hora: {hora}")
        self.label_prof.config(text=f"Profesional: {profesional}")
