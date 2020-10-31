from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user, current_user, login_manager
from .. import db
from app.professeur import professeur
from .forms import LoginForm
from ..models import Professeur


@professeur.route('/loginProf', methods=['GET', 'POST'])
def loginProf():
    """
    Handle requests to the /login route
    Log an employee in through the login form
    """
    formprof = LoginForm()
    if formprof.validate_on_submit():

        # check whether employee exists in the database and whether
        # the password entered matches the password in the database
        professeur = Professeur.query.filter_by(email=formprof.email.data).first()
        if professeur is not None and Professeur.query.filter_by(password_hash=formprof.password.data).first():
            # log employee in
            # log employee in
            login_user(professeur)

            @login_manager.user_loader
            def load_user(id):
                return Professeur.query.get(int(id))

            return redirect(url_for('professeur.AcceuilProfesseur'))

        # when login details are incorrect
        else:
            flash('Invalid email or password.')

    # load login template
    return render_template('professeur/LoginProf.html', form=formprof, title='Login')


@professeur.route('/logoutProf')
@login_required
def logoutProf():
    """
    Handle requests to the /logout route
    Log an employee out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('professeur.loginProf'))


@professeur.route('/AcceuilProfesseur')
@login_required
def AcceuilProfesseur():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('professeur/AccueilProf.html', title="Dashboard")
