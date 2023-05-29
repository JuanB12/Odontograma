from flask import Blueprint, request, jsonify, json
from config.bd import bd, app, ma
from flask import Flask, redirect, request, jsonify, json, session, render_template


class Usuario(bd.Model):
    __tablename__ = "tblUsuario"

    Id_Usuario = bd.Column(bd.Integer, primary_key=True)
    Id_Rol_fk = bd.Column(bd.Integer, bd.ForeignKey("tblRoles.Id_Rol"))
    Nombre = bd.Column(bd.String(50))
    Email = bd.Column(bd.String(50))

    def __init__(self, Id_Rol_fk,Nombre,Email):
        self.Id_Rol_fk = Id_Rol_fk
        self.Nombre = Nombre
        self.Email = Email


with app.app_context():
    bd.create_all()


class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ("Id_Usuario", "Id_Rol_fk", "Nombre", "Email")
