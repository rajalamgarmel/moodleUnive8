# app/admin/views.py

from flask import flash, redirect, render_template, url_for, abort
from flask_login import login_required, current_user
from app.administrateur.departement import departement
from app import db
from ..forms import DepartementForm
from ...models import Departement

def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_superadmin:
        abort(403)


# Department Views


@departement.route('/departements', methods=['GET', 'POST'])
@login_required
def list_departements():
    """
    List all departments
    """
    check_admin()

    departements = Departement.query.all()

    return render_template('administrateur/departement/departements.html',
                           departements=departements, title="Departements")


@departement.route('/departments/add', methods=['GET', 'POST'])
@login_required
def add_departement():
    """
    Add a department to the database
    """
    check_admin()

    add_departement = True

    form = DepartementForm()
    if form.validate_on_submit():
        departement = Departement(label_departement=form.label.data,
                                description=form.description.data)
        try:
            # add department to the database
            db.session.add(departement)
            db.session.commit()
            flash('You have successfully added a new department.')
        except:
            # in case department name already exists
            flash('Error: department name already exists.')

        # redirect to departments page
        return redirect(url_for('departement.list_departements'))

    # load department template
    return render_template('administrateur/departement/departement.html', action="Add",
                           add_departement=add_departement, form=form,
                           title="Add Departement")


@departement.route('/departments/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_departement(id):
    """
    Edit a department
    """
    check_admin()

    add_departement = False

    departement = Departement.query.get_or_404(id)
    form = DepartementForm(obj=departement)
    if form.validate_on_submit():
        departement.label_departement = form.label.data
        departement.description = form.description.data
        db.session.commit()
        flash('You have successfully edited the department.')

        # redirect to the departments page
        return redirect(url_for('departement.list_departements'))

    form.description.data = departement.description
    form.label.data = departement.label_departement
    return render_template('administrateur/departement/departement.html', action="Edit",
                           add_departement=add_departement, form=form,
                           departement=departement, title="Edit Departement")


@departement.route('/departments/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_departement(id):
    """
    Delete a department from the database
    """
    check_admin()

    departement = Departement.query.get_or_404(id)
    db.session.delete(departement)
    db.session.commit()
    flash('You have successfully deleted the department.')

    # redirect to the departments page
    return redirect(url_for('departement.list_departements'))

    return render_template(title="Delete Departement")