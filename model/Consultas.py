from datetime import datetime
from config.bd import bd, app, ma


class Consultas(bd.Model):
    __tablename__ = "tblConsultas"

    Id_Consultas = bd.Column(bd.Integer, primary_key=True, unique=True, nullable=False)
    Id_Paciente_fk = bd.Column(bd.Integer, bd.ForeignKey("tblPacientes.Id_Paciente"))
    Fecha_Consulta = bd.Column(bd.DateTime)
    Antecedes_Medicos = bd.Column(bd.String(200))
    Medicamentos = bd.Column(bd.String(100))
    Diagnostico = bd.Column(bd.String(100))
    Tratamiento = bd.Column(bd.String(100))
    Pruebas = bd.Column(bd.String(100))
    Observaciones = bd.Column(bd.String(100))
    Resultados = bd.Column(bd.String(100))

    def __init__(
        self,
        Id_Paciente_fk,
        Fecha_Consulta,
        Antecedentes_Medicos,
        Medicamentos,
        Diagnostico,
        Tratamiento,
        Pruebas,
        Observaciones,
        Resultados,
    ):
        self.Id_Paciente_fk = Id_Paciente_fk
        self.Fecha_Consulta = Fecha_Consulta
        self.Antecedes_Medicos = Antecedentes_Medicos
        self.Medicamentos = Medicamentos
        self.Diagnostico = Diagnostico
        self.Tratamiento = Tratamiento
        self.Pruebas = Pruebas
        self.Observaciones = Observaciones
        self.Resultados = Resultados


with app.app_context():
    bd.create_all()


# Capturara todos los campos que quiero mostrarle al Usuario
class Consultas_Schema(ma.Schema):
    class Meta:
        fields = (
            "Id_Consultas",
            "Id_Paciente_fk",
            "Fecha_Consulta",
            "Antecedes_Medicos",
            "Medicamentos",
            "Diagnostico",
            "Tratamiento",
            "Pruebas",
            "Observaciones",
            "Resultados",
        )
