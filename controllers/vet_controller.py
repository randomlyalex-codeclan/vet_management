from flask import Flask, render_template, request, redirect, Blueprint
from models.animal import Animal
from models.vet import Vet
import repositories.vet_repository as vet_repository

vets_blueprint = Blueprint("vets", __name__)


@vets_blueprint.route("/vets")
def vets():
    all_vets = vet_repository.select_all()
    return render_template("vets/index.html.j2", all_vets=all_vets)
