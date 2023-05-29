from config.bd import bd, app, ma

class Dentista(bd.Model):
    __tablename__ = "tblDentista"

    Id_Dentista = bd.Column(bd.Integer, primary_key=True, unique=True, nullable=False)
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
            "Id_Dentista",
            "Especializacion",
            "Hora_Reserva",
        )
