# importamos el paquete de config, porque este tiene la configuración de la BD
from config.bd import bd, app, ma


# Model sera esa transacción de la BD, es decir, guardar, eliminar, modificar, etc
class Pacientes(bd.Model):
    # Nombre de la base de datos
    __tablename__ = "tblPacientes"

    # Declaración de atributos
    Id_Paciente = bd.Column(bd.Integer, primary_key=True, unique=True, nullable=False)
    # unique = variable unica
    Nombre = bd.Column(bd.String(50), unique=True, nullable=False)
    Correo = bd.Column(bd.String(50), unique=True, nullable=False)
    Telefono = bd.Column(bd.String(50))
    Edad = bd.Column(bd.Integer())
    Tipo_Documento = bd.Column(bd.String(50), unique=True, nullable=False)
    Historial_Procedimiento = bd.Column(bd.String(100))

    # Creamos el constructor
    def __init__(
        self,
        Id_Dentista_FK,
        Nombre,
        Correo,
        Telefono,
        Edad,
        Tipo_Documento,
        Historial_Procedimiento,
    ):
        self.Id_Dentista_FK = Id_Dentista_FK
        self.Nombre = Nombre
        self.Correo = Correo
        self.Telefono = Telefono
        self.Edad = Edad
        self.Tipo_Documento = Tipo_Documento
        self.Historial_Procedimiento = Historial_Procedimiento


# generamos una envoltura
with app.app_context():
    # cuando se invoque o corra, se creara la tabla
    bd.create_all()


# Capturara todos los campos que quiero mostrarle al Usuario
class Pacientes_Schema(ma.Schema):
    class Meta:
        fields = (
            "Id_Paciente",
            "Id_Dentista_FK",
            "Nombre",
            "Correo",
            "Telefono",
            "Edad",
            "Tipo_Documento",
            "Historial_Procedimiento",
        )
