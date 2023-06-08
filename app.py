from flask import Flask, request, session, json, jsonify, render_template, redirect

from config.db import bd, ma, app

from model.MetodoPago import MetodoPago, MetodoPago_Schema
from model.Roles import Roles, Roles_Schema
from model.Servicios import Servicio, Servicio_Schema

# ------------------------------------------------------------------------------
from model.Dentista import Dentista, Dentista_Schema
from model.Usuario import Usuario, Usuario_Schema
from model.Pacientes import Paciente, Paciente_Schema
from model.Agenda import Agenda, Agenda_Schema
from model.Facturacion import Facturacion, Facturacion_Schema
from model.Odontograma import Odontograma, Odontograma_Schema
from model.HistoriaClinica import Historia_Clinica, HistoriaC_Schema
# ------------------------------------------------------------------------------

metodo_pago = MetodoPago_Schema()
metodos_pago = MetodoPago_Schema(many=True)
rol_schema = Roles_Schema()
roles_schema = Roles_Schema(many=True)
servicio_schema = Servicio_Schema()
servicios_schema = Servicio_Schema(many=True)
# ------------------------------------------------------------------------------
facturacion_schema = Facturacion_Schema()
facturacion_schemas = Facturacion_Schema(many=True)
agenda_schema = Agenda_Schema()
agendas_schema = Agenda_Schema(many=True)
usuario_schema = Usuario_Schema()
usuarios_schema = Usuario_Schema(many=True)
dentista_schema = Dentista_Schema()
dentistas_schema = Dentista_Schema(many=True)
paciente_shcema = Paciente_Schema()
pacientes_schema = Paciente_Schema(many=True)
odontograma_schema = Odontograma_Schema()
odontogramas_schema = Odontograma_Schema(many=True)
historia_schema = HistoriaC_Schema()
historias_schema = HistoriaC_Schema(many=True)



@app.route("/", methods=['GET'])
def index():
    return render_template('home.html')

@app.route("/reservar", methods=['GET'])
def reservar():
    return render_template('reserva.html')

@app.route("/reservarCita", methods=['GET'])
def reservarCita():
    return render_template('home.html')

@app.route("/registro", methods=['GET'])
def registro():
    return render_template('registro.html')

@app.route("/ingresar", methods=["GET"])
def ingresar():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

