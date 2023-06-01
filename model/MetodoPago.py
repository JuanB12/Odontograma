from datetime import datetime
from config.db import bd, app, ma


class MetodoPago(bd.Model):
    __tablename__ = "tblmetodopago"

    id_metodopago = bd.Column(bd.Integer, primary_key=True)
    Valor = bd.Column(bd.String(25))
    Nombre = bd.Column(bd.String(25))

    def __init__(
        self,
        Valor,
        Metodo_Pago
        ):
        self.Valor = Valor
        self.Metodo_Pago = Metodo_Pago


with app.app_context():
    bd.create_all()


class MetodoPago_Schema(ma.Schema):
    class Meta:
        fields = (
            "id_metodopago",
            "Valor",
            "Metodo_Pago",
        )
