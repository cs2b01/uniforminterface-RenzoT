from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import json

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users')
def users():
    db_session = db.getSession(engine)
    users = db_session.query(entities.User)
    data = users[:]
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype = 'application/json')

@app.route('/object_user', methods = ['GET'])
def create_test_books():
    db_session = db.getSession(engine)
    newUser = entities.User(codigo= 201789465, nombre="Domingo", apellido="Dominguez", password="manzana589")
    db_session.add(newUser)
    db_session.commit()
    return "Usuario Creado!"

if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
