from flask import Flask, render_template, request, redirect, Blueprint, url_for
from models.animal import Animal
from models.vet import Vet
from models.owner import Owner
from models.treatment import Treatment
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository
import repositories.treatment_repository as treatment_repository

treatments_blueprint = Blueprint("treatments", __name__)


@treatments_blueprint.route("/treatments")
def index():
    message = request.args.get('message')
    show_all = request.args.get('show_all')
    # animal_id = "Animal id"+str(request.args.get('animal_id'))
    # action = request.args.get('action')
    all_treatments = treatment_repository.select_all()
    return render_template("treatments/index.html.j2", **locals())
