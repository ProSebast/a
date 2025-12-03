import ttkbootstrap as tb
from ui.ventana_llamado import VentanaLlamado
from ui.panel_ingreso import PanelIngreso

class VentanaPrincipal(tb.Window):
    def __init__(self):
        super().__init__(title="Sistema de Citas", themename="flatly")
        self.geometry("900x600")
        self._crear_widgets()

    def _crear_widgets(self):
        titulo = tb.Label(self, text="Registro de Citas", font=("Arial", 20))
        titulo.pack(pady=20)

        # Botón: Abrir panel de ingreso
        btn_ingreso = tb.Button(
            self,
            text="Abrir Panel de Ingreso",
            bootstyle="primary",
            command=self.abrir_panel_ingreso
        )
        btn_ingreso.pack(pady=10)

        # Botón: Abrir ventana de llamado
        btn_llamado = tb.Button(
            self,
            text="Abrir Ventana de Llamado",
            bootstyle="success",
            command=self.abrir_ventana_llamado
        )
        btn_llamado.pack(pady=10)

    def abrir_panel_ingreso(self):
        PanelIngreso(self)

    def abrir_ventana_llamado(self):
        # Ventana de llamado vacía, sin fullscreen ni diseño
        ventana = VentanaLlamado(self)
        ventana.mostrar_sin_diseño()  # Método que implementaremos en ventana_llamado

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
