from flask import Blueprint, jsonify,request,render_template
from models.category import Category,db
category_bp = Blueprint('category', __name__)


@category_bp.route('/')
def get_category():

    status_param = request.args.get('status')
    if status_param is not None:
        status = int(status_param)
        if status == 1:
            arr = db.session.query(Category).filter_by(status=1).all()
        else:
            arr = db.session.query(Category).all()
    else:
        arr = db.session.query(Category).all()
    result = []
    for value in arr:
        result.append({
            'id' :value.id,
            'title': value.title,
            'ar_title':value.ar_title,
            'image':value.image,
            'status':value.status
        })
    return jsonify(result)


@category_bp.route('/<id>', methods=['GET'])
def get_user(id):
    arr = db.session.query(Category).get(id)
    if arr:
        return jsonify({
            'id' :arr.id,
            'title': arr.title,
            'ar_title':arr.ar_title,
            'image':arr.image,
            'status':arr.status
        })
    return jsonify({'message': 'Category not found'}), 404


@category_bp.route('/addcategory', methods=['POST'])
def create_category():
    data = request.get_json()
    # Create a new category
    new_category = Category(id=data['id'], title=data['title'],ar_title=data['ar_title'],image=data['image'],status=data['status'])
    db.session.add(new_category)
    db.session.commit()
    return jsonify({'message': 'Category created successfully'}), 201


@category_bp.route('/updatecategory/<id>', methods=['PUT'])
def update_user(id):
    arr = db.session.query(Category).get(id)
    if arr:
        data = request.get_json()
        arr.id = data['id']
        arr.title = data['title'],
        arr.ar_title = data['ar_title'],
        arr.image = data['image'],
        arr.status = data['status'],
        db.session.commit()
        return jsonify({'message': 'Category updated successfully'}), 200
    return jsonify({'message': 'Category not found'}), 404


@category_bp.route('/deletecategory/<id>', methods=['DELETE'])
def delete_user(id):
    arr = db.session.query(Category).get(id)
    if arr:
        if arr.status == 1:
            arr.status = 3
            db.session.commit()
            return jsonify({'message': 'Category deleted successfully'}), 200
        else:
            return jsonify({'message': 'Category is already deleted'}), 200
    else:
        return jsonify({'message': 'Category not found'}), 404