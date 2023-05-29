from flask import Flask, request, session, json, jsonify, render_template, redirect

from config.bd import bd, ma, app

# ------------------------------------------------------------------------------
from model.Servicios import Servicio, Servicio_Schema
from model.Roles import Roles, Roles_Schema
from model.HistoriaClinica import Historia_Clinica, HistoriaC_Schema
from model.MetodoPago import MetodoPago, MetodoPago_Schema
# ------------------------------------------------------------------------------
from model.Agenda import Agenda, Agenda_Schema
from model.Usuario import Usuario, UsuarioSchema
from model.Pacientes import Paciente, Paciente_Schema
from model.Dentista import Dentista, Dentista_Schema
from model.Odontograma import Odontograma, Odontograma_Schema
from model.Facturacion import Facturacion, Facturacion_Schema

# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------



@app.route("/", methods=["GET"])
def index():
    return "Hola mundo!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
