from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

route_ViewDoctor = Blueprint("routes_ViewDoctor", __name__)

@route_ViewDoctor.route('/IndexViewDoctor', methods=['GET'] )
def homeIndex():
    return render_template('/model/odontogramaview/vistadoctor.html')