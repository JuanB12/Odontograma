# importamos el paquete de config, porque este tiene la configuración de la BD
from config.db import bd, app, ma


class Paciente(bd.Model):
    __tablename__ = "tblpaciente"

    id_paciente = bd.Column(bd.Integer, primary_key=True)
    id_dentista_fk = bd.Column(bd.Integer, bd.ForeignKey("tbldentista.id_dentista"))
    id_usuario_fk = bd.Column(bd.Integer, bd.ForeignKey("tblusuario.id_usuario"))
    Diente = bd.Column(bd.Integer())
    Tratamiento = bd.Column(bd.String(50))
    
    def __init__(
        self,
        id_paciente_fk,
        id_dentista_fk,
        id_usuario_fk,
        Diente,
        Tratamiento,
    ):
        self.id_dentista_fk = id_dentista_fk
        self.id_usuario_fk = id_usuario_fk
        self.Diente = Diente
        self.Tratamiento = Tratamiento


with app.app_context():
    bd.create_all()


class Paciente_Schema(ma.Schema):
    class Meta:
        fields = (
            "id_paciente",
            "id_dentista_fk",
            "id_usuario_fk",
            "Diente",
            "Tratamiento",
        )
