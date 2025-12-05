from tkinter import messagebox
from .estilos import COLORES, FUENTES, ANCHO_VENTANA_PRINCIPAL, ALTO_VENTANA_PRINCIPAL
import ttkbootstrap as tb
from .ventana_llamado import VentanaLlamado 
class VentanaPrincipal(tb.Window):
    def __init__(self):
        super().__init__(title="Sistema de Llamado de Citas", themename="flatly")
        self.geometry(f"{ANCHO_VENTANA_PRINCIPAL}x{ALTO_VENTANA_PRINCIPAL}")
        self.configure(bg=COLORES["fondo_principal"])

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
        nombre = self.nombre_var.get().strip()
        hora = self.hora_var.get().strip()
        prof = self.pro_var.get().strip()
        
        # Validar campos
        if not nombre or not hora or not prof:
            messagebox.showwarning("Validación", "Por favor completa todos los campos")
            return

        numero_formateado = f"{self.numero_actual:03}"

        # Crear fila
        fila = tb.Frame(self.contenedor_registros)
        fila.pack(fill="x", pady=5)

        # Labels
        tb.Label(fila, text=numero_formateado, font=FUENTES["normal"], width=8).pack(side="left", padx=5)
        tb.Label(fila, text=nombre, font=FUENTES["normal"], width=20).pack(side="left", padx=5)
        tb.Label(fila, text=hora, font=FUENTES["normal"], width=10).pack(side="left", padx=5)
        tb.Label(fila, text=prof, font=FUENTES["normal"], width=15).pack(side="left", padx=5)

        # Botón Llamar
        btn_llamar = tb.Button(fila, text="📢 Llamar", bootstyle="info", width=10,
                               command=lambda n=numero_formateado, nom=nombre, h=hora, p=prof, f=fila: self.llamar(n, nom, h, p, f))
        btn_llamar.pack(side="left", padx=5)

        self.numero_actual += 1
        self.nombre_var.set("")
        self.hora_var.set("")
        self.pro_var.set("")

    def limpiar_lista(self):
        """Limpia todos los registros de la lista"""
        for widget in self.contenedor_registros.winfo_children():
            if widget.winfo_class() == "TFrame":
                widget.destroy()
        self.numero_actual = 1

    def llamar(self, numero, nombre, hora, profesional, fila):
        """Llama al paciente y lo muestra en la ventana de llamado"""
        # Agregar paciente a la cola (se muestra en la ventana)
        self.ventana_llamado.agregar_a_cola(numero, nombre, hora, profesional)
        # Guardar el paciente que acaba de ser agregado
        self.ventana_llamado.guardar_paciente({
            "numero": numero,
            "nombre": nombre,
            "hora": hora,
            "profesional": profesional
        })
        # Cambiar color de la fila a gris (para indicar que ya fue llamada)
        for widget in fila.winfo_children():
            if isinstance(widget, tb.Label):
                widget.configure(foreground="#999999")
        # Eliminar la fila después de 2 segundos
        self.after(2000, fila.destroy)
