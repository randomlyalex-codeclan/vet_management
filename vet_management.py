from flask import Flask, render_template, request, redirect

from controllers.animals_controller import animals_blueprint
from controllers.vets_controller import vets_blueprint
from controllers.owners_controller import owners_blueprint
from controllers.treatments_controller import treatments_blueprint
import repositories.vet_repository as vet_repository
import repositories.animal_repository as animal_repository
import repositories.owner_repository as owner_repository
from models.owner import Owner


app = Flask(__name__)

app.register_blueprint(animals_blueprint)
app.register_blueprint(vets_blueprint)
app.register_blueprint(owners_blueprint)
app.register_blueprint(treatments_blueprint)

@app.route("/")
def main():
    return render_template('index.html.j2')


@app.route("/settings", methods=["POST", "GET"])
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


@app.route("/help")
def help():
    return render_template('help.html.j2')


if __name__ == '__main__':
    app.run()
