from tkinter import messagebox
from .estilos import ANCHO_VENTANA_PRINCIPAL, ALTO_VENTANA_PRINCIPAL
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from .ventana_llamado import VentanaLlamado


class VentanaPrincipal(tb.Window):
    def __init__(self):
        super().__init__(
            title="Sistema de Llamado de Citas",
            themename="flatly",
            size=(ANCHO_VENTANA_PRINCIPAL, ALTO_VENTANA_PRINCIPAL)
        )

        self.configure(bg="#F4F6F8")  # fondo profesional

        self.numero_actual = 1
        self.ventana_llamado = VentanaLlamado(self)

        self._crear_widgets()

    def _crear_widgets(self):
        main = tb.Frame(self, padding=20)
        main.pack(fill=BOTH, expand=True)

        # ===== TÍTULO =====
        tb.Label(
            main,
            text="📋 Sistema de Llamado de Citas",
            font=("Segoe UI", 20, "bold"),
            bootstyle=PRIMARY
        ).pack(anchor=W, pady=(0, 20))

        # ===== FORMULARIO =====
        form = tb.Labelframe(
            main,
            text=" Agregar nueva cita ",
            padding=15,
            bootstyle=LIGHT
        )
        form.pack(fill=X, pady=(0, 20))

        self.nombre_var = tb.StringVar()
        self.hora_var = tb.StringVar()
        self.pro_var = tb.StringVar()

        tb.Label(form, text="Nombre").grid(row=0, column=0, sticky=W, padx=5)
        tb.Entry(form, textvariable=self.nombre_var, width=25).grid(row=0, column=1, padx=10)

        tb.Label(form, text="Hora").grid(row=0, column=2, sticky=W, padx=5)
        tb.Entry(form, textvariable=self.hora_var, width=15).grid(row=0, column=3, padx=10)

        tb.Label(form, text="Profesional").grid(row=0, column=4, sticky=W, padx=5)
        tb.Entry(form, textvariable=self.pro_var, width=25).grid(row=0, column=5, padx=10)

        tb.Button(
            form,
            text="➕ Agregar",
            bootstyle=PRIMARY,
            command=self.agregar_registro
        ).grid(row=1, column=0, columnspan=6, sticky=E, pady=10)

        # ===== TABLA PROFESIONAL =====
        table_frame = tb.Frame(main)
        table_frame.pack(fill=BOTH, expand=True)

        columns = ("numero", "nombre", "hora", "profesional")

        self.tabla = tb.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            bootstyle="primary"
        )

        self.tabla.heading("numero", text="N°")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("hora", text="Hora")
        self.tabla.heading("profesional", text="Profesional")

        self.tabla.column("numero", width=60, anchor=CENTER)
        self.tabla.column("nombre", width=200)
        self.tabla.column("hora", width=100, anchor=CENTER)
        self.tabla.column("profesional", width=200)

        self.tabla.pack(side=LEFT, fill=BOTH, expand=True)

        scrollbar = tb.Scrollbar(table_frame, orient=VERTICAL, command=self.tabla.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.tabla.configure(yscrollcommand=scrollbar.set)

        # ===== BOTÓN LLAMAR =====
        tb.Button(
            main,
            text="📢 Llamar seleccionado",
            bootstyle=INFO,
            width=25,
            command=self.llamar_seleccionado
        ).pack(anchor=E, pady=10)

    def agregar_registro(self):
        nombre = self.nombre_var.get().strip()
        hora = self.hora_var.get().strip()
        prof = self.pro_var.get().strip()

        if not nombre or not hora or not prof:
            messagebox.showwarning("Validación", "Completa todos los campos")
            return

        numero = f"{self.numero_actual:03}"

        self.tabla.insert(
            "",
            "end",
            values=(numero, nombre, hora, prof),
            tags=("evenrow" if self.numero_actual % 2 == 0 else "oddrow",)
        )

        self.tabla.tag_configure("evenrow", background="#F9FAFB")
        self.tabla.tag_configure("oddrow", background="#EEF2F6")

        self.numero_actual += 1
        self.nombre_var.set("")
        self.hora_var.set("")
        self.pro_var.set("")

    def llamar_seleccionado(self):
        seleccionado = self.tabla.selection()
        if not seleccionado:
            messagebox.showinfo("Atención", "Selecciona una cita")
            return

        item = self.tabla.item(seleccionado)
        numero, nombre, hora, profesional = item["values"]

        self.ventana_llamado.agregar_a_cola(numero, nombre, hora, profesional)
        self.ventana_llamado.guardar_paciente({
            "numero": numero,
            "nombre": nombre,
            "hora": hora,
            "profesional": profesional
        })

        self.tabla.delete(seleccionado)
