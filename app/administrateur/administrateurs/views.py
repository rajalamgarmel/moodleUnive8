# app/admin/views.py

from flask import flash, redirect, render_template, url_for, abort
from flask_login import login_required, current_user
from app.administrateur.administrateurs import administrateurs
from app import db
from ..forms import AdminForm
from ...models import Administrateur


def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_superadmin:
        abort(403)


@administrateurs.route('/administrateurs', methods=['GET', 'POST'])
@login_required
def list_administrateurs():
    """
    List all administrateurs
    """
    check_admin()

    administrateurs = Administrateur.query.all()

    return render_template('administrateur/administrateurs/administrateurs.html',
                           administrateurs=administrateurs, title="Administrateurs")


@administrateurs.route('/administrateurs/add', methods=['GET', 'POST'])
@login_required
def add_administrateurs():
    check_admin()

    #administrateurs = Administrateur.query.get_or_404(id)

    # prevent admin from being assigned a department or role
    #if Administrateur.is_superadminadmin:
     #   abort(403)

   # add_administrateurs = True

    form = AdminForm()
    if form.validate_on_submit():
        administrateurs = Administrateur(nom_admin=form.nom.data,
                                         prenom_admin=form.prenom.data,
                                         sexe_admin=form.sexe.data,
                                         email=form.email.data,
                                         date_naissance=form.dateNaissance.data,
                                         password_hash=form.dateNaissance.data,
                                         departement=form.departement.data)
        #administrateurs.departement = form.departement.data

        try:
            # add department to the database
            db.session.add(administrateurs)
            db.session.commit()
            flash('You have successfully added a new administrateur .')
        except:
            # in case department name already exists
            flash('Error: administrateur name already exists.')

        # redirect to departments page
        return redirect(url_for('administrateurs.list_administrateurs'))

    # load department template
    return render_template('administrateur/administrateurs/administrateur.html', action="Add",
                           add_administrateurs=add_administrateurs, form=form,
                           title="Add Administrateur")


@administrateurs.route('/administrateurs/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_administrateurs(id):
    """
    Edit a department
    """
    check_admin()

    add_administrateurs = False

    administrateurs = Administrateur.query.get_or_404(id)
    form = AdminForm(obj=administrateurs)
    if form.validate_on_submit():
        administrateurs.nom_admin = form.nom.data
        administrateurs.prenom_admin = form.prenom.data
        administrateurs.date_naissance = form.dateNaissance.data
        administrateurs.email = form.email.data
        administrateurs.sexe_admin = form.sexe.data
        administrateurs.departement = form.departement.data
        db.session.commit()
        flash('You have successfully edited the administrateurs.')

        # redirect to the departments page
        return redirect(url_for('administrateurs.list_administrateurs'))

    form.nom.data = administrateurs.nom_admin
    form.prenom.data = administrateurs.prenom_admin
    form.dateNaissance.data = administrateurs.date_naissance
    form.email.data = administrateurs.email
    form.sexe.data = administrateurs.sexe_admin
    form.departement.data = administrateurs.departement
    return render_template('administrateur/administrateurs/administrateur.html', action="Edit",
                           add_departement=add_administrateurs, form=form,
                           departement=administrateurs, title="Edit administrateurs")


@administrateurs.route('/administrateurs/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_administrateurs(id):
    """
    Delete a department from the database
    """
    check_admin()

    administrateurs = Administrateur.query.get_or_404(id)
    db.session.delete(administrateurs)
    db.session.commit()
    flash('You have successfully deleted the department.')

    # redirect to the departments page
    return redirect(url_for('administrateurs.list_administrateurs'))

    return render_template(title="Delete administrateurs")
