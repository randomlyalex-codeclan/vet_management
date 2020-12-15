from flask import Flask, render_template, request, redirect, Blueprint, url_for
from models.animal import Animal
from models.vet import Vet
import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository
import repositories.treatment_repository as treatment_repository

animals_blueprint = Blueprint("animals", __name__)


@animals_blueprint.route("/animals")
def index():
    # something is wrong below im going to bed :)
    no_vets = False
    message = request.args.get('message')
    show_all = request.args.get('show_all')
    if vet_repository.select_all() == []:
        no_vets = True
        message = "No Vets Found, please add these first."
        # figure out how to pass a param here i can check for
    elif show_all == "True":
        all_animals = animal_repository.select_all()
    else:
        all_animals = animal_repository.select_all_active()
    # return render_template("animals/index.html.j2", all_animals=all_animals, animal_id=animal_id, message=message, action=action)
    return render_template("animals/index.html.j2", **locals())


@ animals_blueprint.route("/animals/new", methods=["POST", "GET"])
def new():
    vets = vet_repository.select_all()
    if request.method == 'GET':
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
            return render_template("animals/new.html.j2", message=message, vets=vets)
    else:
        # POST Error 405 Method Not Allowed
        print("POST Error 405 Method Not Allowed")


@ animals_blueprint.route("/animals/detail/<action>/<id>", methods=["POST", "GET"])
def detail(action, id):
    animal = animal_repository.select_id(id)
    if request.method == 'GET':
        if action == "show":
            len_treatments = len(
                treatment_repository.select_all_by_animal_id(id))
            return render_template("animals/show.html.j2", animal=animal, len_treatments=len_treatments)
        if action == "edit":
            vets = vet_repository.select_all()
            return render_template("animals/edit.html.j2", animal=animal, vets=vets)
        if action == "treatments":
            treatments = animal.get_treatments()
            len_treatments = len(treatments)
            return render_template("animals/detail.html.j2", animal=animal, len_treatments=len_treatments, treatments=treatments)
        if action == "treatments_edit":
            treatments = animal.get_treatments()
            len_treatments = len(treatments)
            return render_template("animals/treatments_edit.html.j2", animal=animal, len_treatments=len_treatments, treatments=treatments)
    if request.method == 'POST':
        if action == "delete":
            animal_repository.delete_id(request.form['id'])
            message = f"Animal: {animal.name} (id:{animal.id}) deleted"
            return redirect(url_for("animals.index", message=message))
        if action == "edit":
            name = request.form['name']
            dob = request.form['dob']
            species = request.form['species']
            owner_id = request.form['owner_id']
            vet_id = request.form['vet_id']
            id = request.form['id']
            try:
                deactivated = request.form['deactivated']
            except:
                deactivated = False
            vet = vet_repository.select_id(vet_id)
            owner = owner_repository.select_id(owner_id)
            animal = Animal(name, dob, species, owner, vet, deactivated, id)
            animal_repository.update(animal)
            message = f"Animal: {animal.name} (id:{animal.id}) updated"
            return redirect(url_for("animals.index", message=message))
        if action == "treatments_delete_all":
            animal = animal_repository.select_id(request.form['id'])
            animal.clear_treatment_history()
            animal_repository.update(animal)
            message = f"Animal: {animal.name} (id:{animal.id}) treatments deleted"
            return redirect(url_for(f"animals.detail", action="show", id=animal.id, message=message))
        else:
            message = "Malformed URL"
            return redirect(url_for("animals.index", message=message))
