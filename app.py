from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from locale import setlocale, LC_ALL
from time import strftime

setlocale(LC_ALL, 'es_CO.utf8')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/registros.db'
db = SQLAlchemy(app)


class Actividad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String(200))
    observaciones = db.Column(db.String(400))


class Estacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(400))


@app.route('/create/<id>', methods=['POST'])
def create(id):
    fecha = strftime("%I:%M:%S %p, %A (%d %B %Y)")
    nueva_actividad = Actividad(fecha=fecha, observaciones=request.form['observaciones'])
    db.session.add(nueva_actividad)
    db.session.commit()
    return redirect(url_for('read', id=id))


@app.route('/')
def home():
    return redirect(url_for('read', id=0))


@app.route('/<id>')
def read(id):
    actividades = Actividad.query.all()
    estaciones = Estacion.query.all()
    return render_template('index.html', actividades=actividades, estaciones=estaciones, id=int(id))


@app.route('/<id>/delete/<identificador>')
def delete(id, identificador):
    Actividad.query.filter_by(id=int(identificador)).delete()
    db.session.commit()
    return redirect(url_for('read', id=id))


@app.route('/change/<id>')
def change(id):
    id = int(id)
    length = len(Estacion.query.all()) - 1

    if id < 0:
        id = length

    if id > length:
        id = 0

    return redirect(url_for('read', id=id))


if __name__ == '__main__':
    app.run(debug=True, port=5002)
