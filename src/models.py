from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

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
            return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name":self.name
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(120), unique=True, nullable=False)
    def __repr__(self):
            return '<people %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name":self.name
        }

class Favorite_People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_people=db.Column(db.Integer, db.ForeignKey('people.id'),nullable=False)
    people= db.relationship('People', backref='people', lazy=True)
    id_user=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user= db.relationship('User', backref='user', lazy=True)
    def __repr__(self):
            return '<Favorite_Character %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            
        }

class Favorite_Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_planets=db.Column(db.Integer,db.ForeignKey('planet.id'))
    planet= db.relationship('Planet', backref='planet', lazy=True)
    id_user=db.Column(db.Integer, db.ForeignKey('user.id'))
    user= db.relationship('User', backref='user1', lazy=True)
    def __repr__(self):
            return '<Favorite_Planet %r>' % self.id

    def serialize(self):
        return {
            "id": self.id
        }

# class Favorites(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     id_planets=db.Column(db.Integer,db.ForeignKey('planet.id'))
#     planet=db.relationship('Planet', backref='planet1', lazy=True)
#     id_peoples=db.Column(db.Integer, db.ForeignKey('people.id'))
#     people=db.relationship('People', backref='people1', lazy=True)
#     id_user=db.Column(db.Integer, db.ForeignKey('user.id'))
#     planet=db.relationship('User', backref='user1', lazy=True)
#     def __repr__(self):
#             return '<Favorites %r>' % self.id

#     def serialize(self):
#         return {
#             "id": self.id
#         }