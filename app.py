from flask import Flask, request, session, json, jsonify, render_template, redirect

from config.db import bd, ma, app

# ------------------------------------------------------------------------------
from model.MetodoPago import MetodoPago, MetodoPago_Schema
from model.Roles import Roles, Roles_Schema
from model.Servicios import Servicio, Servicio_Schema

# ------------------------------------------------------------------------------
from model.Facturacion import Facturacion, Facturacion_Schema
from model.Agenda import Agenda, Agenda_Schema
from model.Usuario import Usuario, Usuario_Schema
from model.Dentista import Dentista, Dentista_Schema
from model.Pacientes import Paciente, Paciente_Schema
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

# --------------------------- Roles ------------------------------------------
@app.route("/", methods=["GET"])
def index():
    resultRoles = Roles.query.all()
    resultado = roles_schema.dump(resultRoles)
    return jsonify(resultado)

@app.route("/principal", methods=["GET"])
def princiapal():
   
    return render_template('odontogramaview/home.html')

# save roles
@app.route("/saveroles", methods=["POST"])
def saveRol():
    nombre = request.json['Nombre']
    newRol = Roles(nombre)
    bd.session.add(newRol)
    bd.session.commit()
    return "Guardado con exito"

# delete roles
@app.route("/eliminar", methods=["POST"])
def deleteRol():
    id_r = request.json['id_rol']
    nombre = Roles.query.get(id_r)
    bd.session.delete(nombre)
    bd.session.commit()
    return jsonify(rol_schema.dump(nombre))


# update roles
@app.route("/update", methods=["POST"])
def updateRol():
    id_r = request.json['id_rol']
    nombre = request.json['Nombre']
    rol = Roles.query.get(id_r)
    # rol = Roles.query.get(nombre)
    rol.id_rol = id_r
    rol.Nombre = nombre
    bd.session.commit()
    return "Update exitoso"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
