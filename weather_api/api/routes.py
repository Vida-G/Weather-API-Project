from flask import Blueprint, request, jsonify, url_for
# from werkzeug.wrappers import response
# #from werkzeug.wrappers import request
from weather_api.helpers import token_required
from weather_api.models import User, Weather, db, weather_schema, weathers_schema

api = Blueprint('api', __name__, url_prefix='/api')


# CRUD functionality below

@api.route('/weathers', methods=['POST'])
@token_required
def create_weather(current_user_token):
    name = request.json['name']
    description = request.json['description']
    city = request.json['city']
    country = request.json['country']
    temperature = request.json['temperature']
    wind_speed = request.json['wind_speed']
    date_created = request.json['date_created']
    token = current_user_token.token

    print(f'TEST: {current_user_token.token}')

    weather = Weather(name,description,city,country,temperature,wind_speed,date_created,user_token = token)

    db.session.add(weather)
    db.session.commit()

    response = weather_schema.dump(weather)
    return jsonify(response)



@api.route('/weathers', methods = ['GET'])
@token_required
def get_weathers(current_user_token):
    owner = current_user_token.token
    weathers = Weather.query.filter_by(user_token = owner).all()
    response = weathers_schema.dump(weathers)
    return jsonify(response)


@api.route('/weathers/<id>', methods= ['GET'])
@token_required
def get_weather(current_user_token, id):
    weather = Weather.query.get(id)
    if weather:
        response = weather_schema.dump(weather)
        return jsonify(response)
    else:
        return jsonify({'Error': 'The information does not exist!'})



@api.route('/weathers/<id>', methods= ['POST', 'PUT'])
@token_required
def update_weather(current_user_token, id):
    weather = Weather.query.get(id)
    print(weather)
    if weather:
        weather.name = request.json['name']
        weather.description = request.json['description']
        weather.city = request.json['city']
        weather.country = request.json['country']
        weather.temperature = request.json['temperature']
        weather.wind_speed = request.json['wind_speed']
        weather.date_created = request.json['date_created']
        weather.token = current_user_token.token
        db.session.commit()

        response = weather_schema.dump(weather)
        return jsonify(response)
    else:
        return jsonify({'Error': 'The information does not exist!'})


@api.route('/weathers/<id>', methods= ['DELETE'])
@token_required
def delete_weather(urrent_user_token, id):
    weather = Weather.query.get(id)
    if weather:
        db.session.delete(weather)
        db.session.commit()
        return jsonify({'Success': f'ID #{weather.id} has been deleted'})
    else:
        return jsonify({'Error': 'The information does not exist!'})

