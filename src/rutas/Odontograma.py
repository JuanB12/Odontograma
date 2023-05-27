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

route_odontograma = Blueprint("route_odontograma", __name__)


@route_odontograma.route("/indexOdontograma", methods=["GET"])
def indexOdontograma():
    return render_template("/main/Odontograma.html")
