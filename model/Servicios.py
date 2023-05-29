from datetime import datetime
from config.bd import bd, app, ma

class Servicio(bd.Model):
    __tablename__ = "tblServicio"
    
    Id_Servicio  = bd.Column(bd.Integer, primary_key=True, unique=True, nullable=False)
    Nombre = bd.Column(bd.String(100))
    Tiempo_Servicio = bd.Column(bd.String(25))
    Valor_Servicio = bd.Column(bd.String(25))

    def __init__(self, Nombre, Tiempo_Servicio, Valor_Servicio):
        self.Nombre = Nombre
        self.Tiempo_Servicio =  Tiempo_Servicio
        self.Valor_Servicio = Valor_Servicio

with app.app_context():
    bd.create_all()

class Servicio_Schema(ma.Schema):
    class Meta:
        fields=(
            "Id_Servicio",
            "Nombre",
            "Tiempo_Servicio",
            "Valor_Servicio"
        )