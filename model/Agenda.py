from datetime import datetime
from config.db import bd, app, ma


class Agenda(bd.Model):
    __tablename__ = "tblagenda"

    id_agenda = bd.Column(bd.Integer, primary_key=True)
    id_paciente_fk = bd.Column(bd.Integer, bd.ForeignKey("tblpaciente.id_paciente"))
    id_dentista_fk = bd.Column(bd.Integer, bd.ForeignKey("tbldentista.id_dentista"))
    id_servicio_fk = bd.Column(bd.Integer, bd.ForeignKey("tblservicio.id_servicio"))
    Hora_Reserva = bd.Column(bd.String(25))
    Fecha_Reserva = bd.Column(bd.String(25))


    def __init__(
        self,
        id_paciente_fk,
        id_dentista_fk,
        id_servicio_fk,
        Hora_Reserva,
        Fecha_Reserva
    ):
        self.id_paciente_fk = id_paciente_fk
        self.id_dentista_fk = id_dentista_fk
        self.id_servicio_fk = id_servicio_fk
        self.Hora_Reserva = Hora_Reserva
        self.Fecha_Reserva = Fecha_Reserva


with app.app_context():
    bd.create_all()


class Agenda_Schema(ma.Schema):
    class Meta:
        fields = (
            "id_agenda",
            "id_paciente_fk",
            "id_dentista_fk",
            "id_servicio_fk",
            "Fecha_Reserva",
            "Hora_Reserva"
        )
