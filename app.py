import json

from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String(500))

    def __repr__(self):
        return self.note.__str__()

    def __str__(self):
        return self.note.__str__()


db.create_all()


class Container(Resource):
    def get(self, note_id):
        # user_input = json.loads(request.get_json())

        notes = Notes.query.all()

        for note in range(len(notes)):
            print(notes[note])

        print(notes[0])

        return {"result": str(notes[0])}

    def post(self):
        user_input = request.get_json()
        if 'note' not in user_input.keys():
            return "JSON must contain key 'note'", 400
        note = Notes(note=user_input['note'])
        db.session.add(note)
        db.session.commit()
        return "", 201


api.add_resource(Container, '/<int:note_id>')

if __name__ == '__main__':
    app.run()
