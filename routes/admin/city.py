from flask import Blueprint, jsonify,request
from models.city import City
from models import session
from datetime import datetime
from flask_jwt_extended import jwt_required,get_jwt_identity
from flask_jwt_extended import create_access_token
city_bp = Blueprint('city', __name__)


@city_bp.route('/')
@jwt_required()
def get_city():
    currentID = get_jwt_identity()
    status_param = request.args.get('status')
    if status_param is not None:
        status = int(status_param)
        if status == 1:
            arr = session.query(City).filter_by(status=1).all()
        else:
            arr = session.query(City).all()
    else:
        arr = session.query(City).all()
    result = []
    for cityData in arr:
        result.append({
            'id' :cityData.id,
            'title': cityData.title,
            'ar_title':cityData.ar_title,
            'status':cityData.status
        })
    session.close()
    return jsonify(result)


@city_bp.route('/<id>', methods=['GET'])
@jwt_required()
def get_user(id):
    currentID = get_jwt_identity()
    arr = session.query(City).get(id)
    if arr:
        return jsonify({
            'id' :arr.id,
            'title': arr.title,
            'ar_title':arr.ar_title,
            'status':arr.status
        })
    session.close()
    return jsonify({'message': 'City not found'}), 404


@city_bp.route('/addcity', methods=['POST'])
@jwt_required()
def create_city():
    currentID = get_jwt_identity()
    data = request.get_json()
    # Create a new city
    new_city = City(title=data['title'],ar_title=data['ar_title'],status=data['status'],created_by=currentID,updated_by = currentID)
    session.add(new_city)
    session.commit()
    session.close()
    return jsonify({'message': 'City created successfully'}), 201


@city_bp.route('/updatecity/<id>', methods=['PUT'])
@jwt_required()
def update_user(id):
    currentID = get_jwt_identity()
    arr = session.query(City).get(id)
    if arr:
        data = request.get_json()
        arr.title = data['title'],
        arr.ar_title = data['ar_title'],
        arr.status = data['status'],
        arr.updated_on = datetime.utcnow(),
        arr.updated_by = currentID
        session.commit()
        session.close()
        return jsonify({'message': 'City updated successfully'}), 200
    return jsonify({'message': 'City not found'}), 404


@city_bp.route('/deletecity/<id>', methods=['DELETE'])
@jwt_required()
def delete_user(id):
    currentID = get_jwt_identity()
    arr = session.query(City).get(id)
    if arr:
        if arr.status == 1:
            arr.status = 3
            session.commit()
            session.close()
            return jsonify({'message': 'City deleted successfully'}), 200
        else:
            return jsonify({'message': 'City is already deleted'}), 200
    else:
        return jsonify({'message': 'City not found'}), 404
    
    
@city_bp.route('/getbyid/<id>')
@jwt_required()
def get_onecity(id):
    currentID = get_jwt_identity()
    arr = session.query(City).filter_by(id=id).first()
    data = {
    "id": arr.id,
    'title':arr.title
    }
    session.close()
    return jsonify(data)