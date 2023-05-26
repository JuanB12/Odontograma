from datetime import datetime
from config.bd import bd, app, ma


class Dientes(bd.Model):
    __tablename__ = "tblDientes"

    Id_Diente = bd.Column(bd.Integer, primary_key=True, unique=True, nullable=False)
    Id_Pacientes_fk = bd.Column(bd.Integer, bd.ForeignKey("tblPacientes.Id_Paciente"))
    Tipo_Diente = bd.Column(bd.String(60), unique=True, nullable=False)
    Historial = bd.Column(bd.String(100))
    Nombre_Diente = bd.Column(bd.String(50), unique=True)
    Estado_Diente = bd.Column(bd.String(50), unique=True)
    Procedimiento_Realizado = bd.Column(bd.String(150))

    def __init__(
        self,
        Id_Agenda_fk,
        Tipo_Diente,
        Historial,
        Nombre_Diente,
        Estado_Diente,
        Procedimiento_Realizado,
    ):
        self.Id_Agenda_fk = Id_Agenda_fk
        self.Tipo_Diente = Tipo_Diente
        self.Historial = Historial
        self.Nombre_Diente = Nombre_Diente
        self.Estado_Diente = Estado_Diente
        self.Procedimiento_Realizado = Procedimiento_Realizado


with app.app_context():
    bd.create_all()


class Dientes_Schema(ma.Schema):
    class Meta:
        fields = (
            "Id_Diente",
            "Id_Agenda_fk",
            "Tipo_Diente",
            "Historial",
            "Nombre_Diente",
            "Estado_Diente",
            "Procedimiento_Realizado",
        )
