from datetime import datetime
from config.bd import bd, app, ma


class Facturacion(bd.Model):
    __tablename__ = "tblFacturacion"

    Id_Facturacion = bd.Column(bd.Integer, primary_key=True, unique=True, nullable=False)
    Id_Servicio_fk = bd.Column(bd.Integer, bd.ForeignKey("tblServicio.Id_Servicio"))
    Valor = bd.Column(bd.String(25))
    Metodo_Pago = bd.Column(bd.Integer)

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


class Facturacion_Schema(ma.Schema):
    class Meta:
        fields = (
            "Id_Facturacion",
            "Id_Servicio_fk",
            "Valor",
            "Metodo_Pago",
        )
