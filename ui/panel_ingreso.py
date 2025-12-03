import ttkbootstrap as tb
from ui.ventana_llamado import VentanaLlamado


contador_llamados = 0  # Contador global
ventana_llamado_instancia = None  # Instancia única de la ventana de llamado

class PanelIngreso(tb.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Panel de Ingreso de Datos")
        self.geometry("400x350")
        self.resizable(False, False)
        self.configure(padx=20, pady=20)

        self.nombre = tb.StringVar()
        self.hora = tb.StringVar()
        self.profesional = tb.StringVar()

        tb.Label(self, text="Nombre:").pack(anchor="w")
        tb.Entry(self, textvariable=self.nombre).pack(fill="x", pady=5)

        tb.Label(self, text="Hora:").pack(anchor="w")
        tb.Entry(self, textvariable=self.hora).pack(fill="x", pady=5)

        tb.Label(self, text="Profesional:").pack(anchor="w")
        tb.Entry(self, textvariable=self.profesional).pack(fill="x", pady=5)

        tb.Button(
            self,
            text="Mostrar en TV",
            bootstyle="success",
            command=self.mostrar_en_tv
        ).pack(pady=10)

        tb.Button(
            self,
            text="Limpiar",
            bootstyle="warning",
            command=self.limpiar
        ).pack()

    def mostrar_en_tv(self):
        global contador_llamados, ventana_llamado_instancia
        contador_llamados += 1

        if ventana_llamado_instancia and ventana_llamado_instancia.winfo_exists():
            # Si la ventana ya existe, solo actualizamos los datos
            ventana_llamado_instancia.actualizar(
                numero=contador_llamados,
                nombre=self.nombre.get(),
                hora=self.hora.get(),
                profesional=self.profesional.get()
            )
        else:
            # Si no existe, la creamos
            ventana_llamado_instancia = VentanaLlamado(
                self,
                numero=contador_llamados,
                nombre=self.nombre.get(),
                hora=self.hora.get(),
                profesional=self.profesional.get()
            )
            ventana_llamado_instancia.attributes("-fullscreen", True)
            ventana_llamado_instancia.focus_set()

    def limpiar(self):
        self.nombre.set("")
        self.hora.set("")
        self.profesional.set("")
