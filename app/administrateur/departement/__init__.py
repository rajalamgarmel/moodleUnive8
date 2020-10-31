# app/home/__init__.py

from flask import Blueprint

departement = Blueprint('departement', __name__)

from app.administrateur.departement import views
