"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planet, People, Favorite_People, Favorite_Planet, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/people', methods=['GET']) #obtiene todos los personajes
def all_people():
    peoples = People.query.all() 
    data =[people.serialize() for people in peoples]
    return jsonify(data), 200

@app.route('/people/<int:people_id>', methods=['GET'])
def get_people(people_id):
    people = People.query.filter_by(id=people_id).first()
    if people:
        return jsonify({"msg": "Character doesn´t exist"}),400
    return jsonify(people.serialize()),200

@app.route('/planets', methods=['GET']) #obtiene todos los personajes
def all_planets():
    planets = Planet.query.all() 
    data =[planet.serialize() for planet in planets]
    return jsonify(data), 200

@app.route('/planets/<int:planets_id>', methods=['GET'])
def get_planet(planets_id):
    planet = Planet.query.filter_by(id=planets_id).first()
    if planet:
        return jsonify({"msg": "Character doesn´t exist"}),400
    return jsonify(planet.serialize()),200

@app.route('/users', methods=['GET'])
def get_user():
    users=User.query.all()
    data=[user.serialize() for user in users]
    return jsonify(data),200

@app.route('/users/favorites', methods=['GET']) #pendiente de terminar 
def all_favorites():
    favorite = User.query.filter_by()
    data =[favorites.serialize() for favorites in favorite ]
    return jsonify(data),200 

@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def favorite_planet():
    data= request.json
    print("@@@@@@@@", data)
    print("@@@@@@@@", data['id_planets'])
    print("@@@@@@@@", data['id_user'])

    favoritePlanet= favorite_planet(id_user=data['id_user'], id_planets=data['id_planets'])
    db.session.add(favoritePlanet)
    db.session.commit()
    if favoritePlanet():
        return jsonify({"msg": "Your favorite planet cannot be added, wrong details"}), 400

    return jsonify({"msg": "Saved favorite planet"}), 200

@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def favorite_people():
    data= request.json
    print("@@@@@@@@", data)
    print("@@@@@@@@", data['id_peoples'])
    print("@@@@@@@@", data['id_user'])

    favoritePeople= Favorite_People(id_user=data['id_user'], id_people=data['id_peoples'])
    db.session.add(favoritePeople)
    db.session.commit()
    if favoritePeople():
        return jsonify({"msg": "Your favorite people cannot be added, wrong details"}), 400

    return jsonify({"msg": "Saved favorite people"}), 200

@app.route('/favorite/planet/<int:planet_id>',methods=['DELETE'])
def delete_planet(planet_id):
    removePlanet = favorite_planet.query.filter_by(id=planet_id).first
    db.session.delete(removePlanet)
    db.session.commit()
    if removePlanet():
        return jsonify({"message": "Error"}),400

    return jsonify({"message":"Favorite planet removed"}),200

@app.route('/favorite/people/<int:people_id>',methods=['DELETE'])
def delete_people(people_id):
    removePeople = favorite_planet.query.filter_by(id=people_id).first
    db.session.delete(removePeople)
    db.session.commit()
    if removePeople():
        return jsonify({"message": "Error"}),400

    return jsonify({"message":"Favorite people removed"}),200















# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
