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

route_dientes = Blueprint("route_Dientes", __name__)


@route_dientes.route("/IndexDientes", methods=["GET"])
def IndexDientes():
    return render_template("main/Dientes.html")
