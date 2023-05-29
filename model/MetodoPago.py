from datetime import datetime
from config.bd import bd, app, ma


class MetodoPago(bd.Model):
    __tablename__ = "tblMetodoPago"

    Id_Metodo_Pago = bd.Column(bd.Integer, primary_key=True, unique=True, nullable=False)
    Valor = bd.Column(bd.String(25))
    Nombre = bd.Column(bd.String(25))

    def __init__(
        self,
        Id_Servicio_fk,
        Valor,
        Metodo_Pago
        ):
        self.Id_Servicio_fk = Id_Servicio_fk
        self.Valor = Valor
        self.Metodo_Pago = Metodo_Pago


with app.app_context():
    bd.create_all()


class MetodoPago_Schema(ma.Schema):
    class Meta:
        fields = (
            "Id_Facturacion",
            "Id_Servicio_fk",
            "Valor",
            "Metodo_Pago",
        )
