from datetime import datetime
from config.bd import bd, app, ma


class Odontograma(bd.Model):
    __tablename__ = "tblOdontograma"

    Id_Odontograma = bd.Column(bd.Integer, primary_key=True, unique=True, nullable=False)
    Id_Agenda_fk = bd.Column(bd.Integer, bd.ForeignKey("tblAgenda.Id_Agenda"))
    Id_Paciente_fk = bd.Column(bd.Integer, bd.ForeignKey("tblPaciente.Id_Paciente"))
    Id_Dentista_fk = bd.Column(bd.Integer, bd.ForeignKey("tblDentista.Id_Dentista"))
    Id_Servicio_fk = bd.Column(bd.Integer, bd.ForeignKey("tblServicio.Id_Servicio"))
    fecha_inicio = bd.Column(bd.String(100))
    fecha_fin = bd.Column(bd.String(100))

    def __init__(
        self,Id_Agenda_fk,Id_Paciente_fk,Id_Dentista_fk,Id_Servicio_fk,fecha_inicio,fecha_fin
    ):
        self.Id_Agenda_fk = Id_Agenda_fk
        self.Id_Paciente_fk = Id_Paciente_fk
        self.Id_Dentista_fk = Id_Dentista_fk
        self.Id_Servicio_fk = Id_Servicio_fk
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin


with app.app_context():
    bd.create_all()


# Capturara todos los campos que quiero mostrarle al Usuario
class Odontograma_Schema(ma.Schema):
    class Meta:
        fields = (
            "Id_Odontograma",
            "Id_Paciente_fk",
            "Id_Dentista_fk",
            # "Id_Facturacion_fk",
            "Fecha_Consulta",
            "Antecedes_Medicos",
            "Medicamentos",
            "Diagnostico",
            "Tratamiento",
            "Pruebas",
            "Observaciones",
            "Resultados",
        )
