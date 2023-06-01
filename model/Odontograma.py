from datetime import datetime
from config.db import bd, app, ma


class Odontograma(bd.Model):
    __tablename__ = "tblodontograma"

    id_odontograma = bd.Column(bd.Integer, primary_key=True)
    id_agenda_fk = bd.Column(bd.Integer, bd.ForeignKey("tblagenda.id_agenda"))
    id_paciente_fk = bd.Column(bd.Integer, bd.ForeignKey("tblpaciente.id_paciente"))
    id_dentista_fk = bd.Column(bd.Integer, bd.ForeignKey("tbldentista.id_dentista"))
    id_servicio_fk = bd.Column(bd.Integer, bd.ForeignKey("tblservicio.id_servicio"))
    fecha_inicio = bd.Column(bd.String(100))
    fecha_fin = bd.Column(bd.String(100))

    def __init__(
        self,id_agenda_fk,id_paciente_fk,id_dentista_fk,id_servicio_fk,fecha_inicio,fecha_fin
    ):
        self.id_agenda_fk = id_agenda_fk
        self.id_paciente_fk = id_paciente_fk
        self.id_dentista_fk = id_dentista_fk
        self.id_servicio_fk = id_servicio_fk
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin


with app.app_context():
    bd.create_all()


# Capturara todos los campos que quiero mostrarle al Usuario
class Odontograma_Schema(ma.Schema):
    class Meta:
        fields = (
            "id_odontograma",
            "id_agenda_fk",
            "id_paciente_fk",
            "id_dentista_fk",
            "id_servicio_fk",
            "fecha_inicio",
            "fecha_fin"
        )
