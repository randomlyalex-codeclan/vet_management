from flask import Flask, render_template, request, redirect, Blueprint
from models.animal import Animal
from models.vet import Vet
import repositories.animal_repository as animal_repository

animals_blueprint = Blueprint("animals", __name__)


@animals_blueprint.route("/animals")
def animals():
    return render_template("animals/index.html")
