# app/__init__.py

# third-party imports
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


# local imports

db = SQLAlchemy()
login_manager = LoginManager()



def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_name)
    app.config.from_pyfile('config.py')

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "etudiant.loginEtud"


    Bootstrap(app)
    db.init_app(app)

    migrate = Migrate(app, db)

    from app import models

    # from .admin import admin as admin_blueprint
    # app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .etudiant import etudiant as etudiant_blueprint
    app.register_blueprint(etudiant_blueprint,url_prefix='/etudiant')

    from .professeur import professeur as professeur_blueprint
    app.register_blueprint(professeur_blueprint, url_prefix='/professeur')

    from .administrateur import administrateur as administrateur_blueprint
    app.register_blueprint(administrateur_blueprint, url_prefix='/administrateur')

    from app.administrateur.departement import departement as departement_blueprint
    app.register_blueprint(departement_blueprint, url_prefix='/departement')

    from app.administrateur.administrateurs import administrateurs as administrateurs_blueprint
    app.register_blueprint(administrateurs_blueprint, url_prefix='/administrateurs')

    from app.administrateur.formation import formations as formations_blueprint
    app.register_blueprint(formations_blueprint, url_prefix='/formations')

    from app.administrateur.professeur import professeurs as professeurs_blueprint
    app.register_blueprint(professeurs_blueprint, url_prefix='/professeurs')

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app
