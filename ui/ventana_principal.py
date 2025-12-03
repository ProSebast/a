import ttkbootstrap as tb
from ui.ventana_llamado import VentanaLlamado

class VentanaPrincipal(tb.Window):
    def __init__(self):
        super().__init__(title="Ingreso de Datos", themename="flatly")
        self.geometry("500x400")

        # --- Campos de ingreso ---
        tb.Label(self, text="Nombre:").pack(pady=5)
        self.entry_nombre = tb.Entry(self)
        self.entry_nombre.pack()

        tb.Label(self, text="Hora:").pack(pady=5)
        self.entry_hora = tb.Entry(self)
        self.entry_hora.pack()

        tb.Label(self, text="Profesional:").pack(pady=5)
        self.entry_pro = tb.Entry(self)
        self.entry_pro.pack()

        # --- Botón Llamar ---
        tb.Button(self, text="Llamar", bootstyle="success", command=self.abrir_llamado).pack(pady=20)

        # --- Crear ventana llamado (segunda pantalla) ---
        self.ventana_llamado = VentanaLlamado(self)

    def abrir_llamado(self):
        nombre = self.entry_nombre.get()
        hora = self.entry_hora.get()
        profesional = self.entry_pro.get()

        self.ventana_llamado.actualizar_llamado(
            nombre=nombre,
            hora=hora,
            profesional=profesional
        )
