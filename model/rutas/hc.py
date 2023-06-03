from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

route_hc = Blueprint("routes_hc", __name__)

@route_hc.route('/IndexHc', methods=['GET'] )
def hcIndex():
    return render_template('/model/odontogramaview/historialclinico.html')