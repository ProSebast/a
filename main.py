import ttkbootstrap as tb
from ui.ventana_llamado import VentanaLlamado
from ui.panel_ingreso import PanelIngreso  # <-- importar el panel

class VentanaPrincipal(tb.Window):
    def __init__(self):
        super().__init__(title="Sistema de Citas", themename="flatly")
        self.geometry("900x600")
        self._crear_widgets()

    def _crear_widgets(self):
        titulo = tb.Label(self, text="Registro de Citas", font=("Arial", 20))
        titulo.pack(pady=20)

        # Botón 1: Mostrar en pantalla (HTML/HDMI/TV)
        btn_html = tb.Button(
            self,
            text="Mostrar en TV (HTML)",
            bootstyle="primary",
            command=self.abrir_panel_ingreso
        )
        btn_html.pack(pady=10)

        # Botón 2: Transmitir por Internet
        btn_stream = tb.Button(
            self,
            text="Transmitir por Internet",
            bootstyle="success",
            command=self.transmitir_internet
        )
        btn_stream.pack(pady=10)

    # === FUNCIÓN 1: Abrir panel de ingreso de datos ===
    def abrir_panel_ingreso(self):
        PanelIngreso(self)

    # === FUNCIÓN 2: Transmisión por Internet ===
    def transmitir_internet(self):
        print("Aquí luego transmitiremos por internet.")
        # Aquí después armamos la transmisión (Flask + página web)


if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
