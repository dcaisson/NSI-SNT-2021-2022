#!/usr/bin/python
# -*- coding: UTF-8

from flask import Flask, render_template
#from fonctions_guirlandes import (
#    allume_ascendant,
#    allume_descendant,
#    allume_alterne,
#    allume_aleatoirement,
#)

# Initialisation de la méthode
app = Flask(__name__)

# Gestion du chemin
@app.route("/", methods=["GET"])
def affiche_index():
    return render_template("index.html")


@app.route("/<command>", methods=["GET"])
def action(command):
    print("Requête GET " + command + " bien reçue")
    if command == "Ascendant":
        allume_ascendant()
    elif command == "Descendant":
        allume_descendant()
    elif command == "Alterné":
        allume_alterne()
    elif command == "Aléatoire":
        allume_aleatoirement()
    return ("Succès", 200)


"""
@app.route("/Ascendant", methods=["GET"])
def action_ascendant():
    print("Requête GET /Ascendant bien reçue")
    return ("Succès", 200)


@app.route("/Descendant", methods=["GET"])
def action_descendant():
    print("Requête GET /Descendant bien reçue")
    return ("Succès", 200)


@app.route("/Alterné", methods=["GET"])
def action_alterne():
    print("Requête GET /Alterné bien reçue")
    return ("Succès", 200)


@app.route("/Aléatoire", methods=["GET"])
def action_aleatoire():
    print("Requête GET /Aléatoire bien reçue")
    return ("Succès", 200)
"""

# Lancement du serveur web
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5555, debug=True)
