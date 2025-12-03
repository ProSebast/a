import ttkbootstrap as tb
from ui.ventana_llamado import VentanaLlamado


class VentanaPrincipal(tb.Window):

    def __init__(self):
        super().__init__(title="Sistema de Citas", themename="flatly")
        self.geometry("900x600")
        self._crear_widgets()

    def _crear_widgets(self):
        titulo = tb.Label(self, text="Registro de Citas", font=("Arial", 20))
        titulo.pack(pady=20)

        # Botón para abrir la pantalla de llamado
        btn = tb.Button(
            self,
            text="Ir a llamada",
            bootstyle="primary",
            command=self.abrir_llamado  # <- Aquí se conecta el método correcto
        )
        btn.pack(pady=10)

    # === ESTE VA EN ventana_principal.py ===
    def abrir_llamado(self):
        """Abre la pantalla de llamado con datos de prueba por ahora."""
        VentanaLlamado(
            parent=self,
            numero="1",
            nombre="Juanito Pérez",
            hora="10:30",
            profesional="Fonoaudióloga"
        )
import ttkbootstrap as tb

class VentanaLlamado(tb.Toplevel):
    def __init__(self, parent, numero=0, nombre="", hora="", profesional=""):
        super().__init__(parent)
        self.title("Pantalla de Llamado")
        self.geometry("800x600")
        self.resizable(False, False)
        self.configure(padx=30, pady=30)

        # Labels guardados como atributos para poder actualizarlos
        self.numero_label = tb.Label(self, text=f"N° {numero}", font=("Arial", 48, "bold"))
        self.numero_label.pack(pady=10)

        self.nombre_label = tb.Label(self, text=f"Nombre: {nombre}", font=("Arial", 18))
        self.nombre_label.pack(pady=10)

        self.hora_label = tb.Label(self, text=f"Hora: {hora}", font=("Arial", 18))
        self.hora_label.pack(pady=10)

        self.pro_label = tb.Label(self, text=f"Profesional: {profesional}", font=("Arial", 18))
        self.pro_label.pack(pady=10)

        tb.Button(self, text="Cerrar", bootstyle="danger", command=self.destroy).pack(pady=20)

    def actualizar(self, numero, nombre, hora, profesional):
        """Actualiza los datos de la ventana sin crear una nueva."""
        self.numero_label.config(text=f"N° {numero}")
        self.nombre_label.config(text=f"Nombre: {nombre}")
        self.hora_label.config(text=f"Hora: {hora}")
        self.pro_label.config(text=f"Profesional: {profesional}")



