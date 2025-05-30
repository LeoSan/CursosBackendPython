from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)

import os
from flask_sqlalchemy import SQLAlchemy

DB_FILE_PATH = os.path.join(
    os.path.dirname(__file__),
    "notes.sqlite"
)

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_FILE_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<Note {self.id}: {self.title}>"


@app.route("/")
def home():
    notes = Note.query.all()
    return render_template("home.html", notes=notes)

@app.route("/acerca-de")
def about():
    return "Esto es una app de notas"

@app.route("/contacto", methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        return "Formulario enviado correctamente", 201
    return "Pagina de contacto"


@app.route("/api/info")
def api_info():
    data = {
        "nombre": "Notes App",
        "version": "1.1.1"
    }
    return jsonify(data), 200

@app.route("/confirmacion")
def confirmation():
    return "Prueba"

@app.route("/crear-nota", methods=["GET", "POST"])
def create_note():
    if request.method == "POST":
        title = request.form.get("title", "")
        content = request.form.get("content", "")

        note_db = Note(
            title=title, content=content
        )
        db.session.add(note_db)
        db.session.commit()

        return redirect(url_for("home"))
    return render_template("note_form.html")

@app.route('/editar-nota/<int:id>', methods=["GET", "POST"])
def edit_note(id):
    note = Note.query.get_or_404(id)
    if request.method == "POST":
        title = request.form.get("title", "")
        content = request.form.get("content", "")
        note.title = title
        note.content = content
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit_note.html", note=note)

@app.route('/delete-note/<int:id>', methods=['POST'])
def delete_note(id):
    note = Note.query.get(id)
    
    if not note:
        # Si la nota no existe, no tiene sentido intentar borrarla
        return redirect(url_for('home'))
    
    db.session.delete(note)
    db.session.commit()
    
    return redirect(url_for('home'))