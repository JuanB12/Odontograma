from datetime import datetime
from config.db import bd, app, ma


class Historia_Clinica(bd.Model):
    __tablename__ = "tblhistoriaclinica"

    id_historiaclinica = bd.Column(bd.Integer, primary_key=True)
    id_odontograma_fk = bd.Column(bd.Integer, bd.ForeignKey("tblodontograma.id_odontograma"))
    id_paciente_fk = bd.Column(bd.Integer, bd.ForeignKey("tblpaciente.id_paciente"))

    def __init__(
        self,
        id_odontograma_fk,
        id_paciente_fk,
    ):
        self.id_odontograma_fk = id_odontograma_fk
        self.id_paciente_fk = id_paciente_fk


with app.app_context():
    bd.create_all()


class HistoriaC_Schema(ma.Schema):
    class Meta:
        fields = (
            "id_historiaclinica",
            "id_odontograma_fk",
            "id_paciente_fk",
        )
