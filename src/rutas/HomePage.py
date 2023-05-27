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

route_HomePage = Blueprint("route_HomePage", __name__)


@route_HomePage.route("/IndexHomePage", methods=["GET"])
def IndexFacturacion():
    return render_template("/main/HomePage.html")
