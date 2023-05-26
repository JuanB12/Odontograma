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

route_Dentistas = Blueprint("route_Dentistas", __name__)


@route_Dentistas.route("/IndexDentistas", methods=["GET"])
def IndexDentistas():
    return render_template("/main/Dentistas.html")
