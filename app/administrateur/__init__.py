# app/home/__init__.py

from flask import Blueprint

administrateur = Blueprint('administrateur', __name__)

from . import views