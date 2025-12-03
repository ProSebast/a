import ttkbootstrap as tb
from tkinter import Label, Entry, Button
from ui.ventana_llamado import VentanaLlamado

class VentanaPrincipal(tb.Window):
    def __init__(self):
        super().__init__(title="Ingreso de Datos", themename="flatly")
        self.geometry("500x400")

        Label(self, text="Número", font=("Arial", 14)).pack(pady=5)
        self.entry_numero = Entry(self)
        self.entry_numero.pack(pady=5)

        Label(self, text="Nombre", font=("Arial", 14)).pack(pady=5)
        self.entry_nombre = Entry(self)
        self.entry_nombre.pack(pady=5)

        Label(self, text="Hora", font=("Arial", 14)).pack(pady=5)
        self.entry_hora = Entry(self)
        self.entry_hora.pack(pady=5)

        Label(self, text="Profesional", font=("Arial", 14)).pack(pady=5)
        self.entry_prof = Entry(self)
        self.entry_prof.pack(pady=5)

        # Botón para llamar
        Button(self, text="Llamar", command=self.abrir_llamado).pack(pady=20)

        # Ventana de llamado inicial vacía
        self.ventana_llamado = VentanaLlamado(self)

    def abrir_llamado(self):
        numero = self.entry_numero.get()
        nombre = self.entry_nombre.get()
        hora = self.entry_hora.get()
        profesional = self.entry_prof.get()

        # Actualiza la ventana de llamado
        self.ventana_llamado.actualizar(numero, nombre, hora, profesional)
