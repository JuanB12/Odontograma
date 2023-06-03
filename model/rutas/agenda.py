from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

route_Agenda = Blueprint("routes_Agenda", __name__)

@route_Agenda.route('/IndexCita', methods=['GET'] )
def agendaIndex():
    return render_template('/model/odontogramaview/agenda.html')