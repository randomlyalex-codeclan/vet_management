from flask import Flask, render_template, request, redirect, Blueprint, url_for
from models.animal import Animal
from models.vet import Vet
import repositories.vet_repository as vet_repository

vets_blueprint = Blueprint("vets", __name__)


@vets_blueprint.route("/vets")
def index():
    message = request.args.get('message')
    animal_id = "Animal id"+str(request.args.get('animal_id'))
    action = request.args.get('action')
    all_vets = vet_repository.select_all()
    return render_template("vets/index.html.j2", **locals())


@vets_blueprint.route("/vets/new", methods=["POST", "GET"])
def new():
    if request.method == 'GET':
        return render_template("vets/new.html.j2")
    if request.method == 'POST':
        name = request.form['name']
        if name != "":
            vet = Vet(name)
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
            return redirect(url_for("vets.index"))
    else:
        # POST Error 405 Method Not Allowed
        print("POST Error 405 Method Not Allowed")


@ vets_blueprint.route("/show/<id>")
def detail(id):
    vet = vet_repository.select_id(id)
    return render_template("vets/show.html.j2", vet=vet)
