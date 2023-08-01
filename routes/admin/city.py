from flask import Blueprint, jsonify,request,render_template
from models.city import City,db
city_bp = Blueprint('city', __name__)


@city_bp.route('/')
def get_city():

    status_param = request.args.get('status')
    if status_param is not None:
        status = int(status_param)
        if status == 1:
            arr = db.session.query(City).filter_by(status=1).all()
        else:
            arr = db.session.query(City).all()
    else:
        arr = db.session.query(City).all()
    result = []
    for value in arr:
        result.append({
            'id' :value.id,
            'title': value.title,
            'ar_title':value.ar_title,
            'status':value.status
        })
    return jsonify(result)


@city_bp.route('/<id>', methods=['GET'])
def get_user(id):
    arr = db.session.query(City).get(id)
    if arr:
        return jsonify({
            'id' :arr.id,
            'title': arr.title,
            'ar_title':arr.ar_title,
            'status':arr.status
        })
    return jsonify({'message': 'City not found'}), 404


@city_bp.route('/addcity', methods=['POST'])
def create_city():
    data = request.get_json()
    # Create a new city
    new_city = City(id=data['id'], title=data['title'],ar_title=data['ar_title'],status=data['status'])
    db.session.add(new_city)
    db.session.commit()
    return jsonify({'message': 'City created successfully'}), 201


@city_bp.route('/updatecity/<id>', methods=['PUT'])
def update_user(id):
    arr = db.session.query(City).get(id)
    if arr:
        data = request.get_json()
        arr.id = data['id']
        arr.title = data['title'],
        arr.ar_title = data['ar_title'],
        arr.status = data['status'],
        db.session.commit()
        return jsonify({'message': 'City updated successfully'}), 200
    return jsonify({'message': 'City not found'}), 404


@city_bp.route('/deletecity/<id>', methods=['DELETE'])
def delete_user(id):
    arr = db.session.query(City).get(id)
    if arr:
        if arr.status == 1:
            arr.status = 3
            db.session.commit()
            return jsonify({'message': 'City deleted successfully'}), 200
        else:
            return jsonify({'message': 'City is already deleted'}), 200
    else:
        return jsonify({'message': 'City not found'}), 404