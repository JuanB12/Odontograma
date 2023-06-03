from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

route_Reserva = Blueprint("routes_Reserva", __name__)

@route_Reserva.route('/IndexReserva', methods=['GET'] )
def homeIndex():
    return render_template('/model/odontogramaview/reserva.html')