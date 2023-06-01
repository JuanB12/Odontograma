from config.db import bd, app, ma

class Roles(bd.Model):
    __tablename__ = "tblroles"
    
    id_rol = bd.Column(bd.Integer, primary_key=True)
    Nombre = bd.Column(bd.String(25))

    def __init__(self, Nombre):
        self.Nombre= Nombre

with app.app_context():
    bd.create_all()

class Roles_Schema(ma.Schema):
    class Meta:
        fields = (
            "id_rol",
            "Nombre",
        )