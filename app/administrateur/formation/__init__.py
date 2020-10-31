# app/home/__init__.py

from flask import Blueprint

formations = Blueprint('formations', __name__)

from app.administrateur.formation import views
