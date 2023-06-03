from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

route_dentista = Blueprint("routes_Dentista", __name__)

@route_dentista.route('/IndexAgenda', methods=['GET'] )
def dentistaIndex():
    return render_template('/model/odontogramaview/vistadoctor.html')