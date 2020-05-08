import json
import string
import random

from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Notes(db.Model):
    id = db.Column(db.String(6), primary_key=True)
    note = db.Column(db.String(500))

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return str(self.note)

    def __str__(self):
        return str(self.note)


db.create_all()


class Container(Resource):
    def get(self, note_id=None):
        notes = Notes.query.all()

        if len(notes) <= 0 or not note_id:
            return ""

        for note in range(len(notes)):
            print("{} {}".format(notes[note].get_id(), notes[note]))

        return str(notes[0])

    def post(self):
        user_input = request.get_json()

        note_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))

        note = Notes(id=note_id, note=user_input)
        db.session.add(note)
        db.session.commit()
        return "", 201


api.add_resource(Container, '/', '/<int:note_id>')

if __name__ == '__main__':
    app.run()
