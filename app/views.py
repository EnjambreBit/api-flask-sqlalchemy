from flask import jsonify
from flask import request
from sqlalchemy import desc
import datetime
import re

from app import app, db, models, schemas

@app.route('/')
def index():
    return jsonify({'data': {}})

## USERS

@app.route('/users/<uuid>')
def get_user_by_id(uuid):
    if not re.match('[\da-f]{8}-([\da-f]{4}-){3}[\da-f]{12}', uuid):
        return jsonify({"error": "invalid uuid"}), 400

    record = models.User.query.get(uuid)

    if not record:
        return jsonify({"error": "record dont exists"}), 400

    result = schemas.user_schema.dump(record)
    return jsonify({'data': result.data})

@app.route('/users/<uuid>', methods=["PUT"])
def update_user(uuid):
    json_data = request.get_json()

    if not re.match('[\da-f]{8}-([\da-f]{4}-){3}[\da-f]{12}', uuid):
        return jsonify({"error": "invalid uuid"}), 400

    if not json_data:
        return jsonify({'message': 'No input data provided'}), 400

    data, errors = schemas.user_schema.load(json_data)

    if errors:
        return jsonify(errors), 422

    record = models.User.query.get(uuid)

    if not record:
        return jsonify({"error": "record dont exists"}), 400

    for key, value in data.iteritems():
        setattr(record, key, value)

    db.session.commit()

    result = schemas.user_schema.dump(record)
    return jsonify({'data': result.data})

@app.route("/users/<uuid>", methods=["DELETE"])
def delete_user(uuid):
    records = models.User.query.filter_by(id=uuid).all()

    if len(records) > 0:
        result = schemas.user_schema.dump(records[0])
        db.session.delete(records[0])
        db.session.commit()
        return jsonify({'data': result.data})
    else:
        return jsonify({'message': 'No record found'}), 404

@app.route("/users", methods=["POST"])
def create_user():
    json_data = request.get_json()

    if not json_data:
        return jsonify({'message': 'No input data provided'}), 400

    data, errors = schemas.user_schema.load(json_data)

    if errors:
        return jsonify(errors), 422

    user = models.User(data['firstname'], data['lastname'])
    db.session.add(user)
    db.session.commit()

    result = schemas.user_schema.dump(user)
    return jsonify({'data': result.data})

@app.route('/users')
def get_users():
    records = models.User.query.all()
    result = schemas.users_schema.dump(records)
    return jsonify({'data': result.data})
