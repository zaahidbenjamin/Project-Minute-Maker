from flask import Blueprint, render_template, request, flash, jsonify, redirect
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        Date=request.form.get("note.dates")
        Topic=request.form.get("note.topic")
        Attendees=request.form.get("note.Attendees")
        Raisedby=request.form.get("note.Raisedby")
        Actionrequired=request.form.get("note.Actionrequired")
        Actionedby=request.form.get("note.Actionedby")
        Information=request.form.get("note.Information")
        Dateofcompletion=request.form.get("note.Dateofcompletion")
        new_note = Note(Dates=Date, Topic=Topic, Attendees=Attendees, Raisedby=Raisedby, Actionrequired=Actionrequired, Actionedby=Actionedby, Information=Information, Dateofcompletion=Dateofcompletion, user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()
        flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete/<int:id>')
@login_required
def delete(id):
    post_to_delete = Note.query.get_or_404(id)
    id = current_user.id
    if id == current_user.id:
        db.session.delete(post_to_delete)
        db.session.commit()
    return redirect("/")
        # Return a message


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
