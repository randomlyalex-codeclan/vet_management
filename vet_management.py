from flask import Flask, render_template, request, redirect

from controllers.animal_controller import animals_blueprint
from controllers.vet_controller import vets_blueprint
from controllers.owner_controller import owner_blueprint
import repositories.vet_repository as vet_repository
import repositories.animal_repository as animal_repository
import repositories.owner_repository as owner_repository

app = Flask(__name__)

app.register_blueprint(animals_blueprint)
app.register_blueprint(vets_blueprint)


@app.route("/")
def main():
    return render_template('index.html.j2')


@app.route("/settings", methods=["POST", "GET"])
def settings():
    if request.method == 'GET':
        return render_template('settings.html.j2')
    if request.method == 'POST':
        if request.form['action'] == "delete_all_vets":
            vet_repository.delete_all()
            message = "All Vets Deleted and associated animals deleted"
            return render_template('settings.html.j2', message=message)
        elif request.form['action'] == "delete_all_animals":
            animal_repository.delete_all()
            message = "All Animals Deleted"
            return render_template('settings.html.j2', message=message)


@app.route("/help")
def help():
    return render_template('help.html.j2')


if __name__ == '__main__':
    app.run()
