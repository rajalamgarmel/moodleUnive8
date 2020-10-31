# app/home/__init__.py

from flask import Blueprint

administrateurs = Blueprint('administrateurs', __name__)

from app.administrateur.administrateurs import views
