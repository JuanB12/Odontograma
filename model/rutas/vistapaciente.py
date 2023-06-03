from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

route_ViewPaciente = Blueprint("routes_ViewPaciente", __name__)

@route_ViewPaciente.route('/IndexViewPaciente', methods=['GET'] )
def homeIndex():
    return render_template('/model/odontogramaview/vistapaciente.html')