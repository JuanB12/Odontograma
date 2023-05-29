from config.bd import bd, app, ma

class Roles(bd.Model):
    __tablename__ = "tblRoles"
    Id_Rol = bd.Column(bd.Integer, primary_key=True, unique=True, nullable=False)
    Nombre = bd.Column(bd.String(25))

    def __init__(self, Nombre):
        self.Nombre= Nombre

with app.app_context():
    bd.create_all()

class Roles_Schema(ma.Schema):
    class Meta:
        fields = (
            "Id_Rol",
            "Nombre",
        )