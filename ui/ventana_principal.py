import ttkbootstrap as tb
from tkinter import Canvas
import platform
import time

class VentanaLlamado(tb.Toplevel):

    def __init__(self, parent, numero="__", nombre="", hora="", profesional=""):
        super().__init__(parent)

        # Pantalla completa primero
        self.attributes("-fullscreen", True)

        # Intentaremos mover al monitor 2 después de un pequeño retraso
        # (usamos delays mayores para asegurar que el fullscreen ya esté aplicado)
        self.after(500, self.mover_monitor_2)

        # --- COLA INFINITA ---
        self.cola = []

        if numero != "__":
            self.cola.append({
                "numero": numero,
                "nombre": nombre,
                "hora": hora,
                "profesional": profesional
            })

        canvas = Canvas(self, bg="#e6f2fa", highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        self.canvas = canvas

        canvas.create_rectangle(200, 100, 1720, 880, outline="black", width=8)

        canvas.create_text(
            960, 150,
            text="🔊 Llamando",
            font=("Helvetica", 48, "bold"),
            fill="#333333"
        )

        self.numero_main = canvas.create_text(960, 300, text="__", font=("Helvetica", 140, "bold"), fill="#333")
        self.nombre_main = canvas.create_text(960, 450, text="", font=("Helvetica", 60, "bold"), fill="#007BFF")
        self.hora_main   = canvas.create_text(960, 550, text="", font=("Helvetica", 36, "bold"), fill="#333")
        self.pro_main    = canvas.create_text(960, 630, text="", font=("Helvetica", 36, "bold"), fill="#28a745")

        # LISTA DE ESPERA VISUAL
        y_base = 760
        self.siguientes = []

        for i in range(2):
            item = {
                "numero": canvas.create_text(350, y_base + i*80, text="__", font=("Helvetica", 32, "bold"), fill="#444"),
                "nombre": canvas.create_text(650, y_base + i*80, text="", font=("Helvetica", 24), fill="#007BFF"),
                "hora":   canvas.create_text(1000, y_base + i*80, text="", font=("Helvetica", 20), fill="#333"),
                "prof":   canvas.create_text(1350, y_base + i*80, text="", font=("Helvetica", 20), fill="#28a745"),
            }
            self.siguientes.append(item)

        self.actualizar_pantalla()

    def mover_monitor_2(self):
        """
        Intentos prácticos para mover la ventana al monitor secundario.
        1) calcula screenwidth (ancho del monitor principal) y lo usa como X.
        2) si no funciona, prueba offsets comunes (1920, 2560, 3000).
        3) imprime en consola lo que intenta (útil para debug).
        """
        try:
            # info básica
            screen_w = self.winfo_screenwidth()
            screen_h = self.winfo_screenheight()
            print(f"[LLAMADO] winfo_screenwidth={screen_w}, winfo_screenheight={screen_h}, platform={platform.system()}")

            # Lista de candidatos de X donde puede empezar el monitor 2
            candidatos_x = []

            # primer candidato: justo a la derecha del monitor principal
            candidatos_x.append(screen_w)

            # candidatos adicionales comunes (monitores 1080p/1440p/etc)
            candidatos_x.extend([1920, 2560, 3000, 3840])

            # eliminar duplicados y mantener orden
            candidatos_x = list(dict.fromkeys(candidatos_x))

            moved = False
            for x in candidatos_x:
                geom = f"+{x}+0"
                print(f"[LLAMADO] intentando geometry {geom}")
                # aplica geometry y espera un poco para que tenga efecto
                try:
                    self.geometry(geom)
                    # forzamos update y dejamos que el window manager lo procese
                    self.update_idletasks()
                    time.sleep(0.12)
                except Exception as e:
                    print(f"[LLAMADO] error aplicando geometry {geom}: {e}")

                # comprobar dónde quedó la ventana consultando su coordenada actual
                try:
                    # winfo_x/y devuelven la coordenada actual de la ventana
                    cur_x = self.winfo_x()
                    cur_y = self.winfo_y()
                    print(f"[LLAMADO] después de intentar {geom} -> winfo_x={cur_x}, winfo_y={cur_y}")
                    # si cur_x coincide con el x que intentamos (o está cerca), asumimos éxito
                    if abs(cur_x - x) <= 10:
                        print(f"[LLAMADO] ventana movida correctamente a x={cur_x}")
                        moved = True
                        break
                except Exception as e:
                    print(f"[LLAMADO] no pude leer winfo_x/winfo_y: {e}")

            if not moved:
                print("[LLAMADO] No se pudo detectar monitor secundario con los intentos automáticos.")
                print("[LLAMADO] Si tu monitor secundario está a la izquierda, arriba o con coordenadas negativas, dímelo y ajuste la lógica.")
                print("[LLAMADO] También puedes probar a cambiar manualmente uno de los valores en candidatos_x (ej: -1920).")
        except Exception as e:
            print(f"[LLAMADO] mover_monitor_2 fallo: {e}")

    # -------------------------------------------------
    def agregar_a_cola(self, numero, nombre, hora, profesional):
        self.cola.append({
            "numero": numero,
            "nombre": nombre,
            "hora": hora,
            "profesional": profesional
        })
        self.actualizar_pantalla()

    def llamar_siguiente(self):
        if len(self.cola) > 0:
            self.cola.pop(0)
        self.actualizar_pantalla()

    def actualizar_pantalla(self):
        if len(self.cola) > 0:
            p = self.cola[0]
            self.canvas.itemconfig(self.numero_main, text=p["numero"])
            self.canvas.itemconfig(self.nombre_main, text=p["nombre"])
            self.canvas.itemconfig(self.hora_main,   text=f"Asignado: {p['hora']}")
            self.canvas.itemconfig(self.pro_main,    text=f"Profesional: {p['profesional']}")
        else:
            self.canvas.itemconfig(self.numero_main, text="__")
            self.canvas.itemconfig(self.nombre_main, text="")
            self.canvas.itemconfig(self.hora_main,   text="")
            self.canvas.itemconfig(self.pro_main,    text="")

        for i in range(2):
            if len(self.cola) > i+1:
                item = self.cola[i+1]
                self.canvas.itemconfig(self.siguientes[i]["numero"], text=item["numero"])
                self.canvas.itemconfig(self.siguientes[i]["nombre"], text=item["nombre"])
                self.canvas.itemconfig(self.siguientes[i]["hora"],   text=item["hora"])
                self.canvas.itemconfig(self.siguientes[i]["prof"],   text=item["profesional"])
            else:
                self.canvas.itemconfig(self.siguientes[i]["numero"], text="__")
                self.canvas.itemconfig(self.siguientes[i]["nombre"], text="")
                self.canvas.itemconfig(self.siguientes[i]["hora"],   text="")
                self.canvas.itemconfig(self.siguientes[i]["prof"],   text="")

    def actualizar(self, numero, nombre, hora, profesional):
        self.agregar_a_cola(numero, nombre, hora, profesional)
