import ttkbootstrap as tb
from ui.ventana_llamado import VentanaLlamado


class VentanaPrincipal(tb.Window):

    def __init__(self):
        super().__init__(title="Sistema de Citas", themename="flatly")
        self.geometry("900x600")
        self.llamado = None  # referencia a la ventana de llamado
        self._crear_widgets()

    def _crear_widgets(self):
        titulo = tb.Label(self, text="Registro de Citas", font=("Arial", 20))
        titulo.pack(pady=20)

        # Botón para abrir la pantalla de llamado
        tb.Button(
            self,
            text="Ir a llamada",
            bootstyle="primary",
            command=self.abrir_llamado
        ).pack(pady=10)

        # Botón para agregar pacientes de prueba
        tb.Button(
            self,
            text="Agregar paciente a la cola",
            bootstyle="success",
            command=self.agregar_paciente
        ).pack(pady=10)

        # Botón "Siguiente"
        tb.Button(
            self,
            text="👉 Siguiente",
            bootstyle="warning",
            command=self.llamar_siguiente
        ).pack(pady=10)

    # ================================
    # Abrir ventana de llamado
    # ================================
    def abrir_llamado(self):
        if self.llamado is None or not self.llamado.winfo_exists():
            self.llamado = VentanaLlamado(parent=self)
        else:
            self.llamado.lift()

    # ================================
    # Agregar pacientes de prueba
    # ================================
    def agregar_paciente(self):
        if self.llamado is None:
            return

        import random
        numero = str(random.randint(1, 99))
        nombre = f"Paciente {numero}"
        hora = "10:00"
        profesional = "Fonoaudióloga"

        self.llamado.agregar_a_cola(numero, nombre, hora, profesional)

    # ================================
    # Llamar siguiente
    # ================================
    def llamar_siguiente(self):
        if self.llamado:
            self.llamado.llamar_siguiente()
