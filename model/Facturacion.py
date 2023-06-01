from datetime import datetime
from config.db import bd, app, ma


class Facturacion(bd.Model):
    __tablename__ = "tblfacturacion"

    id_facturacion = bd.Column(bd.Integer, primary_key=True)
    id_servicio_fk = bd.Column(bd.Integer, bd.ForeignKey("tblservicio.id_servicio"))
    id_metodo_fk = bd.Column(bd.Integer, bd.ForeignKey("tblmetodopago.id_metodopago"))
    Valor = bd.Column(bd.String(25))
    
    def __init__(
        self,
        id_servicio_fk,
        id_metodo_fk,
        Valor,
        ):
        self.Id_Servicio_fk = id_servicio_fk
        self.id_metodo_fk = id_metodo_fk
        self.Valor = Valor


with app.app_context():
    bd.create_all()


class Facturacion_Schema(ma.Schema):
    class Meta:
        fields = (
            "id_facturacion",
            "id_servicio_fk",
            "id_metodo_fk",
            "Valor",
        )
