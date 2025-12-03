import ttkbootstrap as tb
from tkinter import Label

class VentanaLlamado(tb.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Sistema de Llamado")
        self.geometry("600x400")  # Ventana simple
        # No fullscreen, no canvas, nada más

    def mostrar_sin_diseño(self):
        Label(self, text="SISTEMA DE LLAMADO", font=("Arial", 30)).pack(expand=True)
