import ttkbootstrap as tb
from .ventana_llamado import VentanaLlamado

class VentanaPrincipal(tb.Window):
    def __init__(self):
        super().__init__(title="Ingreso de Datos", themename="flatly")
        self.geometry("900x600")

        self.numero_actual = 1  # Para el formato 000
        self.ventana_llamado = VentanaLlamado(self)

        self._crear_widgets()

    def _crear_widgets(self):
        # Entradas
        self.nombre_var = tb.StringVar()
        self.hora_var = tb.StringVar()
        self.pro_var = tb.StringVar()

        tb.Label(self, text="Nombre").pack()
        tb.Entry(self, textvariable=self.nombre_var).pack()
        tb.Label(self, text="Hora").pack()
        tb.Entry(self, textvariable=self.hora_var).pack()
        tb.Label(self, text="Profesional").pack()
        tb.Entry(self, textvariable=self.pro_var).pack()

        tb.Button(self, text="Agregar", bootstyle="primary", command=self.agregar_registro).pack(pady=10)

        # Contenedor de registros (como “tabla”)
        self.contenedor_registros = tb.Frame(self)
        self.contenedor_registros.pack(fill="both", expand=True, pady=20)

        # Cabeceras
        cabecera = tb.Frame(self.contenedor_registros)
        cabecera.pack(fill="x")
        for t, w in zip(["Numero", "Nombre", "Hora", "Profesional", "Accion"], [80, 200, 100, 150, 100]):
            tb.Label(cabecera, text=t, font=("Arial", 12, "bold"), width=w//10).pack(side="left")

    def agregar_registro(self):
        numero_formateado = f"{self.numero_actual:03}"
        nombre = self.nombre_var.get()
        hora = self.hora_var.get()
        prof = self.pro_var.get()

        # Crear fila
        fila = tb.Frame(self.contenedor_registros)
        fila.pack(fill="x", pady=2)

        # Labels
        tb.Label(fila, text=numero_formateado, width=8).pack(side="left")
        tb.Label(fila, text=nombre, width=20).pack(side="left")
        tb.Label(fila, text=hora, width=10).pack(side="left")
        tb.Label(fila, text=prof, width=15).pack(side="left")

        # Botón Llamar
        btn_llamar = tb.Button(fila, text="Llamar", bootstyle="success",
                               command=lambda n=numero_formateado, nom=nombre, h=hora, p=prof, f=fila: self.llamar(n, nom, h, p, f))
        btn_llamar.pack(side="left", padx=5)

        self.numero_actual += 1
        self.nombre_var.set("")
        self.hora_var.set("")
        self.pro_var.set("")

    def llamar(self, numero, nombre, hora, profesional, fila):
        # Agregar paciente a la cola (se muestra en la ventana)
        self.ventana_llamado.agregar_a_cola(numero, nombre, hora, profesional)
        # Guardar el paciente que acaba de ser agregado
        self.ventana_llamado.guardar_paciente({
            "numero": numero,
            "nombre": nombre,
            "hora": hora,
            "profesional": profesional
        })
        # Eliminar la fila de la lista
        fila.destroy()
