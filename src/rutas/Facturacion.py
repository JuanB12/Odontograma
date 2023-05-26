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

route_facturacion = Blueprint("route_facturacion", __name__)


@route_facturacion.route("/IndexFacturacion", methods=["GET"])
def IndexFacturacion():
    return render_template("/main/Facturacion.html")
