from dataclasses import dataclass

@dataclass
class RegistroPaciente:
    numero: str
    nombre: str
    hora: str
    profesional: str