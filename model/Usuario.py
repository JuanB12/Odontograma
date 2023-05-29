from flask import Blueprint, request, jsonify, json
from config.bd import db, app, ma
from flask import Flask, redirect, request, jsonify, json, session, render_template


class Usuario(db.Model):
    __tablename__ = "tblUsuario"

    Id_Usuario = db.Column(db.Integer, primary_key=True)
    Id_Rol_fk = db.Column(db.Integer, db.ForeignKey("tblRoles.Id_Rol"))
    Nombre = db.Column(db.String(50))
    Email = db.Column(db.String(50))

    def __init__(self, Id_Rol_fk,Nombre,Email):
        self.Id_Rol_fk = Id_Rol_fk
        self.Nombre = Nombre
        self.Email = Email


with app.app_context():
    db.create_all()


class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ("Id_Usuario", "Id_Rol_fk", "Nombre", "Email")
