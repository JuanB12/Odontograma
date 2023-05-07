from flask import Flask, request, session, json, jsonify, render_template, redirect

from config.bd import bd, ma, app
from model.Agenda import Agenda, Agenda_Schema
from model.Consultas import Consultas, Consultas_Schema
from model.Dentista import Dentista, Dentista_Schema
from model.Dientes import Dientes, Dientes_Schema
from model.Facturacion import Facturacion, Facturacion_Schema
from model.HistoriaClinica import Historia_Clinica, HistoriaC_Schema
from model.Pacientes import Pacientes, Pacientes_Schema

agenda_schema = Agenda_Schema()
agendas_schema = Agenda_Schema(many=True)
consulta_schema = Consultas_Schema()
consultas_schema = Consultas_Schema(many=True)
dentista_schema = Dentista_Schema()
dentistas_schema = Dentista_Schema(many=True)
diente_schema = Dientes_Schema()
dientes_Schema = Dientes_Schema(many=True)
facturacion_schema = Facturacion_Schema()
facturaciones_schema = Facturacion_Schema(many=True)
hc_schema = HistoriaC_Schema()
hcs_schema = HistoriaC_Schema(many=True)
paciente_schema = Pacientes_Schema()
pacientes_schema = Pacientes_Schema(many=True)


@app.route("/", methods=["GET"])
def index():
    return "Hola mundo!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
