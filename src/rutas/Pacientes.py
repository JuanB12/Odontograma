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

route_Paciente = Blueprint("route_Paciente", __name__)


@route_Paciente.route("/indexPaciente", methods=["GET"])
def indexPaciente():
    return render_template("/main/Pacientes.html")
