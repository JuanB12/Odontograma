from flask import Blueprint, request, jsonify, json
from config.bd import db, app, ma
from flask import Flask, redirect, request, jsonify, json, session, render_template


class Registro(db.Model):
    __tablename__ = "tblregistro"

    id = db.Column(db.Integer, primary_key=True)
    NombreCompleto = db.Column(db.String(50))
    CorreoElectronico = db.Column(db.String(50))
    Contrasena = db.Column(db.String(50))

    def __init__(self, NombreCompleto, CorreoElectronico, Contrasena):
        self.NombreCompleto = NombreCompleto
        self.CorreoElectronico = CorreoElectronico
        self.Contrasena = Contrasena


with app.app_context():
    db.create_all()


class RegistroSchema(ma.Schema):
    class Meta:
        fields = ("id", "NombreCompleto", "CorreoElectronico", "Contrasena")
