from flask import Flask, render_template, request, redirect, Blueprint, url_for
from models.animal import Animal
from models.vet import Vet
import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository

animals_blueprint = Blueprint("animals", __name__)


@animals_blueprint.route("/animals")
def index():
    # something is wrong below im going to bed :)
    no_vets = False
    vets = vet_repository.select_all()

    if vets == []:
        no_vets = True
        message = "No Vets Found, please add these first."
    elif request.args.get('animal_id') != None:
        message = request.args.get(
            'message')+"Animal id"+request.args.get('animal_id')+request.args.get('action')
    all_animals = animal_repository.select_all()
    # return render_template("animals/index.html.j2", all_animals=all_animals, animal_id=animal_id, message=message, action=action)
    return render_template("animals/index.html.j2", **locals())


@ animals_blueprint.route("/animals/new", methods=["POST", "GET"])
def new():
    if request.method == 'GET':
        vets = vet_repository.select_all()
        return render_template("animals/new.html.j2", vets=vets)
    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
        species = request.form['species']
        owner = request.form['owner']
        vet_id = request.form['vet_id']
        vet = vet_repository.select_id(vet_id)
        animal = Animal(name, dob, species, owner, vet)
        saved_animal = animal_repository.save(animal)
        if saved_animal.id != None:
            message = f"Success {saved_animal.name} added"
        else:
            message = "Failure"
        if request.form['action'] == "finish":
            return redirect(url_for("animals.index", message=message))
        elif request.form['action'] == "continue":
            return render_template("animals/new.html.j2", message=message)
    else:
        # POST Error 405 Method Not Allowed
        print("POST Error 405 Method Not Allowed")


@ animals_blueprint.route("/show/<id>")
def detail(id):

    return render_template("animals/show.html.j2")
