from datetime import datetime
from config.bd import bd, app, ma


class Dentista(bd.Model):
    __tablename__ = "tblDentista"

    Id_Dentista = bd.Column(bd.Integer, primary_key=True, unique=True, nullable=False)
    Id_Paciente_fk = bd.Column(bd.Integer, bd.ForeignKey("tblPacientes.Id_Paciente"))
    Id_Agenda_fk = bd.Column(bd.Integer, bd.ForeignKey("tblAgenda.Id_Agenda"))
    Nombre = bd.Column(bd.String(50), unique=True)
    Edad = bd.Column(bd.Integer(5))
    Telefono = bd.Column(bd.String(20))
    # nos interesa el horario de atención de la cita en el momento de ahora.
    Horario_Atencion = bd.Column(bd.DateTime, default=datetime.datetime.now)
    Jornada_Laboral = bd.Column(bd.String(20))

    def __init__(
        self,
        Id_Paciente_fk,
        Id_Agenda_fk,
        Nombre,
        Edad,
        Telefono,
        Horario_Atencion,
        Jornada_Laboral,
    ):
        self.Id_Paciente_fk = Id_Paciente_fk
        self.Id_Agenda_fk = Id_Agenda_fk
        self.Nombre = Nombre
        self.Edad = Edad
        self.Telefono = Telefono
        self.Horario_Atencion = Horario_Atencion
        self.Jornada_Laboral = Jornada_Laboral


with app.app_context():
    bd.create_all()


class Dentista_Schema(ma.Schema):
    class Meta:
        fields = (
            "Id_Dentista",
            "Id_Paciente_fk",
            "Id_Agenda_fk",
            "Nombre",
            "Edad",
            "Telefono",
            "Horario_Atencion",
            "Jornada_Laboral",
        )
