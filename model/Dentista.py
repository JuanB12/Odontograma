from config.db import bd, app, ma

class Dentista(bd.Model):
    __tablename__ = "tbldentista"

    id_dentista = bd.Column(bd.Integer, primary_key=True)
    Especializacion = bd.Column(bd.String(50))
    Hora_Reserva = bd.Column(bd.String(25))

    def __init__(self, Especializacion, Hora_Reserva):
        self.Especializacion = Especializacion
        self.Hora_Reserva = Hora_Reserva

with app.app_context():
    bd.create_all()

class Dentista_Schema(ma.Schema):
    class Meta:
        fields = (
            "id_dentista",
            "Especializacion",
            "Hora_Reserva",
        )
