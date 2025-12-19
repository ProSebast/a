from tkinter import messagebox
from .estilos import COLORES, FUENTES, ANCHO_VENTANA_PRINCIPAL, ALTO_VENTANA_PRINCIPAL
import ttkbootstrap as tb
from .ventana_llamado import VentanaLlamado 


class VentanaPrincipal(tb.Window):
    def __init__(self):
        super().__init__(title="Sistema de Llamado de Citas", themename="flatly")
        self.geometry(f"{ANCHO_VENTANA_PRINCIPAL}x{ALTO_VENTANA_PRINCIPAL}")
        self.configure(bg=COLORES["fondo_principal"])

        self.numero_actual = 1
        self.ventana_llamado = VentanaLlamado(self)

        self._crear_widgets()

    def _crear_widgets(self):
        # ===== CONTENEDOR PRINCIPAL =====
        main_container = tb.Frame(self, padding=20)
        main_container.pack(fill="both", expand=True)

        # ===== TÍTULO =====
        tb.Label(
            main_container,
            text="📋 Sistema de Llamado de Citas",
            font=("Arial", 20, "bold"),
            bootstyle="primary"
        ).pack(anchor="w", pady=(0, 20))

        # ===== CARD FORMULARIO =====
        card_form = tb.Frame(
            main_container,
            padding=20,
            bootstyle="light",
        )
        card_form.pack(fill="x", pady=(0, 25))

        tb.Label(
            card_form,
            text="Agregar nueva cita",
            font=("Arial", 14, "bold")
        ).grid(row=0, column=0, columnspan=6, sticky="w", pady=(0, 15))

        # Variables
        self.nombre_var = tb.StringVar()
        self.hora_var = tb.StringVar()
        self.pro_var = tb.StringVar()

        # Nombre
        tb.Label(card_form, text="Nombre").grid(row=1, column=0, sticky="w", padx=(0, 5))
        tb.Entry(card_form, textvariable=self.nombre_var, width=25).grid(row=1, column=1, padx=(0, 15))

        # Hora
        tb.Label(card_form, text="Hora").grid(row=1, column=2, sticky="w", padx=(0, 5))
        tb.Entry(card_form, textvariable=self.hora_var, width=15).grid(row=1, column=3, padx=(0, 15))

        # Profesional
        tb.Label(card_form, text="Profesional").grid(row=1, column=4, sticky="w", padx=(0, 5))
        tb.Entry(card_form, textvariable=self.pro_var, width=25).grid(row=1, column=5)

        # Botón agregar
        tb.Button(
            card_form,
            text="➕ Agregar cita",
            bootstyle="primary",
            width=20,
            command=self.agregar_registro
        ).grid(row=2, column=0, columnspan=6, pady=(15, 0), sticky="e")

        # ===== CARD LISTA =====
        card_lista = tb.Frame(main_container, padding=15, bootstyle="light")
        card_lista.pack(fill="both", expand=True)

        tb.Label(
            card_lista,
            text="Listado de citas",
            font=("Arial", 14, "bold")
        ).pack(anchor="w", pady=(0, 10))

        # Contenedor registros
        self.contenedor_registros = tb.Frame(card_lista)
        self.contenedor_registros.pack(fill="both", expand=True)

        # Cabecera estilo tabla
        cabecera = tb.Frame(self.contenedor_registros, bootstyle="secondary", padding=8)
        cabecera.pack(fill="x", pady=(0, 5))

        for t, w in zip(
            ["N°", "Nombre", "Hora", "Profesional", "Acción"],
            [6, 20, 10, 18, 12]
        ):
            tb.Label(
                cabecera,
                text=t,
                font=("Arial", 11, "bold"),
                width=w,
                foreground="white"
            ).pack(side="left", padx=3)

    def agregar_registro(self):
        nombre = self.nombre_var.get().strip()
        hora = self.hora_var.get().strip()
        prof = self.pro_var.get().strip()
        
        if not nombre or not hora or not prof:
            messagebox.showwarning("Validación", "Por favor completa todos los campos")
            return

        numero_formateado = f"{self.numero_actual:03}"

        fila = tb.Frame(self.contenedor_registros, padding=6)
        fila.pack(fill="x", pady=3)

        tb.Label(fila, text=numero_formateado, width=6).pack(side="left")
        tb.Label(fila, text=nombre, width=20, anchor="w").pack(side="left", padx=3)
        tb.Label(fila, text=hora, width=10).pack(side="left", padx=3)
        tb.Label(fila, text=prof, width=18, anchor="w").pack(side="left", padx=3)

        tb.Button(
            fila,
            text="📢 Llamar",
            bootstyle="info",
            width=12,
            command=lambda n=numero_formateado, nom=nombre, h=hora, p=prof, f=fila:
                self.llamar(n, nom, h, p, f)
        ).pack(side="left", padx=5)

        self.numero_actual += 1
        self.nombre_var.set("")
        self.hora_var.set("")
        self.pro_var.set("")

    def limpiar_lista(self):
        for widget in self.contenedor_registros.winfo_children():
            if widget.winfo_class() == "TFrame":
                widget.destroy()
        self.numero_actual = 1

    def llamar(self, numero, nombre, hora, profesional, fila):
        self.ventana_llamado.agregar_a_cola(numero, nombre, hora, profesional)
        self.ventana_llamado.guardar_paciente({
            "numero": numero,
            "nombre": nombre,
            "hora": hora,
            "profesional": profesional
        })

        for widget in fila.winfo_children():
            if isinstance(widget, tb.Label):
                widget.configure(foreground="#999999")

        self.after(2000, fila.destroy)
