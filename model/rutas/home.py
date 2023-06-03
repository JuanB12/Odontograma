from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

route_Home = Blueprint("routes_Home", __name__)

@route_Home.route('/IndexHome', methods=['GET'] )
def homeIndex():
    return render_template('/model/odontogramaview/home.html')