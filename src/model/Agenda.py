from datetime import datetime
from config.bd import bd, app, ma


class Agenda(bd.Model):
    __tablename__ = "tblAgenda"

    Id_Agenda = bd.Column(bd.Integer, primary_key=True, unique=True, nullable=False)
    Id_Dentista_fk = bd.Column(bd.Integer, bd.ForeignKey("tblDentista.Id_Dentista"))
    Fecha_Reserva = bd.Column(bd.DateTime)
    Datos_Personales = bd.Column(bd.String(200), unique=True, nullable=False)
    Servicio = bd.Column(bd.String(100))
    Especialista = bd.Column(bd.String(70))
    Jornada = bd.Column(bd.String(20))

    def __init__(
        self,
        Id_Dentista_fk,
        Fecha_Reserva,
        Datos_Personales,
        Servicio,
        Especialista,
        Jornada,
    ):
        self.Id_Dentista_fk = Id_Dentista_fk
        self.Fecha_Reserva = Fecha_Reserva
        self.Datos_Personales = Datos_Personales
        self.Servicio = Servicio
        self.Especialista = Especialista
        self.Jornada = Jornada


with app.app_context():
    bd.create_all()


class Agenda_Schema(ma.Schema):
    class Meta:
        fields = (
            "Id_Agenda",
            "Id_Dentista_fk",
            "Fecha_Reserva",
            "Datos_Personales",
            "Servicio",
            "Especialista",
            "Jornada",
        )
