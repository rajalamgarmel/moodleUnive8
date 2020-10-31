# app/home/__init__.py

from flask import Blueprint

professeurs = Blueprint('professeurs', __name__)

from app.administrateur.professeur import views
