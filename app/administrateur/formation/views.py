# app/admin/views.py

from flask import flash, redirect, render_template, url_for, abort
from flask_login import login_required, current_user
from app.administrateur.formation import formations
from app import db
from ..forms import FormationForm
from ...models import Formation


# Department Views


@formations.route('/departements', methods=['GET', 'POST'])
@login_required
def list_formations():
    """
    List all departments
    """

    formations = Formation.query.all()

    return render_template('administrateur/formations/formations.html',
                           formations=formations, title="Formations")


@formations.route('/formations/add', methods=['GET', 'POST'])
@login_required
def add_formations():
    """
    Add a formations to the database
    """

    add_formations = True

    form = FormationForm()
    if form.validate_on_submit():
        formations = Formation(label_formation=form.label_formation.data,
                                description=form.description.data,
                               departement=form.departement.data)
        try:
            # add department to the database
            db.session.add(formations)
            db.session.commit()
            flash('You have successfully added a new formation.')
        except:
            # in case department name already exists
            flash('Error: formation name already exists.')

        # redirect to departments page
        return redirect(url_for('formations.list_formations'))

    # load department template
    return render_template('administrateur/formations/formation.html', action="Add",
                           add_formations=add_formations, form=form,
                           title="Add Formation")


@formations.route('/formations/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_formations(id):
    """
    Edit a formation
    """

    add_departement = False

    formations = Formation.query.get_or_404(id)
    form = FormationForm(obj=formations)
    if form.validate_on_submit():
        formations.label_formation = form.label_formation.data
        formations.description = form.description.data
        formations.departement = form.departement.data
        db.session.commit()
        flash('You have successfully edited the formation.')

        # redirect to the departments page
        return redirect(url_for('formations.list_formations'))

    form.description.data = formations.description
    form.label_formation.data = formations.label_formation
    return render_template('administrateur/formations/formation.html', action="Edit",
                           add_formations=add_departement, form=form,
                           formations=formations, title="Edit Formations")


@formations.route('/formations/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_formations(id):
    """
    Delete a formation from the database
    """

    formations = Formation.query.get_or_404(id)
    db.session.delete(formations)
    db.session.commit()
    flash('You have successfully deleted the formation.')

    # redirect to the departments page
    return redirect(url_for('formations.list_formations'))

    return render_template(title="Delete Formation")