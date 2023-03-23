from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(120), unique=True, nullable=False)
    def __repr__(self):
            return '<Planets %r>' % self.username

    def serialize(self):
        return {
            "id": self.id
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(120), unique=True, nullable=False)
    def __repr__(self):
            return '<Characters %r>' % self.username

    def serialize(self):
        return {
            "id": self.id
        }

class Favorite_People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_peoples=db.Column(db.Integer, db.ForeignKey('people.id'))
    id_user=db.Column(db.Integer, db.ForeignKey('user.id'))
    def __repr__(self):
            return '<Favorite_Character %r>' % self.username

    def serialize(self):
        return {
            "id": self.id
        }

class Favorite_Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_planets=db.Column(db.Integer,db.ForeignKey('planet.id'))
    id_user=db.Column(db.Integer, db.ForeignKey('user.id'))
    def __repr__(self):
            return '<Favorite_Planet %r>' % self.username

    def serialize(self):
        return {
            "id": self.id
        }

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_planets=db.Column(db.Integer,db.ForeignKey('planet.id'))
    id_peoples=db.Column(db.Integer, db.ForeignKey('people.id'))
    id_user=db.Column(db.Integer, db.ForeignKey('user.id'))
    def __repr__(self):
            return '<Favorites %r>' % self.username

    def serialize(self):
        return {
            "id": self.id
        }