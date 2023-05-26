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
    url_for,
    flash,
    sessions,
)
from model.Registro import Registro
import email
from datetime import datetime, timezone

route_login = Blueprint("route_login", __name__)


@route_login.route("/indexLogin", methods=["GET"])
def indexLogin():
    return render_template("/main/Login.html")


# guardado de usuario
@route_login.route("/guardarUsuario", methods=["POST"])
def guardarUsuario():
    fullname = request.form["fullname"]
    fullemail = request.form["fullemail"]
    password = request.form["password"]
    print(fullname, fullemail, password)
    nuevoUsuario = Registro(fullname, fullemail, password)
    db.session.add(nuevoUsuario)
    db.session.commit()
    rpta = {"fullname": fullname, "fullemail": fullemail, "password": password}
    estado = 200
    cabecera = {}
    return jsonify(rpta), estado, cabecera


# login
@route_login.route("/login", methods=["POST"])
def login():
    fullemail = request.form["fullemail"]
    password = request.form["password"]
    # verificacion de que el usuario y contraseña sean validos en la base de datos
    usuario = Registro.query.filter_by(
        CorreoElectronico=fullemail, Contrasena=password
    ).first()

    # validcion de credenciales
    if usuario:
        session["user_id"] = usuario.id
        message = {"message": "inicio de sesión valido"}
        estado = 200
    else:
        message = {"message": "inicio de sesión denegado"}
        estado = 401

    cabecera = {"Content-Type': 'application/json"}
    return jsonify(message), estado, cabecera


# verificacion de correos
@route_login.route("/verificarCorreo", methods=["POST"])
def verificarCorreo():
    fullemail = request.json["fullemail"]
    user_1 = Registro.query.filter_by(CorreoElectronico=fullemail).first()
    if user_1:
        session["user_id"] = user_1.id
        message = {"message": "Correo Electronico encontrado en la base de datos"}
        estado = 200
    else:
        message = {"message": "Correo electrónico no encontrado en la base de datos"}
        estado = 401
    cabecera = {"Content-Type": "application/json"}
    return jsonify(message), estado, cabecera


# clave olvidada - HACER UN METODO PARA RESETEAR CONTRASEÑA
# @route_login.route("/verificarClave", methods=["POST"])
# def verificarClave():
