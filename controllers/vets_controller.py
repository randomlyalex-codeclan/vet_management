from flask import Flask, render_template, request, redirect, Blueprint, url_for
from models.animal import Animal
from models.vet import Vet
import repositories.vet_repository as vet_repository
import repositories.animal_repository as animal_repository

vets_blueprint = Blueprint("vets", __name__)


@vets_blueprint.route("/vets")
def index():
    message = request.args.get('message')
    show_all = request.args.get('show_all')
    if show_all == "True":
        all_vets = vet_repository.select_all()
    else:
        all_vets = vet_repository.select_all_active()
    return render_template("vets/index.html.j2", **locals())


@vets_blueprint.route("/vets/new", methods=["POST", "GET"])
def new():
    if request.method == 'GET':
        return render_template("vets/new.html.j2")
    if request.method == 'POST':
        name = request.form['name']
        deactivated = False
        if name != "":
            vet = Vet(name, deactivated)
            saved_vet = vet_repository.save(vet)
            if saved_vet.id != None:
                message = f"Success {saved_vet.name} added"
            else:
                message = "Failure"
            if request.form['action'] == "finish":
                return redirect(url_for("vets.index", message=message))
            elif request.form['action'] == "continue":
                return render_template("vets/new.html.j2", message=message)
            else:
                message = "Malformed URL"
            return redirect(url_for("vets.index", message=message))
        else:
            return redirect(url_for("vets.index"))
    else:
        message = "Error finding or displaying page"
        return redirect(url_for("index", message=message))


@ vets_blueprint.route("/vets/detail/<action>/<id>", methods=["POST", "GET"])
def detail(action, id):
    vet = vet_repository.select_id(id)
    if request.method == 'GET':
        if action == "show":
            return render_template("vets/show.html.j2", vet=vet)
        elif action == "edit":
            return render_template("vets/edit.html.j2", vet=vet)
        else:
            message = "Error Malformed URL"
            return redirect(url_for("vets.index", message=message))
    if request.method == 'POST':
        if action == "delete":
            vet_repository.delete_id(request.form['id'])
            message = f"Vet: {vet.name} (id:{vet.id}) deleted"
            return redirect(url_for("vets.index", message=message))
        elif action == "edit":
            name = request.form['name']
            try:
                deactivated = request.form['deactivated']
                if len(animal_repository.select_all_by_vet_id(id)) > 0:
                    message = f"Vet: {vet.name} (id:{vet.id}) has animals assigned"
                    return redirect(url_for("vets.index", message=message))
            except:
                deactivated = False
            vet = Vet(name, deactivated, id)
            vet_repository.update(vet)
            message = f"Vet: {vet.name} (id:{vet.id}) updated"
            return redirect(url_for("vets.index", message=message))
        elif action == "deactivate":
            if len(animal_repository.select_all_by_vet_id(id)) == 0:
                vet = vet_repository.select_id(id)
                vet.deactivated = True
                vet_repository.update(vet)
                message = f"Vet: {vet.name} (id:{vet.id}) has been deactivated"
            else:
                message = f"Vet: {vet.name} (id:{vet.id}) has animals assigned, reassign these first"
            return redirect(url_for("vets.index", message=message))
        else:
            message = "Error Malformed URL"
            return redirect(url_for("vets.index", message=message))
