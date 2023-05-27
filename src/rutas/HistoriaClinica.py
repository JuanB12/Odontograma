from config.bd import db, app, ma
from flask import (
    Blueprint,
    Flask,
    redirect,
    request,
    jsonify,
    json,
    session,
    render_template,
)
from model.Registro import Registro

route_RegistroHistorial = Blueprint("route_RegistroHistorial", __name__)


@route_RegistroHistorial.route("/IndexHistorial", methods=["GET"])
def IndexHistorial():
    return render_template("/main/HistorialRegistro.html")


@route_RegistroHistorial.route("/VerRegistro", methods=["GET"])
def VerRegistro():
    ArregloUsuario = {}
    result = db.session.query(Registro).select_from(Registro).all()
    Usuario = 0
    Array = []
    for atributo in result:
        Usuario = Usuario + 1
        ArregloUsuario[Usuario] = {
            "id": atributo.id,
            "NombreCompleto": atributo.NombreCompleto,
            "CorreoElectronico": atributo.CorreoElectronico,
            "Contrasena": atributo.Contrasena,
        }
        Array.append(ArregloUsuario)
    return jsonify(ArregloUsuario)
