from flask import Flask, render_template, request, redirect, Blueprint, url_for
from models.animal import Animal
from models.vet import Vet
from models.treatment import Treatment
import repositories.vet_repository as vet_repository
import repositories.animal_repository as animal_repository
import repositories.treatment_repository as treatment_repository

treatments_blueprint = Blueprint("treatments", __name__)


@treatments_blueprint.route("/treatments")
def index():
    message = request.args.get('message')
    show_all = request.args.get('show_all')
    all_treatments = treatment_repository.select_all()
    return render_template("treatments/index.html.j2", **locals())


@treatments_blueprint.route("/treatments/new", methods=["POST", "GET"])
def new():
    if request.method == 'GET':
        message = request.args.get('message')
        show_all = request.args.get('show_all')
        active_vets = vet_repository.select_all_active()
        active_animals = animal_repository.select_all_active()
        return render_template("treatments/new.html.j2", **locals())
    if request.method == 'POST':
        vet_id = request.form['vet_id']
        animal_id = request.form['animal_id']
        date = request.form['date']
        notes = request.form['notes']
        weight = request.form['weight']
        treatment = Treatment(vet_id, animal_id, date, notes, weight)
        saved_treatment = treatment_repository.save(treatment)
        message = f"Treatment ID:{saved_treatment.id} Added"
        return redirect(url_for("treatments.index", message=message))
