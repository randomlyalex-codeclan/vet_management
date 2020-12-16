from flask import Flask, render_template, request, redirect

from controllers.animals_controller import animals_blueprint
from controllers.vets_controller import vets_blueprint
from controllers.owners_controller import owners_blueprint
from controllers.treatments_controller import treatments_blueprint
from controllers.settings_controller import settings_blueprint
import repositories.vet_repository as vet_repository
import repositories.animal_repository as animal_repository
import repositories.owner_repository as owner_repository
from models.owner import Owner


app = Flask(__name__)

app.register_blueprint(animals_blueprint)
app.register_blueprint(vets_blueprint)
app.register_blueprint(owners_blueprint)
app.register_blueprint(treatments_blueprint)
app.register_blueprint(settings_blueprint)


@app.route("/")
def main():
    return render_template('index.html.j2')


@app.route("/help")
def help():
    return render_template('help.html.j2')


if __name__ == '__main__':
    app.run()
