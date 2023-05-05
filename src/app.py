from flask import Flask, request, session, json, jsonify, render_template, redirect
from config.bd import app, db, ma


@app.route("/", methods=["GET"])
def index():
    return "Hola mundo!"


if __name__ == "__main__":
    app.run(debug=True)
