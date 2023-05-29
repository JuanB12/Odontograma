# importamos el paquete de config, porque este tiene la configuración de la BD
from config.bd import bd, app, ma


class Paciente(bd.Model):
    __tablename__ = "tblPaciente"

    Id_Paciente = bd.Column(bd.Integer, primary_key=True, unique=True, nullable=False)
    Id_Dentista_fk = bd.Column(bd.Integer, bd.ForeignKey("tblDentista.Id_Dentista"))
    Id_Usuario_fk = bd.Column(bd.Integer, bd.ForeignKey("tblUsuario.Id_Usuario"))
    Diente = bd.Column(bd.Integer())
    Tratamiento = bd.Column(bd.String(50))
    
    def __init__(
        self,
        Id_Dentista_FK,
        Diente,
        Tratamiento,
        
    ):
        self.Id_Dentista_FK = Id_Dentista_FK
        self.Diente = Diente
        self.Tratamiento = Tratamiento


with app.app_context():
    bd.create_all()


class Paciente_Schema(ma.Schema):
    class Meta:
        fields = (
            "Id_Paciente",
            "Id_Dentista_FK",
            "Diente",
            "Tratamiento",
        )
