# app/auth/views.py

from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user
from .. import db
from app.etudiant import etudiant
from .forms import LoginForm
from ..models import Etudiant



@etudiant.route('/loginEtud', methods=['GET', 'POST'])
def loginEtud():
    """
    Handle requests to the /login route
    Log an employee in through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():

        # check whether employee exists in the database and whether
        # the password entered matches the password in the database
        etudiant = Etudiant.query.filter_by(email=form.email.data).first()
        if etudiant is not None and Etudiant.query.filter_by(password_hash=form.password.data).first():
            # log employee in
            # log employee in
            login_user(etudiant)


            return redirect(url_for('etudiant.AccueilEtud'))

        # when login details are incorrect
        else:
            flash('Invalid email or password.')

    # load login template
    return render_template('etudiant/LoginEtud.html', form=form, title='Login')


@etudiant.route('/logoutEtud')
@login_required
def logoutEtud():
    """
    Handle requests to the /logout route
    Log an employee out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('etudiant.loginEtud'))


@etudiant.route('/AccueilEtud')
@login_required
def AccueilEtud():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('etudiant/AccueilEtud.html', title="Dashboard")
