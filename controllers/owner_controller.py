from flask import Flask, render_template, request, redirect, Blueprint, url_for
from models.animal import Animal
from models.vet import Vet
from models.owner import Owner
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository

owner_blueprint = Blueprint("owner", __name__)
