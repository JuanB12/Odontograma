from datetime import datetime
from config.db import bd, app, ma

class Servicio(bd.Model):
    __tablename__ = "tblservicio"
    
    id_servicio  = bd.Column(bd.Integer, primary_key=True)
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
            "id_servicio",
            "Nombre",
            "Tiempo_Servicio",
            "Valor_Servicio"
        )