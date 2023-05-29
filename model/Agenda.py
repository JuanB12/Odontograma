from datetime import datetime
from config.bd import bd, app, ma


class Agenda(bd.Model):
    __tablename__ = "tblAgenda"

    Id_Agenda = bd.Column(bd.Integer, primary_key=True, unique=True, nullable=False)
    Id_Paciente_fk = bd.Column(bd.Integer, bd.ForeignKey("tblPacientes.Id_Paciente"))
    Id_Dentista_fk = bd.Column(bd.Integer, bd.ForeignKey("tblDentista.Id_Dentista"))
    Id_Servicio_fk = bd.Column(bd.Integer, bd.ForeignKey("tblServicio.Id_Servicio"))
    Hora_Reserva = bd.Column(bd.String(25))
    Fecha_Reserva = bd.Column(bd.String(25))
    

    def __init__(
        self,
        Id_Paciente_fk,
        Id_Dentista_fk,
        Id_Servicio_fk,
        Hora_Reserva,
        Fecha_Reserva
    ):
        self.Id_Paciente_fk = Id_Paciente_fk
        self.Id_Dentista_fk = Id_Dentista_fk
        self.Id_Servicio_fk = Id_Servicio_fk
        self.Fecha_Reserva = Fecha_Reserva
        self.Hora_Reserva = Hora_Reserva


with app.app_context():
    bd.create_all()


class Agenda_Schema(ma.Schema):
    class Meta:
        fields = (
            "Id_Agenda",
            "Id_Paciente_fk",
            "Id_Dentista_fk",
            "Id_Servicio_fk",
            "Hora_Reserva",
            "Fecha_Reserva"
        )
