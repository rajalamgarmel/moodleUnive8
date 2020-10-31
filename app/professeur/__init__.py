# app/home/__init__.py

from flask import Blueprint

professeur = Blueprint('professeur', __name__)

from . import views
