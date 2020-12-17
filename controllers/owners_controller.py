from flask import Flask, render_template, request, redirect, Blueprint, url_for
from models.animal import Animal
from models.vet import Vet
from models.owner import Owner
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository
import repositories.animal_repository as animal_repository

owners_blueprint = Blueprint("owners", __name__)


@owners_blueprint.route("/owners")
def index():
    owner_repository.create_no_owner()
    message = request.args.get('message')
    show_all = request.args.get('show_all')
    if show_all == "True":
        all_owners = owner_repository.select_all()
    else:
        all_owners = owner_repository.select_all_active()
    return render_template("owners/index.html.j2", **locals())


@owners_blueprint.route("/owners/new", methods=["POST", "GET"])
def new():
    if request.method == 'GET':
        return render_template("owners/new.html.j2")
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        deactivated = False
        if name != "":
            owner = Owner(name, address, deactivated)
            saved_owner = owner_repository.save(owner)
            if saved_owner.id != None:
                message = f"Success {saved_owner.name} added"
            else:
                message = "Failure"
            if request.form['action'] == "finish":
                return redirect(url_for("owners.index", message=message))
            elif request.form['action'] == "continue":
                return render_template("owners/new.html.j2", message=message)
        else:
            return redirect(url_for("owner.index"))
    else:
        print("POST Error 405 Method Not Allowed")


@owners_blueprint.route("/owners/detail/<action>/<id>", methods=["POST", "GET"])
def detail(action, id):
    if request.method == 'GET':
        animals = animal_repository.select_all_by_owner_id(id)
        owner = owner_repository.select_id(id)
        len_animals = len(animal_repository.select_all_by_owner_id(id))
        if action == "show":
            return render_template("owners/show.html.j2", owner=owner, len_animals=len_animals)
        elif action == "edit":
            return render_template("owners/edit.html.j2", owner=owner)
        elif action == "animals":
            return render_template("owners/detail.html.j2", owner=owner, len_animals=len_animals, animals=animals)
        elif action == "orphaned":
            animals = animal_repository.select_all_by_owner_id(1)
            active_owners = owner_repository.select_all_active()
            return render_template("owners/orphaned.html.j2", active_owners=active_owners, owner=owner, len_animals=len_animals, animals=animals)
        else:
            message = "Malformed URL"
            return redirect(url_for("owners.index", message=message))
    if request.method == 'POST':
        if action == "delete":
            owner_repository.delete_id(request.form['id'])
            message = f"Owner: {owner.name} (id:{owner.id}) deleted"
            return redirect(url_for("owners.index", message=message))
        elif action == "edit":
            name = request.form['name']
            address = request.form['address']
            try:
                deactivated = request.form['deactivated']
            except:
                deactivated = False
            id = request.form['id']
            owner = Owner(name, address, deactivated, id)
            owner_repository.update(owner)
            message = f"Owner: {owner.name} (id:{owner.id}) updated"
            return redirect(url_for("owners.index", message=message))
        elif action == "deactivate":
            owner = owner_repository.select_id(id)
            animals = animal_repository.select_all_by_owner_id(id)
            for animal in animals:
                animal.owner = owner_repository.select_id(1)
                animal_repository.update(animal)
            owner.deactivated = True
            owner_repository.update(owner)
            message = f"All animals moved to No Owner, Owner {owner.name} deactivated, please reassign"
            return redirect(url_for("owners.index", message=message))
        else:
            message = "Malformed URL"
            return redirect(url_for("owners.index", message=message))
