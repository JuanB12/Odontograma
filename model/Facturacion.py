from datetime import datetime
from config.bd import bd, app, ma


class Facturacion(bd.Model):
    __tablename__ = "tblFacturacion"

    Id_Facturacion = bd.Column(
        bd.Integer, primary_key=True, unique=True, nullable=False
    )
    Id_HistoriaClinica_fk = bd.Column(
        bd.Integer, bd.ForeignKey("tblHistoria_Clinica.Id_HistoriaClinica")
    )
    Id_Paciente_fk = bd.Column(bd.Integer, bd.ForeignKey("tblPacientes.Id_Paciente"))
    Fecha_Radicacion = bd.Column(bd.DateTime)
    Fecha_Vencimiento = bd.Column(bd.DateTime)
    Monto_Total = bd.Column(bd.Double)
    Procedimiento_Realizado = bd.Column(bd.String(150))
    Metodo_Pago = bd.Column(bd.String(50))

    def __init__(
        self,
        Id_HistoriaClinica_fk,
        Id_Paciente_fk,
        Fecha_Radicacion,
        Fecha_Vencimiento,
        Monto_Total,
        Procedimiento_Realizado,
        Metodo_Pago,
    ):
        self.Id_HistoriaClinica_fk = Id_HistoriaClinica_fk
        self.Id_Paciente_fk = Id_Paciente_fk
        self.Fecha_Radicacion = Fecha_Radicacion
        self.Fecha_Vencimiento = Fecha_Vencimiento
        self.Monto_Total = Monto_Total
        self.Procedimiento_Realizado = Procedimiento_Realizado
        self.Metodo_Pago = Metodo_Pago


with app.app_context():
    bd.create_all()


class Facturacion_Schema(ma.Schema):
    class Meta:
        fields = (
            "Id_Facturacion",
            "Id_HistoriaClinica_fk",
            "Id_Paciente_fk",
            "Fecha_Radicacion",
            "Fecha_Vencimiento",
            "Monto_Total",
            "Procedimiento_Realizado",
            "Metodo_Pago",
        )
