from flask import Flask, render_template, request, redirect, Blueprint, url_for
from models.animal import Animal
from models.vet import Vet
import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository

animals_blueprint = Blueprint("animals", __name__)


@animals_blueprint.route("/animals")
def animals():
    # something is wrong below im going to bed :)
    no_vets = False
    vets = vet_repository.select_all()
    vet = vets[0]
    if vets == []:
        no_vets = True
        message = "No Vets Found, please add these first."
    elif request.args.get('animal_id') != None:
        message = request.args.get(
            'message')+"Animal id"+request.args.get('animal_id')+request.args.get('action')
    all_animals = animal_repository.select_all()
    # return render_template("animals/index.html.j2", all_animals=all_animals, animal_id=animal_id, message=message, action=action)
    return render_template("animals/index.html.j2", vet=vet, **locals())


@ animals_blueprint.route("/animals/new", methods=["POST", "GET"])
def new():
    if request.method == 'GET':
        return render_template("animals/new.html.j2")
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
            message = "Success"
            animal_id = saved_animal.id
        return redirect(url_for("animals.animals", message=message, animal_id=animal_id, action="added"))
    else:
        # POST Error 405 Method Not Allowed
        print("POST Error 405 Method Not Allowed")


@ animals_blueprint.route("/show/<id>")
def detail(id):

    return render_template("animals/show.html.j2")
