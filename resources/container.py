import json

from flask import request
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy

from common.notes import db, Notes


class Container(Resource):
    def get(self):
        user_input = json.loads(request.get_json())

        return {"about": "Hello world"}

    def post(self):
        user_input = request.get_json()
        if 'note' not in user_input.keys():
            return "JSON must contain key 'note'", 400
        note = Notes(note=user_input['note'])
        db.session.add(note)
        db.session.commit()
        return None, 201
