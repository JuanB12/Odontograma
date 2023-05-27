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

route_Agenda = Blueprint("route_Agenda", __name__)


@route_Agenda.route("/Agenda", methods=["GET"])
def IndexFacturacion():
    return render_template("/main/Agenda.html")
