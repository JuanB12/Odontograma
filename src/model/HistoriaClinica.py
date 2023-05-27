from datetime import datetime
from config.bd import bd, app, ma


class Historia_Clinica(bd.Model):
    __tablename__ = "tblHistoria_Clinica"

    Id_HistoriaClinica = bd.Column(
        bd.Integer, primary_key=True, unique=True, nullable=False
    )
    Id_Odontograma_fk = bd.Column(
        bd.Integer, bd.ForeignKey("tblOdontograma.Id_Odontograma")
    )
    Diagnostico = bd.Column(bd.String(200), unique=True, nullable=False)

    def __init__(
        self,
        Id_Odontograma_fk,
        Diagnostico,
    ):
        self.Id_Odontograma_fk = Id_Odontograma_fk
        self.Diagnostico = Diagnostico


with app.app_context():
    bd.create_all()


class HistoriaC_Schema(ma.Schema):
    class Meta:
        fields = (
            "Id_HistoriaClinica",
            "Id_Odontograma_fk",
            "Diagnostico",
        )
