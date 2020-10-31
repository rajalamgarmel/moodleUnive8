# app/home/__init__.py

from flask import Blueprint

etudiant = Blueprint('etudiant', __name__)

from . import views
