from flask import Flask, render_template, request, redirect, Blueprint, url_for
from models.animal import Animal
from models.vet import Vet
import repositories.vet_repository as vet_repository

vets_blueprint = Blueprint("vets", __name__)


@vets_blueprint.route("/vets")
def vets():
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
        vet = Vet(name)
        saved_vet = vet_repository.save(vet)
        if saved_vet.id != None:
            message = "Success"
            vet_id = saved_vet.id
        return redirect(url_for("vets.vets", message=message, vet_id=vet_id, action="added"))
    else:
        # POST Error 405 Method Not Allowed
        print("POST Error 405 Method Not Allowed")


@vets_blueprint.route("/show/<id>")
def detail(id):

    return render_template("vets/show.html.j2")
