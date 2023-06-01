from flask import Blueprint, request, jsonify, json
from flask import Flask, redirect, request, jsonify, json, session, render_template
from config.db import bd, app, ma


class Usuario(bd.Model):
    __tablename__ = "tblusuario"

    id_usuario = bd.Column(bd.Integer, primary_key=True)
    id_rol_fk = bd.Column(bd.Integer, bd.ForeignKey("tblroles.id_rol"))
    Nombre = bd.Column(bd.String(50))
    Email = bd.Column(bd.String(50))

    def __init__(self, id_rol_fk,Nombre,Email):
        self.id_rol_fk = id_rol_fk
        self.Nombre = Nombre
        self.Email = Email


with app.app_context():
    bd.create_all()


class Usuario_Schema(ma.Schema):
    class Meta:
        fields = ("id_usuario", "id_rol_fk", "Nombre", "Email")
