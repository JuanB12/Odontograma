from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

route_Registro = Blueprint("routes_Registro", __name__)

@route_Registro.route('/IndexRegistro', methods=['GET'] )
def homeIndex():
    return render_template('/model/odontogramaview/registro.html')