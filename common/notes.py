from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String(500))

    def __repr__(self):
        return self.note


db.create_all()
