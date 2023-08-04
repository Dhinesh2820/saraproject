from flask import Blueprint, jsonify,request
from flask_jwt_extended import jwt_required,get_jwt_identity
from models.category import Category
from models import session
from datetime import datetime

category_bp = Blueprint('category', __name__)


@category_bp.route('/')
@jwt_required()
def get_category():
    currentID = get_jwt_identity()
    status_param = request.args.get('status')
    if status_param is not None:
        status = int(status_param)
        if status == 1:
            arr = session.query(Category).filter_by(status=1).all()
        else:
            arr = session.query(Category).all()
    else:
        arr = session.query(Category).all()
    result = []
    for categoryData in arr:
        result.append({
            'id' :categoryData.id,
            'title': categoryData.title,
            'ar_title':categoryData.ar_title,
            'image':categoryData.image,
            'status':categoryData.status
        })
    session.close()
    return jsonify(result)


@category_bp.route('/<id>', methods=['GET'])
@jwt_required()
def get_user(id):
    currentID = get_jwt_identity()
    arr = session.query(Category).get(id)
    if arr:
        return jsonify({
            'id' :arr.id,
            'title': arr.title,
            'ar_title':arr.ar_title,
            'image':arr.image,
            'status':arr.status
        })
    session.close()
    return jsonify({'message': 'Category not found'}), 404


@category_bp.route('/addcategory', methods=['POST'])
@jwt_required()
def create_category():
    currentID = get_jwt_identity()
    data = request.get_json()
    # Create a new category
    new_category = Category(title=data['title'],ar_title=data['ar_title'],image=data['image'],status=data['status'],created_by=currentID,updated_by = currentID)
    session.add(new_category)
    session.commit()
    session.close()
    return jsonify({'message': 'Category created successfully'}), 201


@category_bp.route('/updatecategory/<id>', methods=['PUT'])
@jwt_required()
def update_user(id):
    currentID = get_jwt_identity()
    arr = session.query(Category).get(id)
    if arr:
        data = request.get_json()
        arr.title = data['title'],
        arr.ar_title = data['ar_title'],
        arr.image = data['image'],
        arr.status = data['status'],
        arr.updated_on=datetime.utcnow()
        arr.updated_by = currentID
        session.commit()
        session.close()
        return jsonify({'message': 'Category updated successfully'}), 200
    return jsonify({'message': 'Category not found'}), 404


@category_bp.route('/deletecategory/<id>', methods=['DELETE'])
@jwt_required()
def delete_user(id):
    currentID = get_jwt_identity()
    arr = session.query(Category).get(id)
    if arr:
        if arr.status == 1:
            arr.status = 3
            session.commit()
            session.close()
            return jsonify({'message': 'Category deleted successfully'}), 200
        else:
            return jsonify({'message': 'Category is already deleted'}), 200
    else:
        return jsonify({'message': 'Category not found'}), 404