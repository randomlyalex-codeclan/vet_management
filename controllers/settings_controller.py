from flask import Flask, render_template, request, redirect, Blueprint, url_for
from models.animal import Animal
from models.vet import Vet
from models.owner import Owner
from models.treatment import Treatment
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository
import repositories.animal_repository as animal_repository
import repositories.treatment_repository as treatment_repository

settings_blueprint = Blueprint("settings", __name__)


@settings_blueprint.route("/settings", methods=["POST", "GET"])
def settings():
    if request.method == 'GET':
        return render_template('settings.html.j2')
    if request.method == 'POST':
        if request.form['action'] == "delete_id":
            id = request.form['id']
            if request.form['table'] == "vet":
                vet = vet_repository.select_id(id)
                vet_repository.delete_id(id)
                message = f"Vet {vet.name} {vet.id} deleted, and cascaded"
            elif request.form['table'] == "owner":
                owner = owner_repository.select_id(id)
                owner_repository.delete_id(id)
                message = f"Owner {owner.name} {owner.id} deleted, and cascaded"
            elif request.form['table'] == "animal":
                animal = animal_repository.select_id(id)
                animal_repository.delete_id(id)
                message = f"Vet {animal.name} {animal.id} deleted, and cascaded"
        elif request.form['action'] == "delete_all":
            if request.form['table'] == "vet":
                vet_repository.delete_all()
                message = "All Vets deleted, and cascaded"
            elif request.form['table'] == "owner":
                owner_repository.delete_all()
                message = f"All Owners deleted, and cascaded"
            elif request.form['table'] == "animal":
                animal_repository.delete_all()
                message = f"All Animals deleted, and cascaded"
        return render_template('settings.html.j2', message=message)
