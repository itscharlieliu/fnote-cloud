from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

from resources.container import Container


def create_app():
    app = Flask(__name__)
    api = Api(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from common.notes import db
    db.init_app(app)

    api.add_resource(Container, '/')
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
