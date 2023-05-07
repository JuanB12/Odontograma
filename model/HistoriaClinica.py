from datetime import datetime
from config.bd import bd, app, ma


class Historia_Clinica(bd.Model):
    __tablename__ = "tblHistoria_Clinica"

    Id_HistoriaClinica = bd.Column(
        bd.Integer, primary_key=True, unique=True, nullable=False
    )
    Id_Paciente_fk = bd.Column(bd.Integer, bd.ForeignKey("tblPacientes.Id_Paciente"))
    Id_Dentista_fk = bd.Column(bd.Integer, bd.ForeignKey("tblDentista.Id_Dentista"))
    Id_Agenda_fk = bd.Column(bd.Integer, bd.ForeignKey("tblAgenda.Id_Agenda"))
    Id_Consultas_fk = bd.Column(bd.Integer, bd.ForeignKey("tblConsultas.Id_Consultas"))
    Diagnostico = bd.Column(bd.String(200), unique=True, nullable=False)

    def __init__(
        self,
        Id_Paciente_fk,
        Id_Dentista_fk,
        Id_Agenda_fk,
        Id_Consultas_fk,
        Diagnostico,
    ):
        self.Id_Paciente_fk = Id_Paciente_fk
        self.Id_Dentista_fk = Id_Dentista_fk
        self.Id_Agenda_fk = Id_Agenda_fk
        self.Id_Consultas_fk = Id_Consultas_fk
        self.Diagnostico = Diagnostico


with app.app_context():
    bd.create_all()


class HistoriaC_Schema(ma.Schema):
    class Meta:
        fields = (
            "Id_HistoriaClinica",
            "Id_Paciente_fk",
            "Id_Dentista_fk",
            "Id_Agenda_fk",
            "Id_Consultas_fk",
            "Diagnostico",
        )
